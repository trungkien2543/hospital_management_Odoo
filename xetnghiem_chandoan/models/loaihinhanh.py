from odoo import api, fields, models

class Loaihinhanh(models.Model):
    _name = "benhvien.loaihinhanh"
    _description = "Loai Hinh Anh Management"

    ma_loai = fields.Char(string="Mã loại", required=True)
    name = fields.Char(string="Tên hình ảnh", required=True)
    mo_ta = fields.Text(string="Mô tả")