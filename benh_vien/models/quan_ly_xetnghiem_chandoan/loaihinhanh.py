from odoo import api, fields, models

class Loaihinhanh(models.Model):
    _name = "benhvien.loaihinhanh"
    _description = "Loai Hinh Anh Management"

    ma_loai = fields.Char(string="Mã chụp", required=True, copy=False, readonly=True, default="Không cần nhập")
    name = fields.Char(string="Tên hình ảnh", required=True)
    mo_ta = fields.Text(string="Mô tả")

    @api.model
    def create(self, vals):
        if vals.get('ma_loai', "New") == "New":
            vals['ma_loai'] = self.env['ir.sequence'].next_by_code('benhvien.loaihinhanh') or "LHA001"
        return super(Loaihinhanh, self).create(vals)