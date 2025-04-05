from odoo import models, fields, api



class DonThuoc(models.Model):
    _name = "benhvien.don_thuoc"
    _description = "Đơn thuốc"

    ma_don_thuoc = fields.Char(string="Mã đơn thuốc", required=True, copy=False, readonly=True, default='New')
    ngay_ke_don = fields.Date(string="Ngày kê đơn",readonly=True,default=fields.Date.today())
    ghi_chu = fields.Text(string="Ghi chú")
    dan_do = fields.Text(string="Dặn dò")
    chan_doan = fields.Text(string="Chẩn đoán")
    hen_ngay_tai_kham = fields.Date(string="Hẹn ngày tái khám")
    chi_tiet_don_thuoc_ids = fields.One2many("benhvien.chi_tiet_don_thuoc", "ma_don_thuoc", string="Chi tiết đơn thuốc")

    ho_so_benh = fields.Many2one("benhvien.hosobenhan",string="Hồ sơ bệnh án")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('ma_don_thuoc') or vals['ma_don_thuoc'] == 'DT0001':
                vals['ma_don_thuoc'] = self.env['ir.sequence'].next_by_code('benhvien.don_thuoc') or 'DT0001'

        return super(DonThuoc, self).create(vals_list)