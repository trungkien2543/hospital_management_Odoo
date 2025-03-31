from odoo import api, fields, models

class Loaixetnghiem(models.Model):
    _name = "benhvien.loaichandoan"
    _description = "Loai Chan Doan Management"

    ma_loai = fields.Char(string="Mã chan doan", required=True, copy=False, readonly=True, default="Không cần nhập")
    name = fields.Char(string="Tên chan doan", required=True)
    mo_ta = fields.Text(string="Mô tả")

    status = fields.Selection([
        ('xetnghiem', 'Xet nghiem'),
        ('chupanh', 'Chup anh')
    ], string="Loai chan doan", store=True)

    @api.model
    def create(self, vals):
        if vals.get('ma_loai', "New") == "New":
            vals['ma_loai'] = self.env['ir.sequence'].next_by_code('benhvien.loaichandoan') or "LCD001"
        return super(Loaixetnghiem, self).create(vals)