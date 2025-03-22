
from odoo import api, fields, models

class Khoa(models.Model):
    _name = "benhvien.khoa"
    _description = "Khoa Management"

    ma_khoa = fields.Char(string="Mã khoa", required=True, copy=False, readonly=True, default="KHOA001")
    name = fields.Char(string="Tên khoa")
    description = fields.Text(string="Mô tả khoa")

    phongkham_ids = fields.One2many(
        "benhvien.phongkham",
        "khoa",
        string="Danh sách phòng khám"
    )

    phongbenh_ids = fields.One2many(
        "benhvien.phongbenh",
        "khoa",
        string="Danh sách phòng bệnh"
    )

    @api.model
    def create(self, vals):
        if vals.get('ma_khoa', "New") == "New":
            vals['ma_khoa'] = self.env['ir.sequence'].next_by_code('benhvien.khoa') or "KHOA001"
        return super(Khoa, self).create(vals)