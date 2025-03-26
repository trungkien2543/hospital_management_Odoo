from odoo import fields, models

class GioTrong(models.Model):
    _name = 'benhvien.giotrong'
    _description = "Giờ trống của bác sĩ"

    khung_gio = fields.Char(string="Khung giờ")
    mo_ta = fields.Char(string="Mô tả")
    lichhen_id = fields.Many2one('benhvien.lichhen', string="Lịch hẹn")
