
from odoo import models, fields, api


class ChiTietHoaDon(models.Model):
    _name = 'benhvien.chi_tiet_hoa_don'
    _description = 'Chi Tiết Hóa Đơn'

    hoa_don_id = fields.Many2one('benhvien.hoa_don', string='Hóa Đơn', readonly=True)
    dich_vu = fields.Many2one('benhvien.dich_vu', string='Dịch Vụ', required=True)
    so_luong = fields.Integer(string='Số Lượng', required=True, default=1)
    don_gia = fields.Monetary(string='Đơn giá', currency_field='currency_id', compute='_compute_don_gia', store=True,readonly=True)
    original_price = fields.Monetary(string='DV Chưa Giảm', currency_field='currency_id', compute='_compute_original_price', store=True,readonly=True)
    discount_amount = fields.Monetary(string='Miễn Giảm', currency_field='currency_id', default=0.0,readonly=True,compute='_compute_discount_amount',store=True)
    patient_pay = fields.Monetary(string='Phải Thu', currency_field='currency_id', compute='_compute_patient_pay', store=True,readonly=True)

    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.ref('base.VND').id,
        readonly=True
    )

    @api.depends('dich_vu.don_gia')
    def _compute_don_gia(self):
        for record in self:
            record.don_gia = record.dich_vu.don_gia


    @api.depends('dich_vu.don_gia', 'so_luong')
    def _compute_original_price(self):
        for record in self:
            record.original_price = record.dich_vu.don_gia * record.so_luong


    @api.depends('hoa_don_id.has_bhyt', 'dich_vu.ap_dung_bhyt', 'original_price')
    def _compute_discount_amount(self):
        for record in self:
            if record.hoa_don_id.has_bhyt and record.dich_vu.ap_dung_bhyt:
                record.discount_amount = record.original_price * 0.8  # Giảm 80% nếu áp dụng BHYT
            else:
                record.discount_amount = 0.0


    @api.depends('original_price', 'discount_amount')
    def _compute_patient_pay(self):
        for record in self:
            record.patient_pay = record.original_price - record.discount_amount
