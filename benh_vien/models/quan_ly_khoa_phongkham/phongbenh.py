
from odoo import api, fields, models

class PhongbenhInformation(models.Model):
    _name = "benhvien.phongbenh"
    _description = "PhongBenh Management"

    ma_phong = fields.Char(string="Mã phòng bệnh", required=True, copy=False, readonly=True, default="Không cần nhập")
    name = fields.Char(string="Tên Phòng Bệnh", required=True)
    khoa = fields.Many2one('benhvien.khoa', string="Tên Khoa", required=True)
    bed_count = fields.Integer(string="Số Lượng Giường", default=1)

    giuongbenh_ids = fields.One2many(
        "benhvien.giuongbenh",
        "code_phong",
        string="Danh sách các giường trong phòng"
    )

    @api.model
    def create(self, vals):
        if vals.get('ma_phong', "New") == "New":
            vals['ma_phong'] = self.env['ir.sequence'].next_by_code('benhvien.phongbenh') or "PBENH001"
        return super(PhongbenhInformation, self).create(vals)

    def action_xem_ds_giuong(self):
        return {
            'name': 'Danh sách Giường bệnh',
            'type': 'ir.actions.act_window',
            'res_model': 'benhvien.giuongbenh',
            'view_mode': 'list,form',
            'domain': [('code_phong', '=', self.id)],  # Chỉ hiển thị giường thuộc phòng này
            'target': 'current'
        }