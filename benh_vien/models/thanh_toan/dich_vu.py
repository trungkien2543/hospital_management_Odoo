from odoo import models, fields


class DichVu(models.Model):
    _name = 'benhvien.dich_vu'
    _description = 'Dịch Vụ'
    _rec_name = 'ten_dich_vu'

    ten_dich_vu = fields.Char(string='Tên Dịch Vụ')

    don_gia = fields.Monetary(string='Đơn Giá', currency_field='currency_id')

    mo_ta = fields.Text(string='Mô Tả')

    bhyt = fields.Boolean(string='Cho phép BHYT')

    currency_id = fields.Many2one(
        'res.currency', 
        string='Currency', 
        default=lambda self: self.env.ref('base.VND').id, 
        readonly=True
    )
