from odoo import api, fields, models

class HoSoBenhAn(models.Model):
    _name = 'benhvien.hosobenhan'
    _description = 'Quản lý hồ sơ bệnh án'

    ma_ho_so = fields.Char(string="Mã hồ sơ bệnh án", readonly=True, copy=False, default="New")
    ma_benh_nhan = fields.Many2one('benhvien.benhnhan', string="Mã bệnh nhân", required=True)
    ma_bac_si = fields.Text(string="Mã bác sĩ phụ trách", required=True)
    chuan_doan = fields.Text(string="Chuẩn đoán bệnh")
    trieu_chung = fields.Text(string="Triệu chứng")
    don_thuoc = fields.Text(string="Đơn thuốc liên quan")
    ngay_kham = fields.Date(string="Ngày khám", required=True, default=fields.Date.context_today)
    ke_hoach_dieu_tri = fields.Text(string="Kế hoạch điều trị")
    hen_ngay_tai_kham = fields.Date(string="Hẹn ngày tái khám")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('ma_ho_so', "New") == "New":
                vals['ma_ho_so'] = self.env['ir.sequence'].next_by_code('benhvien.hosobenhan') or "HS-000"
        return super().create(vals_list)
