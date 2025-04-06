from odoo import models, fields

class Allowance(models.Model):
    _name = 'benhvien.tienluong.phucap'
    _description = 'Phụ cấp'
    name = fields.Char(string="Tên phụ cấp", required=True)
    amount = fields.Integer(string="Số tiền", required=True)
