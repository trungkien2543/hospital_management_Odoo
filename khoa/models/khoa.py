
from odoo import api, fields, models

class Khoa(models.Model):
    _name = "benhvien.khoa"
    _description = "Khoa Management"

    name = fields.Char(string="Tên khoa")
    description = fields.Text(string="Mô tả khoa")
