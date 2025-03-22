from odoo import api, fields, models

class DatLichHen(models.Model):
    _name = 'benhvien.lichhen'
    _description = 'Lịch hẹn khám bệnh'

    ma_lich_hen = fields.Char(string="Mã lịch hẹn", readonly=True, copy=False, default="New")
    ten_benh_nhan = fields.Char(string="Họ tên bệnh nhân", required=True)
    phone = fields.Char(string="Số điện thoại")
    email = fields.Char(string="Email")
    bac_si = fields.Char(string="Bác sĩ phụ trách")
    appointment_date = fields.Datetime(string="Ngày giờ hẹn khám", required=True)
    ngay_dat_lich = fields.Date(string="Ngày đặt lịch", required=True, default=fields.Date.context_today)
    ly_do_kham = fields.Text(string="Lý do khám")
    trang_thai = fields.Selection([
        ('draft', 'Mới'),
        ('confirm', 'Đã xác nhận'),
        ('done', 'Hoàn thành'),
        ('cancel', 'Hủy')
    ], string="Trạng thái", default="draft")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('ma_lich_hen', "New") == "New":
                vals['ma_lich_hen'] = self.env['ir.sequence'].next_by_code('benhvien.lichhen') or "LH-000"
        return super().create(vals_list)
