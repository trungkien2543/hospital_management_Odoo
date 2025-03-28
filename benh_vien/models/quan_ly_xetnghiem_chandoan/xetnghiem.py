﻿from odoo import api, fields, models

class Xetnghiem(models.Model):
    _name = "benhvien.xetnghiem"
    _description = "Xet Nghiem Management"

    ma_xet_nghiem = fields.Char(string="Mã xét nghiệm", required=True, copy=False, readonly=True, default="Không cần nhập")
    ten_loai_xet_nghiem = fields.Many2one('benhvien.loaixetnghiem', string="Loại xét nghiệm", required=True)
    ma_benh_an = fields.Char(string="Mã bệnh án", required=True)
    ten_bac_si = fields.Char(string="Ten bác sĩ", required=True)
    name = fields.Char(string="Tên mẫu xét nghiệm", required=True)
    thoi_gian_bat_dau = fields.Datetime(string="Thời gian bắt đầu", required=True)
    thoi_gian_ket_thuc = fields.Datetime(string="Thời gian kết thúc")
    trang_thai = fields.Selection([
        ('dang_lay_mau', 'Đang lấy mẫu'),
        ('dang_xet_nghiem', 'Đang xét nghiệm')
    ], default='dang_lay_mau', string='Trạng thái')

    ket_qua = fields.Text(string="Kết quả")

    @api.model
    def create(self, vals):
        if vals.get('ma_xet_nghiem', "New") == "New":
            vals['ma_xet_nghiem'] = self.env['ir.sequence'].next_by_code('benhvien.xetnghiem') or "XN001"
        return super(Xetnghiem, self).create(vals)
