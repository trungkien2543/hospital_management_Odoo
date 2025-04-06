from odoo import api, fields, models

class Hinhanh(models.Model):
    _name = "benhvien.hinhanh"
    _description = "Hinh Anh Management"

    ma_chup = fields.Char(string="Mã chụp", required=True, copy=False, readonly=True, default="Không cần nhập")
    loai_hinh_anh_chup = fields.Many2one('benhvien.loaichandoan', string="Loại hinh anh", required=True)
    ma_bac_si_chup = fields.Many2one("benhvien.nhansu", string="Bác Sĩ Phụ Trách", required=True)
    ma_benh_an = fields.Many2one("benhvien.hosobenhan", string="Mã Bệnh án", required=True)
    name = fields.Char(string="Tên ảnh chụp", required=True)
    thoi_gian_chup = fields.Datetime(string="Thời gian chụp", required=True)
    trang_thai = fields.Selection([
        ('dang_chup', 'đang chụp'),
        ('da_chup', 'đã chụp'),
        ('huy', 'Hủy')
    ], default='dang_chup', string='Trạng thái')
    hinh_anh = fields.Binary(string="Hình ảnh", attachment=True)

    @api.model
    def create(self, vals):
        if vals.get('ma_chup', "New") == "New":
            vals['ma_chup'] = self.env['ir.sequence'].next_by_code('benhvien.hinhanh') or "HA001"
        return super(Hinhanh, self).create(vals)