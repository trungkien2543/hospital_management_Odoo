from odoo import api, fields, models

class Sudunggiuongbenh(models.Model):
    _name = "benhvien.sudunggiuongbenh"
    _description = "SudungGiuongbenh Management"

    name = fields.Many2one("benhvien.giuongbenh", string="Số Giường", required=True)
    patient_id = fields.Char(string="Tên Bệnh Nhân", required=True)
    doctor_id = fields.Char(string="Bác Sĩ Phụ Trách", required=True)
    start_time = fields.Datetime(string="Thời Gian Bắt Đầu", required=True)
    end_time = fields.Datetime(string="Thời Gian Kết Thúc", required=True)
