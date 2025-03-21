from odoo import api, fields, models

class Xetnghiem(models.Model):
    _name = "benhvien.xetnghiem"
    _description = "Xet Nghiem Management"

    ma_xet_nghiem = fields.Char(string="Mã xét nghiệm", required=True)
    ten_loai_xet_nghiem = fields.Char(string="Tên loại xét nghiệm", required=True)
    ma_benh_an = fields.Char(string="Ma benh an", required=True)
    ten_bac_si = fields.Char(string="Ten bac si", required=True)
    name = fields.Char(string="Tên mẫu xét nghiệm", required=True)
    thoi_gian_bat_dau = fields.Datetime(string="Thời gian bắt đầu", required=True)
    thoi_gian_ket_thuc = fields.Datetime(string="Thời gian kết thúc")
    trang_thai = fields.Selection([
        ('dang_lay_mau', 'Đang lấy mẫu'),
        ('dang_xet_nghiem', 'Đang xét nghiệm')
    ], default='dang_lay_mau', string='Trạng thái')
    ket_qua = fields.Text(string="Kết quả")
