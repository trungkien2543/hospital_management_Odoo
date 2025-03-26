from odoo import api, fields, models

class Loaiphongkham(models.Model):
    _name = "benhvien.loaiphongkham"
    _description = "Loai Phong Kham Management"

    ma_loai = fields.Char(string="Mã loại", required=True, copy=False, readonly=True, default="LPK001")
    name = fields.Char(string="Tên loại phòng", required=True)
    mo_ta = fields.Text(string="Mô tả")

    @api.model
    def create(self, vals):
        if vals.get('ma_loai', "New") == "New":
            vals['ma_loai'] = self.env['ir.sequence'].next_by_code('benhvien.loaiphongkham') or "LPK001"
        return super(Loaiphongkham, self).create(vals)