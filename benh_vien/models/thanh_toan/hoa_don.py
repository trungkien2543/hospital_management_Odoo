from odoo import models, fields, api

class HoaDon(models.Model):
    _name = 'benhvien.hoa_don'
    _description = 'Hóa Đơn'

    ngay_lap = fields.Datetime(
        string='Ngày chỉnh sửa gần nhất',
        default=fields.Datetime.now,
        readonly=True,
        store=True,
        compute="_update_ngay_lap"
    )


    tong_tien = fields.Monetary(string='Tổng Tiền', currency_field='currency_id', readonly=True, compute="_compute_tong_tien",store=True)
    ghi_chu = fields.Text(string='Ghi Chú')
    con_no = fields.Monetary(string='Còn Nợ', currency_field='currency_id',readonly=True, compute="_compute_tien_con_no",store=True)


    so_tien_benh_nhan = fields.Monetary(string='Số Tiền Bệnh Nhân', currency_field='currency_id',readonly=True, compute="_compute_tien_benh_nhan",store=True)
    so_tien_bhyt = fields.Monetary(string='Số Tiền BHYT', currency_field='currency_id',readonly=True,compute="_compute_tien_bhyt",store=True)


    so_tien_benh_nhan_da_tra = fields.Monetary(string='Số Tiền Bệnh Nhân Đã Trả', currency_field='currency_id',readonly=True)
    so_tien_bhyt_da_tra = fields.Monetary(string='Số Tiền BHYT Đã Trả', currency_field='currency_id',readonly=True)

    trang_thai = fields.Selection([('draft', 'Khởi tạo'), ('unpaid', 'Chưa Thanh Toán'), ('paid', 'Đã Thanh Toán')],
                                  string='Trạng Thái',readonly=True, compute="_compute_trang_thai",store=True)


    benh_an_id = fields.Many2one(
        'benhvien.hosobenhan',
        string='Bệnh Án',
        ondelete="cascade",
        readonly=True
    )

    chi_tiet_hoa_don_ids = fields.One2many("benhvien.chi_tiet_hoa_don","hoa_don_id",String="Chi tiết hóa đơn")


    phieu_xuat_ids = fields.One2many("benhvien.phieu_xuat","hoa_don",String="Phiếu xuất kho thuốc")



    currency_id = fields.Many2one(
        'res.currency', 
        string='Currency', 
        default=lambda self: self.env.ref('base.VND').id, 
        readonly=True
    )

    _sql_constraints = [
        ('unique_benh_an', 'UNIQUE(benh_an_id)', 'Mỗi hóa đơn chỉ có thể liên kết với một bệnh án!')
    ]

    @api.onchange('benh_an_id')
    def _onchange_benh_an_id(self):
        """ Khi chọn bệnh án bên hóa đơn, cập nhật hóa đơn trong bệnh án """
        if self.benh_an_id:
            self.benh_an_id.hoa_don_id = self

    @api.depends('so_tien_benh_nhan','so_tien_bhyt')
    def _compute_tong_tien(self):
        """Tính tổng tiền dựa vào thành tiền của các dịch vụ."""
        for record in self:
            record.tong_tien = record.so_tien_benh_nhan + record.so_tien_bhyt


    @api.depends('chi_tiet_hoa_don_ids.thanh_tien')
    def _compute_tien_benh_nhan(self):
        """Tính tiền cho bệnh nhân bằng tổng các tiền bệnh nhân trả."""
        for record in self:
            record.so_tien_benh_nhan = sum(record.chi_tiet_hoa_don_ids.mapped("thanh_tien"))




    @api.depends('chi_tiet_hoa_don_ids.gia_bhyt')
    def _compute_tien_bhyt(self):
        """Tính tiền bhyt bằng tổng các tiền bhyt trả."""
        for record in self:
            record.so_tien_bhyt = sum(record.chi_tiet_hoa_don_ids.mapped("gia_bhyt"))


    @api.depends('so_tien_benh_nhan_da_tra','so_tien_bhyt_da_tra','tong_tien')
    def _compute_tien_con_no(self):
        """Tính còn nợ dựa vào số tiền bệnh nhân đã trả và tiền bhyt đã trả"""
        for record in self:
            record.con_no = record.tong_tien - (record.so_tien_benh_nhan_da_tra + record.so_tien_bhyt_da_tra)



    @api.depends('tong_tien', 'con_no')
    def _compute_trang_thai(self):
        """Tự động cập nhật trạng thái dựa trên tổng tiền và còn nợ."""
        for record in self:
            if record.tong_tien > 0:
                if record.con_no > 0:
                    record.trang_thai = 'unpaid'
                else:
                    record.trang_thai = 'paid'
            else:
                record.trang_thai = 'draft'

    @api.depends('tong_tien', 'con_no', 'ghi_chu', 'so_tien_benh_nhan_da_tra', 'so_tien_bhyt_da_tra','chi_tiet_hoa_don_ids')
    def _update_ngay_lap(self):
        """Tự động cập nhật ngày chỉnh sửa gần nhất khi có thay đổi."""
        for record in self:
            record.ngay_lap = fields.Datetime.now()