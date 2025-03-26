
from odoo import models, fields, api



class HoaDon(models.Model):
    _name = "benhvien.hoa_don"
    _description = "Hóa đơn"

    ngay_lap = fields.Datetime(string="Ngày lập", default=lambda self: fields.Datetime.now(), readonly=True)
    tong_tien = fields.Monetary(string="Tổng tiền", currency_field="currency_id")
    ghi_chu = fields.Text(string="Ghi chú")
    so_tien_da_thanh_toan = fields.Monetary(string="Số tiền đã thanh toán", currency_field="currency_id")
    so_tien_benh_nhan = fields.Monetary(string="Số tiền bệnh nhân trả", currency_field="currency_id")
    so_tien_BHYT = fields.Monetary(string="Số tiền BHYT trả", currency_field="currency_id")
    trang_thai = fields.Selection([
        ('draft', 'Khởi tạo'),
        ('paid', 'Đã thanh toán'),
        ('due', 'Còn nợ')
    ], string="Trạng thái", default="draft")


    currency_id = fields.Many2one("res.currency", string="Loại tiền tệ")

    con_no = fields.Monetary(string="Còn nợ", currency_field="currency_id", compute="_compute_con_no", store=True)

    @api.depends('tong_tien', 'so_tien_da_thanh_toan')
    def _compute_con_no(self):
        for record in self:
            record.con_no = record.tong_tien - record.so_tien_da_thanh_toan