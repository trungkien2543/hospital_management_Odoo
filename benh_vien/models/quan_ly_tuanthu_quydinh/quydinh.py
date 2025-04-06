from odoo import models, fields, api


class QuyDinh(models.Model):
    _name = "benhvien.quydinh"
    _description = "Quản lý Quy Định"
    _rec_name = "mo_ta"

    ma_quy_dinh = fields.Char(string="Mã quy định", required=True, copy=False, readonly=True, default="Không cần nhập")
    mo_ta = fields.Text(string="Mô tả")
    co_quan_ban_hanh = fields.Char(string="Cơ quan ban hành")
    ngay_ban_hanh = fields.Date(string="Ngày ban hành")
    ngay_het_hieu_luc = fields.Date(string="Ngày hết hiệu lực")
    trang_thai = fields.Selection([
        ('hieu_luc', 'Hiệu lực'),
        ('het_hieu_luc', 'Hết hiệu lực'),
    ], string="Trạng thái", default='hieu_luc')



    @api.model
    def create(self, vals):
        if vals.get('ma_quy_dinh', "New") == "New":
            vals['ma_quy_dinh'] = self.env['ir.sequence'].next_by_code('benhvien.quydinh') or "QD001"
        return super(QuyDinh, self).create(vals)