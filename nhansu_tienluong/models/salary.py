from odoo import models, fields

class Salary(models.Model):
    _name = 'benhvien.tienluong'
    _description = 'Tiền Lương'

    code = fields.Char(string="Mã tiền lương", required=True)
    employee_id = fields.Many2one('benhvien.nhansu', string="Nhân sự", required=True)
    month_year = fields.Date(string="Tháng năm", required=True)
    working_days = fields.Integer(string="Số ngày công")
    overtime_hours = fields.Integer(string="Số giờ làm thêm")
    base_salary = fields.Integer(string="Lương cơ bản")
    salary_coefficient = fields.Float(string="Hệ số lương")
    allowance = fields.Integer(string="Phụ cấp")
    tax_income = fields.Integer(string="Thuế TNCN")
    note = fields.Text(string="Ghi chú")
