from odoo import api, fields, models

class Loaixetnghiem(models.Model):
    _name = "benhvien.loaixetnghiem"
    _description = "Loai Xet Nghiem Management"

    ma_loai = fields.Char(string="Mã chụp", required=True, copy=False, readonly=True, default="Không cần nhập")
    name = fields.Char(string="Tên xét nghiệm", required=True)
    mo_ta = fields.Text(string="Mô tả")

    @api.model
    def create(self, vals):
        if vals.get('ma_loai', "New") == "New":
            vals['ma_loai'] = self.env['ir.sequence'].next_by_code('benhvien.loaixetnghiem') or "LXN001"
        return super(Loaixetnghiem, self).create(vals)