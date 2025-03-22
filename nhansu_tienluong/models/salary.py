from odoo import models, fields

class Salary(models.Model):
    _name = 'nhansu_tienluong.salary'
    _description = 'Tiền lương nhân sự'

    employee_id = fields.Many2one('res.partner', string="Nhân sự", required=True)
    month_year = fields.Date(string="Tháng năm", required=True)
    work_days = fields.Integer(string="Số ngày công", required=True)
    overtime_hours = fields.Integer(string="Số giờ làm thêm", required=True)
    base_salary = fields.Integer(string="Lương cơ bản", required=True)
    salary_multiplier = fields.Float(string="Hệ số lương", required=True)
    allowance_id = fields.Many2one('nhansu_tienluong.allowance', string="Phụ cấp")
    tax = fields.Integer(string="Thuế TNCN")
    notes = fields.Text(string="Ghi chú")
