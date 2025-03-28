from odoo import models, fields



class PhuongThucThanhToan(models.Model):
    _name = 'benhvien.phuong_thuc_thanh_toan'
    _description = 'Phương Thức Thanh Toán'

    ten_phuong_thuc = fields.Char(string='Tên Phương Thức')
    mo_ta = fields.Text(string='Mô Tả')
