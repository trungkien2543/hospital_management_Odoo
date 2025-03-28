from odoo import models, fields, api

class ChiTietHoaDon(models.Model):
    _name = 'benhvien.chi_tiet_hoa_don'
    _description = 'Chi Tiết Hóa Đơn'

    hoa_don_id = fields.Many2one('benhvien.hoa_don', string='Hóa Đơn')
    dich_vu = fields.Many2one('benhvien.dich_vu', string='Dịch Vụ',required =True)
    so_luong = fields.Integer(string='Số Lượng',required =True,default=1)
    thanh_tien = fields.Monetary(string='Thành Tiền', currency_field='currency_id',readonly=True,compute = '_compute_thanh_tien',store=True)
    don_gia = fields.Monetary(string='Đơn giá', currency_field='currency_id', compute = '_compute_don_gia',store=True,readonly=True)
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.ref('base.VND').id,
        readonly=True
    )



    @api.depends("dich_vu")
    def _compute_don_gia(self):
        """Lấy giá dịch vụ."""
        for record in self:
            record.don_gia = record.dich_vu.don_gia if record.dich_vu else 0.0


    @api.depends("so_luong", "don_gia")
    def _compute_thanh_tien(self):
        """Tính tổng tiền = số lượng * đơn giá."""
        for record in self:
            record.thanh_tien = record.so_luong * record.don_gia if record.so_luong and record.don_gia else 0.0