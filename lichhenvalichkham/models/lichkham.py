from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools.translate import _

class LichKham(models.Model):
    _name = 'benhvien.lichkham'
    _description = 'Lịch Khám'

    ma_lich_kham = fields.Char(string='Mã Lịch Khám', readonly=True, copy=False, default="New")
    ma_lich_hen = fields.Many2one('benhvien.lichhen', string="Lịch Hẹn Liên Quan", ondelete="cascade")
    ma_benh_nhan = fields.Many2one('benhvien.benhnhan', string='Bệnh Nhân', required=True)
    ma_bac_si = fields.Many2one('my.employee', string='Mã Bác Sĩ', required=True)
    ngay_kham = fields.Date(string="Ngày khám", required=True)
    khung_gio = fields.Selection([
        ('08:00-10:00', '08:00 - 10:00'),
        ('10:00-12:00', '10:00 - 12:00'),
        ('13:00-15:00', '13:00 - 15:00'),
        ('15:00-17:00', '15:00 - 17:00'),
        ('17:00-19:00', '17:00 - 19:00'),
        ('19:00-21:00', '19:00 - 21:00'),
    ], string="Khung giờ", required=True)
    trang_thai = fields.Selection([
        ('cho_xac_nhan', 'Chờ xác nhận'),
        ('da_xac_nhan', 'Đã xác nhận'),
        ('da_huy', 'Đã hủy')
    ], string="Trạng Thái", default="cho_xac_nhan")
    ly_do_kham = fields.Text(string='Lý Do Khám Bệnh')
    ngay_dat_lich = fields.Datetime(string='Ngày Đặt Lịch', default=fields.Datetime.now(), readonly=True)

    @api.constrains('ngay_kham')
    def _check_ngay_kham(self):
        """Không cho phép đặt lịch trong quá khứ"""
        today = fields.Date.today()
        for record in self:
            if record.ngay_kham < today:
                raise ValidationError("Không thể đặt lịch khám vào ngày trong quá khứ.")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('ma_lich_kham', "New") == "New":
                vals['ma_lich_kham'] = self.env['ir.sequence'].next_by_code('benhvien.lichkham') or "LK-000"
        return super().create(vals_list)

    def write(self, vals):
        """Cập nhật trạng thái lịch hẹn khi lịch khám thay đổi"""
        result = super(LichKham, self).write(vals)
        if 'trang_thai' in vals and self.ma_lich_hen:
            self.ma_lich_hen.sudo().write({'trang_thai': vals['trang_thai']})
        return result

    def action_xac_nhan(self):
        """Bác sĩ xác nhận lịch khám và gửi email cho bệnh nhân"""
        self.write({'trang_thai': 'da_xac_nhan'})

        # Lấy template email
        template = self.env.ref('lichhenvalichkham.email_template_lich_kham_xac_nhan')

        # Kiểm tra xem template có tồn tại không
        if template:
            for record in self:
                if record.ma_benh_nhan.email:
                    template.send_mail(record.id, force_send=True)
                else:
                    raise ValidationError(_("Bệnh nhân chưa có email, không thể gửi xác nhận."))


    def action_huy_lich(self):
        """Bác sĩ hủy lịch khám"""
        self.write({'trang_thai': 'da_huy'})
