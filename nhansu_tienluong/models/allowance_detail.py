from odoo import models, fields

class AllowanceDetail(models.Model):
    _name = 'benhvien.tienluong.chitietphucap'
    _description = 'Chi tiết Phụ cấp'

    employee_id = fields.Many2one('benhvien.nhansu', string="Nhân sự", required=True)
    allowance_id = fields.Many2one('benhvien.tienluong.phucap', string="Phụ cấp", required=True)
