from odoo import models, fields

class HoaDon(models.Model):
    _name = "benhvien.hoa_don"
    _description = "Hóa đơn"

    ngay_lap = fields.Date(string="Ngày lập", required=True)
    tong_tien = fields.Monetary(string="Tổng tiền", currency_field="currency_id")
    ghi_chu = fields.Text(string="Ghi chú")
    so_tien_da_thanh_toan = fields.Monetary(string="Số tiền đã thanh toán", currency_field="currency_id")
    con_no = fields.Monetary(string="Còn nợ", currency_field="currency_id")
    so_tien_benh_nhan = fields.Monetary(string="Số tiền bệnh nhân trả", currency_field="currency_id")
    so_tien_BHYT = fields.Monetary(string="Số tiền BHYT trả", currency_field="currency_id")
    trang_thai = fields.Selection([
        ('draft', 'Khởi tạo'),
        ('paid', 'Đã thanh toán'),
        ('due', 'Còn nợ')
    ], string="Trạng thái", default="draft")

    benh_an = fields.Many2one("benhvien.hosobenhan", string="Bệnh án")


    currency_id = fields.Many2one("res.currency", string="Loại tiền tệ")
