from odoo import api, fields, models

class Loaixetnghiem(models.Model):
    _name = "benhvien.loaixetnghiem"
    _description = "Loai Xet Nghiem Management"

    ma_loai = fields.Char(string="Mã loại", required=True)
    name = fields.Char(string="Tên xét nghiệm", required=True)
    mo_ta = fields.Text(string="Mô tả")