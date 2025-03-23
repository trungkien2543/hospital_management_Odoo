from odoo import models, fields

class MyExperience(models.Model):
    _name = 'my.experience'
    _description = 'Experience'

    experience_code = fields.Integer(string="Mã Kinh nghiệm", required=True)  # int
    title = fields.Char(string="Tiêu đề", required=True)  # nvarchar
    description = fields.Text(string="Mô tả kinh nghiệm")  # nvarchar
    start_date = fields.Datetime(string="Ngày bắt đầu")  # datetime
    end_date = fields.Datetime(string="Ngày kết thúc")  # datetime
    employee_id = fields.Many2one('my.employee', string="Mã nhân sự", required=True)  # varchar (liên kết với nhân viên)
