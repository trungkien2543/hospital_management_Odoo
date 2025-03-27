
from odoo import models, fields

class MaThanhToan(models.Model):
    _name = 'benhvien.ma_thanh_toan'
    _description = 'Mã Thanh Toán'

    ngay_thanh_toan = fields.Date(string='Ngày Thanh Toán')
    so_tien = fields.Monetary(string='Số Tiền', currency_field='currency_id')
    mo_ta = fields.Text(string='Mô Tả')
    trang_thai = fields.Selection([('pending', 'Chờ Xử Lý'), ('done', 'Hoàn Thành')], string='Trạng Thái')
    hoa_don_id = fields.Many2one('benhvien.hoa_don', string='Hóa Đơn')
    phuong_thuc_id = fields.Many2one('benhvien.phuong_thuc_thanh_toan', string='Phương Thức Thanh Toán')
    currency_id = fields.Many2one(
        'res.currency', 
        string='Currency', 
        default=lambda self: self.env.ref('base.VND').id, 
        readonly=True
    )