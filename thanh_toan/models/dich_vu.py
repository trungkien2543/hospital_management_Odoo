from odoo import models,fields

class DichVu(models.Model):
    _name = "benhvien.dich_vu"
    _description = "Dịch vụ"

    name = fields.Char(string="Tên dịch vụ", required=True, copy=False)
    don_gia = fields.Monetary(string="Đơn giá", required=True, currency_field="currency_id")
    mo_ta = fields.Text(string="Mô tả")
    currency_id = fields.Many2one("res.currency", string="Loại tiền tệ")

    currency_id = fields.Many2one(
        "res.currency",
        string="Loại tiền tệ",
        default=lambda self: self.env.company.currency_id,
        readonly=True,
        store=False  # Không lưu vào database
    )

