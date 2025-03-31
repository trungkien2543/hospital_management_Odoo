
from odoo import api, fields, models

class Khoa(models.Model):
    _name = "benhvien.khoa"
    _description = "Khoa Management"

    ma_khoa = fields.Char(string="Mã khoa", required=True, copy=False, readonly=True, default="Không cần nhập")
    name = fields.Char(string="Tên khoa")
    description = fields.Text(string="Mô tả khoa")

    # nhansu_ids = fields.One2many("benhvien.nhansu", "khoa", string="Danh sách nhân viên")

    phongkham_ids = fields.One2many(
        "benhvien.phongkham",
        "khoa",
        string="Danh sách phòng khám và các phòng chức năng"
    )

    phongbenh_ids = fields.One2many(
        "benhvien.phongbenh",
        "khoa",
        string="Danh sách phòng bệnh"
    )

    so_phong_kham_xet_nghiem = fields.Integer(
        string="Số phòng khám",
        compute="_compute_so_phong_kham_xet_nghiem",
        store=True
    )

    so_phong_benh = fields.Integer(
        string="Số phòng bệnh",
        compute="_compute_so_phong_benh",
        store=True
    )

    @api.depends("phongkham_ids")
    def _compute_so_phong_kham_xet_nghiem(self):
        for record in self:
            record.so_phong_kham_xet_nghiem = len(record.phongkham_ids)

    @api.depends("phongkham_ids", "phongbenh_ids")
    def _compute_so_phong_benh(self):
        for record in self:
            record.so_phong_benh = len(record.phongbenh_ids)

    @api.model
    def create(self, vals):
        if vals.get('ma_khoa', "New") == "New":
            vals['ma_khoa'] = self.env['ir.sequence'].next_by_code('benhvien.khoa') or "KHOA001"
        return super(Khoa, self).create(vals)