from odoo import models, fields

class MedicalWorkSchedule(models.Model):
    _name = 'medical.work.schedule'
    _description = 'Lịch làm việc hàng ngày của nhân viên y tế'

    employee_id = fields.Many2one('benhvien.nhansu', string='Nhân viên')
    date = fields.Date(string='Ngày làm việc', required=True)
    shift = fields.Selection([
        ('morning', 'Ca sáng'),
        ('afternoon', 'Ca chiều'),
        ('night', 'Ca tối')
    ], string='Ca làm việc', required=True)
    start_time = fields.Float(string='Giờ bắt đầu')  # Ví dụ: 8.0
    end_time = fields.Float(string='Giờ kết thúc')  # Ví dụ: 12.0
    notes = fields.Text(string='Ghi chú')
