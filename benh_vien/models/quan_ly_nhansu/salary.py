from odoo import models, fields, api

class Salary(models.Model):
    _name = 'benhvien.tienluong'
    _description = 'Tiền Lương'

    code = fields.Char(string="Mã tiền lương", required=True)
    employee_code = fields.Many2one('benhvien.nhansu', string="Nhân sự", required=True)
    month_year = fields.Date(string="Tháng năm", required=True)
    working_days = fields.Integer(string="Số ngày công")
    overtime_hours = fields.Integer(string="Số giờ làm thêm")
    base_salary = fields.Integer(string="Lương cơ bản")
    salary_coefficient = fields.Float(string="Hệ số lương")
    allowance = fields.Integer(string="Phụ cấp", compute="_compute_allowance", store=True)
    tax_income = fields.Integer(string="Thuế TNCN")
    note = fields.Text(string="Ghi chú")

    @api.depends('employee_code')
    def _compute_allowance(self):
        for record in self:
            total = 0
            if record.employee_code:
                # Tìm tất cả phụ cấp của nhân sự này
                allowance_details = self.env['benhvien.tienluong.chitietphucap'].search([
                    ('employee_code', '=', record.employee_code.id)
                ])
                for detail in allowance_details:
                    total += detail.allowance_id.amount
            record.allowance = total
