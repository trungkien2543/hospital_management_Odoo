from odoo import api, fields, models

class Loaiphongkham(models.Model):
    _name = "benhvien.loaiphongkham"
    _description = "Loai Phong Kham Management"

    ma_loai = fields.Char(string="Mã loại", required=True)
    name = fields.Char(string="Tên loại phòng", required=True)
    mo_ta = fields.Text(string="Mô tả")