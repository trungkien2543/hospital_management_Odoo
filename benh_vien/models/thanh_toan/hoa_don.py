from datetime import date

from odoo import models, fields, api


class HoaDon(models.Model):
    _name = "benhvien.hoa_don"
    _description = "Hóa Đơn"
    _rec_name = 'ma_hoa_don'

    ma_hoa_don = fields.Char(string="Mã Hóa Đơn", required=True, copy=False, readonly=True, default="New")
    created_at = fields.Datetime(string="Ngày Tạo", required=True, default=fields.Datetime.now, readonly=True)
    benh_an_id = fields.Many2one("benhvien.hosobenhan", string="Bệnh Án", required=True)

    has_bhyt = fields.Boolean(string="Có BHYT", compute="_compute_bhyt", store=True)

    chi_tiet_hoa_don = fields.One2many("benhvien.chi_tiet_hoa_don", "hoa_don_id", string="Chi Tiết Hóa Đơn")

    tong_tien = fields.Monetary(string="Tổng Tiền", compute="_compute_tong_tien", store=True,
                                currency_field="currency_id")
    mien_giam = fields.Monetary(string="Tổng Miễn Giảm", compute="_compute_tong_tien", store=True,
                                currency_field="currency_id")
    phai_thu = fields.Monetary(string="Phải Thu", compute="_compute_tong_tien", store=True,
                               currency_field="currency_id")


    chi_tiet_hoa_don_ids = fields.One2many("benhvien.chi_tiet_hoa_don","hoa_don_id",string="Chi tiết hóa đơn")

    phieu_xuat_ids =fields.One2many("benhvien.phieu_xuat","hoa_don",string="Phiếu xuất")


    currency_id = fields.Many2one(
        "res.currency",
        string="Loại tiền tệ",
        default=lambda self: self.env.company.currency_id,
        readonly=True
    )

    @api.depends("chi_tiet_hoa_don.original_price", "chi_tiet_hoa_don.discount_amount", "chi_tiet_hoa_don.patient_pay")
    def _compute_tong_tien(self):
        for record in self:
            record.tong_tien = sum(record.chi_tiet_hoa_don.mapped("original_price"))
            record.mien_giam = sum(record.chi_tiet_hoa_don.mapped("discount_amount"))
            record.phai_thu = sum(record.chi_tiet_hoa_don.mapped("patient_pay"))

    @api.depends('benh_an_id')
    def _compute_bhyt(self):
        """Tự động cập nhật has_bhyt dựa vào thông tin BHYT của bệnh nhân"""
        for record in self:
            record.has_bhyt = False  # Mặc định là không có BHYT
            if record.benh_an_id and record.benh_an_id.ma_benh_nhan:
                benh_nhan = record.benh_an_id.ma_benh_nhan
                today = date.today()

                # Tìm BHYT hợp lệ
                bhyt_hop_le = self.env["benhvien.bhyt"].search([
                    ("ma_benh_nhan", "=", benh_nhan.id),
                    ("ngay_hieu_luc", "<=", today),
                    ("ngay_het_han", ">", today)
                ], limit=1)

                # Nếu có BHYT hợp lệ, cập nhật has_bhyt = True
                if bhyt_hop_le:
                    record.has_bhyt = True


    @api.model
    def create(self, vals):
        """Tự động tạo mã hóa đơn theo sequence"""
        if vals.get('ma_hoa_don', 'New') == 'New':
            vals['ma_hoa_don'] = self.env['ir.sequence'].next_by_code('benhvien.hoa_don') or 'HD00001'

        hoa_don = super(HoaDon, self).create(vals)

        # Kiểm tra nếu hóa đơn có BHYT thì tự động tạo mã thanh toán BHYT
        if hoa_don.has_bhyt:
            self.env['benhvien.ma_thanh_toan'].create({
                'hoa_don_id': hoa_don.id,
                'so_tien': hoa_don.phai_thu,  # Lấy số tiền bệnh nhân phải trả sau khi giảm BHYT
                'trang_thai': 'pending',  # Mặc định là chờ xử lý
                'is_bhyt': True,  # Đánh dấu đây là thanh toán BHYT
                'phuong_thuc': 'bhyt',  # Phương thức thanh toán là BHYT
            })

        return hoa_don
