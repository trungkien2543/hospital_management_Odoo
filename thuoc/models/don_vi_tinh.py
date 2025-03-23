from odoo import models, fields


class DonViTinh(models.Model):
    _name = "benhvien.don_vi_tinh"
    _description = "Đơn vị tính"
    _rec_name = "ten_don_vi"  # Định nghĩa tên hiển thị thay vì ID

    ten_don_vi = fields.Char(string="Tên đơn vị", required=True, copy=False, )

    _sql_constraints = [
        ('unique_ten_don_vi', 'unique(ten_don_vi)', 'Tên đơn vị tính phải là duy nhất!')
    ]