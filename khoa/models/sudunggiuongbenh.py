
from odoo import api, fields, models

class Sudunggiuongbenh(models.Model):
    _name = "benhvien.sudunggiuongbenh"
    _description = "SudungGiuongbenh Management"

    code_phong = fields.Many2one("phongbenh.information", string="Phòng Bệnh", required=True)
    code_giuong = fields.Many2one(
        "giuongbenh.information",
        string="Số Giường",
        domain="[('code_phong', '=', code_phong)]"  # Chỉ hiển thị giường của phòng đã chọn
    )

    patient_id = fields.Char(
        string="Tên Bệnh Nhân",
        required=True
    )

    doctor_id = fields.Char(
        string="Bác Sĩ Phụ Trách",
        required=True
    )

    start_time = fields.Datetime(
        string="Thời Gian Bắt Đầu",
        required=True
    )

    end_time = fields.Datetime(
        string="Thời Gian Kết Thúc",
        required=True
    )
