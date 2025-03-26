from odoo import models, fields, api

class MyEmployee(models.Model):
    _name = 'benhvien.nhansu'
    _description = 'Employee'
    _rec_name = 'employee_code'  # Đặt employee_code làm tên hiển thị thay vì id

    employee_code = fields.Char(string="Mã nhân sự", required=True, index=True)  # Khóa chính tùy chỉnh
    name = fields.Char(string="Tên nhân sự", required=True)  
    job_position = fields.Char(string="Tên công việc")  
    address = fields.Char(string="Địa chỉ")  
    birth_date = fields.Date(string="Ngày sinh")  
    gender = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ')
    ], string="Giới tính")  
    cccd = fields.Char(string="CCCD")  
    email = fields.Char(string="Email")  
    phone = fields.Char(string="Số điện thoại")  
    image = fields.Image(string="Ảnh")  
    manager_id = fields.Many2one('benhvien.nhansu', string="Quản lý")  

    experience_ids = fields.One2many('benhvien.nhansu.kinhnghiem', 'employee_code', string="Kinh nghiệm")
    skill_ids = fields.One2many('benhvien.nhansu.kynang', 'employee_code', string="Kỹ năng")
    khoa = fields.Many2one('benhvien.khoa', string="Khoa")

    _sql_constraints = [
        ('unique_employee_code', 'UNIQUE(employee_code)', 'Mã nhân sự phải là duy nhất!')
    ]

    @api.model
    def create(self, vals):
        if 'employee_code' in vals and not vals['employee_code']:
            vals['employee_code'] = self.env['ir.sequence'].next_by_code('benhvien.nhansu') or 'EMP0001'
        return super(MyEmployee, self).create(vals)

    def name_get(self):
        result = []
        for record in self:
            name = f"[{record.employee_code}] {record.name}"
            result.append((record.id, name))
        return result
