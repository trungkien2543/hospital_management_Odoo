from odoo import models, fields, api

class MyEmployee(models.Model):
    _name = 'benhvien.nhansu'
    _description = 'Nhân viên y tế'
    _rec_name = 'name'  # Đặt employee_code làm tên hiển thị thay vì id

    employee_code = fields.Char(string="Mã nhân sự", required=True, index=True)  # Khóa chính tùy chỉnh

    # --- Thông tin cá nhân ---
    name = fields.Char(string='Họ và tên', required=True)
    gender = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ'),
        ('other', 'Khác')
    ], string='Giới tính')
    date_of_birth = fields.Date(string='Ngày sinh')
    phone = fields.Char(string='Số điện thoại')
    email = fields.Char(string='Email')
    address = fields.Text(string='Địa chỉ')
    cccd = fields.Char(string="CCCD")  

    sudungphongkham_id = fields.Many2one("benhvien.sudungphongkham", string="Sử dụng phòng khám")

    # --- Chuyên môn ---
    specialization = fields.Char(string='Chuyên môn')
    qualifications = fields.Text(string='Bằng cấp')
    certifications = fields.Text(string='Chứng chỉ')

    # --- Lịch làm việc ---
    work_schedule_ids = fields.One2many(
        'medical.work.schedule',
        'employee_id',
        string='Lịch làm việc'
    )

    # --- Đánh giá hiệu suất ---
    performance_ids = fields.One2many(
        'medical.performance.review',
        'employee_id',
        string='Đánh giá hiệu suất'
    )


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