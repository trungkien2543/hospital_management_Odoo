
from odoo import models, fields, api

class PhieuXuatKho(models.Model):
    _name = 'benhvien.phieu_xuat'
    _description = 'Phiếu Xuất Kho'

    ma_phieu_xuat = fields.Char(string="Mã Phiếu Xuất", required=True, copy=False, readonly=True, default="New")
    ngay_xuat = fields.Datetime(string="Ngày Xuất", required=True, default=fields.Datetime.now, readonly=True)
    ghi_chu = fields.Text(string="Ghi Chú")

    hoa_don = fields.Many2one("benhvien.hoa_don", string="Hóa đơn")

    currency_id = fields.Many2one(
        "res.currency",
        string="Loại tiền tệ",
        default=lambda self: self.env.company.currency_id,
        readonly=True
    )

    chi_tiet_xuat = fields.One2many("benhvien.chi_tiet_phieu_xuat", "ma_phieu", string="Chi Tiết Xuất")

    # 🟢 Tổng tiền chưa giảm
    tong_tien_chua_giam = fields.Monetary(
        string="Tổng Tiền Chưa Giảm",
        compute="_compute_tong_tien",
        store=True,
        currency_field="currency_id"
    )

    # 🟢 Tổng miễn giảm
    tong_mien_giam = fields.Monetary(
        string="Tổng Miễn Giảm",
        compute="_compute_tong_tien",
        store=True,
        currency_field="currency_id"
    )

    # 🟢 Tổng phải thu
    tong_phai_thu = fields.Monetary(
        string="Tổng Phải Thu",
        compute="_compute_tong_tien",
        store=True,
        currency_field="currency_id"
    )

    @api.depends('chi_tiet_xuat.gia_chua_giam', 'chi_tiet_xuat.mien_giam', 'chi_tiet_xuat.phai_thu')
    def _compute_tong_tien(self):
        """Tính tổng tiền của phiếu xuất"""
        for record in self:
            record.tong_tien_chua_giam = sum(record.chi_tiet_xuat.mapped("gia_chua_giam"))
            record.tong_mien_giam = sum(record.chi_tiet_xuat.mapped("mien_giam"))
            record.tong_phai_thu = sum(record.chi_tiet_xuat.mapped("phai_thu"))
