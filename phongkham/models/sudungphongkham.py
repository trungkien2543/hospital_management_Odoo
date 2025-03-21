
from odoo import api, fields, models

class SudungPhongkham(models.Model):
    _name = "benhvien.sudungphongkham"
    _description = "Su dung Phong kham Management"

    name = fields.Many2one("benhvien.phongkham", string="Phòng khám", required=True)
    doctor_id = fields.Char(string="Bác sĩ", required=True)
    start_time = fields.Datetime(string="Thời gian bắt đầu", required=True)
    end_time = fields.Datetime(string="Thời gian kết thúc", required=True)
    status = fields.Selection([
        ('in_use', 'Đang sử dụng'),
        ('no_use', 'Không sử dụng')
    ], string="Trạng thái", default='no_use', required=True)
    description = fields.Text(string="Mô tả sử dụng")
