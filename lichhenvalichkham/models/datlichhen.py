from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime


class DatLichHen(models.Model):
    _name = 'benhvien.lichhen'
    _description = 'Lịch hẹn khám bệnh'

    ma_lich_hen = fields.Char(string="Mã lịch hẹn", readonly=True, copy=False, default="New")
    ten_benh_nhan = fields.Many2one('benhvien.benhnhan', string="Bệnh nhân", required=True)
    phone = fields.Char(string="Số điện thoại")
    email = fields.Char(string="Email")
    bac_si = fields.Many2one('my.employee', string="Bác sĩ phụ trách", required=True)
    ngay_kham = fields.Date(string="Ngày khám", required=True)

    khung_gio = fields.Selection([
        ('08:00-10:00', '08:00 - 10:00'),
        ('10:00-12:00', '10:00 - 12:00'),
        ('13:00-15:00', '13:00 - 15:00'),
        ('15:00-17:00', '15:00 - 17:00'),
        ('17:00-19:00', '17:00 - 19:00'),
        ('19:00-21:00', '19:00 - 21:00'),
    ], string="Khung giờ", required=True)

    ngay_dat_lich = fields.Date(string="Ngày đặt lịch", default=fields.Date.context_today, readonly=True)
    ly_do_kham = fields.Text(string="Lý do khám")
    trang_thai = fields.Selection([
        ('cho_xac_nhan', 'Chờ xác nhận'),
        ('da_xac_nhan', 'Đã xác nhận'),
        ('da_huy', 'Đã hủy')
    ], string="Trạng thái", default="cho_xac_nhan", required=True)

    @api.constrains('ngay_kham')
    def _check_ngay_kham(self):
        """Không cho phép đặt lịch trong quá khứ"""
        today = fields.Date.today()
        for record in self:
            if record.ngay_kham < today:
                raise ValidationError("Không thể đặt lịch khám vào ngày trong quá khứ.")

    @api.model_create_multi
    def create(self, vals_list):
        records = super(DatLichHen, self).create(vals_list)
        for record in records:
            if record.ma_lich_hen == "New":
                record.ma_lich_hen = self.env['ir.sequence'].next_by_code('benhvien.lichhen') or "LH-000"
            record._create_lich_kham()
        return records

    def _create_lich_kham(self):
        """Tự động tạo lịch khám khi bệnh nhân đặt lịch hẹn"""
        for record in self:
            self.env['benhvien.lichkham'].create({
                'ma_lich_hen': record.id,
                'ma_benh_nhan': record.ten_benh_nhan.id,
                'ma_bac_si': record.bac_si.id,
                'ngay_kham': record.ngay_kham,
                'khung_gio': record.khung_gio,
                'trang_thai': 'cho_xac_nhan',
                'ly_do_kham': record.ly_do_kham,
                'ngay_dat_lich': fields.Datetime.now(),
            })
