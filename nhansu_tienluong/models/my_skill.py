from odoo import models, fields

class MySkill(models.Model):
    _name = 'benhvien.nhansu.kynang'
    _description = 'Skill'

    skill_code = fields.Integer(string="Mã Kỹ năng", required=True)  # int
    skill_type = fields.Char(string="Loại kỹ năng", required=True)  # nvarchar
    title = fields.Char(string="Tiêu đề", required=True)  # nvarchar
    level = fields.Integer(string="Phân cấp")  # int
    employee_id = fields.Many2one('benhvien.nhansu', string="Mã nhân sự", required=True)  # varchar (liên kết với nhân viên)
