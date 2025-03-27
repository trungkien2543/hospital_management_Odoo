from odoo import models, fields, api



class HoaDon(models.Model):
    _name = 'benhvien.hoa_don'
    _description = 'Hóa Đơn'

    ngay_lap = fields.Datetime(string='Ngày Lập',default=fields.Datetime.now,readonly=True)
    tong_tien = fields.Monetary(string='Tổng Tiền', currency_field='currency_id', readonly=True)
    ghi_chu = fields.Text(string='Ghi Chú')
    con_no = fields.Monetary(string='Còn Nợ', currency_field='currency_id',readonly=True)
    so_tien_benh_nhan = fields.Monetary(string='Số Tiền Bệnh Nhân', currency_field='currency_id',readonly=True)
    so_tien_bhyt = fields.Monetary(string='Số Tiền BHYT', currency_field='currency_id',readonly=True)
    trang_thai = fields.Selection([('draft', 'Khởi tạo'), ('unpaid', 'Chưa Thanh Toán'), ('paid', 'Đã Thanh Toán')],
                                  string='Trạng Thái',readonly=True)

    benh_an_id = fields.Many2one(
        'benhvien.hosobenhan',
        string='Bệnh Án',
        ondelete="cascade",
        readonly=True
    )

    currency_id = fields.Many2one('res.currency', string='Currency', store=True)

    _sql_constraints = [
        ('unique_benh_an', 'UNIQUE(benh_an_id)', 'Mỗi hóa đơn chỉ có thể liên kết với một bệnh án!')
    ]

    @api.onchange('benh_an_id')
    def _onchange_benh_an_id(self):
        """ Khi chọn bệnh án bên hóa đơn, cập nhật hóa đơn trong bệnh án """
        if self.benh_an_id:
            self.benh_an_id.hoa_don_id = self