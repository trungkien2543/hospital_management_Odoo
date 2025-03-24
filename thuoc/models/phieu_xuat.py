from odoo import models, fields, api
from datetime import datetime

class PhieuXuatKho(models.Model):
    _name = 'benhvien.phieu_xuat'
    _description = 'Phiếu Xuất Kho'

    ma_phieu_xuat = fields.Char(string="Mã Phiếu Xuất", required=True, copy=False, readonly=True, default="New")
    ngay_xuat = fields.Date(string="Ngày Xuất", required=True, default=fields.Date.today)
    tong_tien = fields.Float(string="Tổng Tiền", compute="_compute_tong_tien", store=True)
    ghi_chu = fields.Text(string="Ghi Chú")


    chi_tiet_xuat = fields.One2many("benhvien.chi_tiet_phieu_xuat", "ma_phieu", string="Chi Tiết Xuất")

    @api.depends('chi_tiet_xuat.thanh_tien')
    def _compute_tong_tien(self):
        """Tính tổng tiền dựa vào thành tiền của các chi tiết phiếu xuất."""
        for record in self:
            record.tong_tien = sum(record.chi_tiet_xuat.mapped("thanh_tien"))


    @api.model_create_multi
    def create(self, vals_list):
        """
        Ghi đè phương thức create để tự động tạo mã phiếu nhập (ma_phieu_nhap) khi thêm mới bản ghi.
        """
        for vals in vals_list:
            if not vals.get('ma_phieu_xuat') or vals['ma_phieu_nhap'] == 'PX0001':
                vals['ma_phieu_xuat'] = self.env['ir.sequence'].next_by_code('benhvien.phieu_xuat') or 'PX0001'

        return super(PhieuXuatKho, self).create(vals_list)