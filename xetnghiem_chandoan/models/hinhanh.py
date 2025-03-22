from odoo import api, fields, models

class Hinhanh(models.Model):
    _name = "benhvien.hinhanh"
    _description = "Hinh Anh Management"

    ma_chup = fields.Char(string="Mã chụp", required=True)
    loai_hinh_anh_chup = fields.Char(string="Loại hình ảnh chụp", required=True)
    ma_bac_si_chup = fields.Char(string="Mã bác sĩ chụp", required=True)
    ma_benh_an = fields.Char(string="Mã bệnh án", required=True)
    name = fields.Char(string="Tên ảnh chụp", required=True)
    thoi_gian_chup = fields.Datetime(string="Thời gian chụp", required=True)
    thoi_gian_ket_thuc = fields.Datetime(string="Thời gian kết thúc")
    trang_thai = fields.Selection([
        ('cho_duyet', 'Chờ duyệt'),
        ('da_duyet', 'Đã duyệt'),
        ('huy', 'Hủy')
    ], default='cho_duyet', string='Trạng thái')
    duong_dan_anh = fields.Char(string="Đường dẫn ảnh")
