from odoo import models, fields

class MyExperience(models.Model):
    _name = 'benhvien.nhansu.kinhnghiem'
    _description = 'Experience'

    title = fields.Char(string="Tiêu đề", required=True)  # nvarchar
    description = fields.Text(string="Mô tả kinh nghiệm")  # nvarchar
    start_date = fields.Datetime(string="Ngày bắt đầu")  # datetime
    end_date = fields.Datetime(string="Ngày kết thúc")  # datetime
    employee_code = fields.Many2one('benhvien.nhansu', string="Nhân sự", ondelete='cascade')
