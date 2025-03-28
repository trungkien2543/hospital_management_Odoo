from odoo import api, fields, models

class Hinhanh(models.Model):
    _name = "benhvien.hinhanh"
    _description = "Hinh Anh Management"

    ma_chup = fields.Char(string="Mã chụp", required=True, copy=False, readonly=True, default="Không cần nhập")
    loai_hinh_anh_chup = fields.Many2one('benhvien.loaichandoan', string="Loại hinh anh", required=True)
    ma_bac_si_chup = fields.Char(string="Mã bác sĩ chụp", required=True)
    ma_benh_an = fields.Char(string="Mã bệnh án", required=True)
    name = fields.Char(string="Tên ảnh chụp", required=True)
    thoi_gian_chup = fields.Datetime(string="Thời gian chụp", required=True)
    trang_thai = fields.Selection([
        ('cho_duyet', 'Chờ duyệt'),
        ('da_duyet', 'Đã duyệt'),
        ('huy', 'Hủy')
    ], default='cho_duyet', string='Trạng thái')
    hinh_anh = fields.Binary(string="Hình ảnh", attachment=True)

    @api.model
    def create(self, vals):
        if vals.get('ma_chup', "New") == "New":
            vals['ma_chup'] = self.env['ir.sequence'].next_by_code('benhvien.hinhanh') or "HA001"
        return super(Hinhanh, self).create(vals)