from odoo import models, fields, api


class KiemTra(models.Model):
    _name = "benhvien.kiemtra"
    _description = "Quản lý Kiểm Tra"

    ma_kiem_tra = fields.Char(string="Mã kiểm tra", required=True, copy=False, readonly=True, default="Không cần nhập")
    ngay_kiem_tra = fields.Date(string="Ngày kiểm tra")
    ket_qua = fields.Text(string="Kết quả")
    ghi_chu = fields.Text(string="Ghi chú")

    quy_dinh = fields.Many2one("benhvien.quydinh",string="Quy định")

    nhan_su = fields.Many2one("benhvien.nhansu",string="Nhân sự thực hiện")

    @api.model
    def create(self, vals):
        if vals.get('ma_kiem_tra', "New") == "New":
            vals['ma_kiem_tra'] = self.env['ir.sequence'].next_by_code('benhvien.kiemtra') or "KT001"
        return super(KiemTra, self).create(vals)