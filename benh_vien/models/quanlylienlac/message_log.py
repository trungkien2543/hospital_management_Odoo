# models/message_log.py
from odoo import models, fields

class PatientMessageLog(models.Model):
    _name = 'clinic.message.log'
    _description = 'Patient Message Log'

    patient_id = fields.Many2one( 'benhvien.hosobenhan', string="Bệnh nhân")
    message_type = fields.Selection([('email', 'Email'), ('sms', 'SMS')], required=True, string="Hình thức")
    subject = fields.Char(string="Tiêu đề")
    content = fields.Text(string="Nội dung")
    sent_date = fields.Datetime(default=fields.Datetime.now, string="Ngày gửi")
    status = fields.Selection([('sent', 'Sent'), ('failed', 'Failed')], default='sent', string="Trạng thái")
