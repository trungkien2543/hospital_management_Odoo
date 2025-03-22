from odoo import models, fields, api

class PhieuNhap(models.Model):
    _name = 'hospital.phieu_nhap'
    _description = 'Phiếu Nhập'
    _rec_name = "ma_phieu_nhap"

    ma_phieu_nhap = fields.Char(string="Mã Phiếu Nhập", required=True, copy=False, readonly=True, default='New')
    tong_tien = fields.Float(string="Tổng Tiền", required=True)
    hinh_thuc_thanh_toan = fields.Selection([
        ('tien_mat', 'Tiền mặt'),
        ('chuyen_khoan', 'Chuyển khoản'),
        ('the_tin_dung', 'Thẻ tín dụng')
    ], string="Hình Thức Thanh Toán", required=True)
    ghi_chu = fields.Text(string="Ghi Chú")
    nha_cung_cap = fields.Many2one('res.partner', string="Nhà Cung Cấp", required=True)

    @api.model
    def create(self, vals):
        if vals.get('ma_phieu_nhap', 'PN0001') == 'PN0001':
            vals['ma_phieu_nhap'] = self.env['ir.sequence'].next_by_code('hospital.phieu_nhap') or 'PN0001'
        return super(PhieuNhap, self).create(vals)
