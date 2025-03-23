
from odoo import api, fields, models

class PhongkhamInformation(models.Model):
    _name = "benhvien.phongkham"
    _description = "Phongkham Management"

    ma_phong = fields.Char(string="Mã phòng khám", required=True, copy=False, readonly=True, default="Không cần nhập")
    name = fields.Char(string="Tên Phòng khám")
    loai_phong = fields.Many2one("benhvien.loaiphongkham", string="Loại phòng khám", required=True, ondelete="restrict")
    khoa = fields.Many2one("benhvien.khoa", string="Khoa", required=True)

    sudungphong_ids = fields.One2many(
        "benhvien.sudungphongkham",
        "name",
        string="Lịch sử sử dụng phòng"
    )

    @api.model
    def create(self, vals):
        if vals.get('ma_phong', "New") == "New":
            vals['ma_phong'] = self.env['ir.sequence'].next_by_code('benhvien.phongkham') or "PKHAM001"
        return super(PhongkhamInformation, self).create(vals)
