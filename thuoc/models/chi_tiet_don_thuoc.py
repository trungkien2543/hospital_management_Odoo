from odoo import models, fields,api


class ChiTietDonThuoc(models.Model):
    _name = "benhvien.chi_tiet_don_thuoc"
    _description = "Chi tiết đơn thuốc"

    ma_don_thuoc = fields.Many2one("benhvien.don_thuoc", string="Mã đơn thuốc", required=True, ondelete="cascade")
    ma_thuoc = fields.Many2one("benhvien.thuoc", string="Mã thuốc", required=True, ondelete="cascade")
    so_luong = fields.Integer(string="Số lượng",required=True)
    chi_dan = fields.Text(string="Chỉ dẫn",required=True)
    don_vi_tinh = fields.Many2one(
        "benhvien.don_vi_tinh",
        string="Đơn vị tính",
        related="ma_thuoc.don_vi_tinh",
        store=True,
        readonly=True
    )