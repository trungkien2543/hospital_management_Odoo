from odoo import models, fields

class PatientFeedback(models.Model):
    _name = 'clinic.feedback'
    _description = 'Patient Feedback'

    name = fields.Char(string="Tên phản hồi", required=True)  # Trường lưu tên phản hồi
    feedback_type = fields.Selection([
        ('positive', 'Tích cực'),
        ('negative', 'Tiêu cực'),
        ('neutral', 'Trung lập')
    ], string="Loại phản hồi", required=True)
    feedback_text = fields.Text(string="Nội dung phản hồi")
    feedback_date = fields.Datetime(default=fields.Datetime.now, string="Ngày phản hồi")
    resolved = fields.Boolean(string="Đã giải quyết", default=False)  # Thể hiện tình trạng giải quyết
    resolution = fields.Text(string="Giải pháp", help="Giải pháp xử lý phản hồi khi cần thiết")
    
class PatientComplaint(models.Model):
    _name = 'clinic.complaint'
    _description = 'Patient Complaint'

    name = fields.Char(string="Tên khiếu nại", required=True)  # Trường lưu tên khiếu nại
    complaint_type = fields.Selection([
        ('service', 'Chất lượng dịch vụ'),
        ('treatment', 'Điều trị'),
        ('cost', 'Chi phí'),
        ('other', 'Khác')
    ], string="Loại khiếu nại", required=True)
    complaint_text = fields.Text(string="Nội dung khiếu nại")
    complaint_date = fields.Datetime(default=fields.Datetime.now, string="Ngày khiếu nại")
    resolved = fields.Boolean(string="Đã giải quyết", default=False)  # Thể hiện tình trạng giải quyết
    resolution = fields.Text(string="Giải pháp", help="Giải pháp xử lý khiếu nại khi cần thiết")

