from odoo import models, fields

class AllowanceDetail(models.Model):
    _name = 'hr.allowance.detail'
    _description = 'Chi tiết Phụ cấp'

    employee_id = fields.Many2one('my.employee', string="Nhân sự", required=True)
    allowance_id = fields.Many2one('hr.allowance', string="Phụ cấp", required=True)
