from odoo import models, fields, api


class ChungNhan(models.Model):
    _name = "benhvien.chungnhan"
    _description = "Quản lý Chứng Nhận"

    ma_chung_nhan = fields.Char(string="Mã chứng nhận", required=True, copy=False, readonly=True, default="Không cần nhập")
    ten_chung_nhan = fields.Char(string="Tên chứng nhận", required=True)
    ngay_cap = fields.Date(string="Ngày cấp")
    ngay_het_han = fields.Date(string="Ngày hết hạn")
    trang_thai = fields.Selection([
        ('hieu_luc', 'Hiệu lực'),
        ('het_han', 'Hết hạn'),
    ], string="Trạng thái", default='hieu_luc')

    @api.model
    def create(self, vals):
        if vals.get('ma_chung_nhan', "New") == "New":
            vals['ma_chung_nhan'] = self.env['ir.sequence'].next_by_code('benhvien.chungnhan') or "CN001"
        return super(ChungNhan, self).create(vals)