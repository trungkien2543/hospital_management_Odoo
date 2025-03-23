from odoo import models, fields

class MyEmployee(models.Model):
    _name = 'my.employee'
    _description = 'Employee'

    employee_code = fields.Char(string="Mã nhân sự", required=True)  # varchar
    name = fields.Char(string="Tên nhân sự", required=True)  # nvarchar
    job_position = fields.Char(string="Tên công việc")  # nvarchar
    address = fields.Char(string="Địa chỉ")  # varchar
    birth_date = fields.Date(string="Ngày sinh")  # date
    gender = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ')
    ], string="Giới tính")  # bit (boolean nhưng thể hiện dưới dạng Selection)
    cccd = fields.Char(string="CCCD")  # varchar
    email = fields.Char(string="Email")  # varchar
    phone = fields.Char(string="Số điện thoại")  # varchar
    image = fields.Image(string="Ảnh")  # nvarchar
    manager_id = fields.Many2one('my.employee', string="Quản lý")  # Many2one tham chiếu nhân viên khác

    experience_ids = fields.One2many('my.experience', 'employee_id', string="Kinh nghiệm")
    skill_ids = fields.One2many('my.skill', 'employee_id', string="Kỹ năng")
    khoa = fields.Many2one('benhvien.khoa', string="Khoa")