
from odoo import api, fields, models

class PhongbenhInformation(models.Model):
    _name = "benhvien.phongbenh"
    _description = "PhongBenh Management"

    name = fields.Char(string="Tên Phòng Bệnh", required=True)
    khoa = fields.Many2one('benhvien.khoa', string="Tên Khoa", required=True)
    bed_count = fields.Integer(string="Số Lượng Giường", default=1)

    def action_xem_ds_giuong(self):
        return {
            'name': 'Danh sách Giường bệnh',
            'type': 'ir.actions.act_window',
            'res_model': 'giuongbenh.information',
            'view_mode': 'list,form',
            'domain': [('code_phong', '=', self.id)],  # Chỉ hiển thị giường thuộc phòng này
            'target': 'current'
        }