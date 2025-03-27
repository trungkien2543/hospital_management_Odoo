from odoo import models, fields

class ChiTietHoaDon(models.Model):
    _name = 'benhvien.chi_tiet_hoa_don'
    _description = 'Chi Tiết Hóa Đơn'

    hoa_don_id = fields.Many2one('benhvien.hoa_don', string='Hóa Đơn')
    dich_vu_id = fields.Many2one('benhvien.dich_vu', string='Dịch Vụ')
    so_luong = fields.Integer(string='Số Lượng')
    thanh_tien = fields.Monetary(string='Thành Tiền', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', store=True)