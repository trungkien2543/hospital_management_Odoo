
from odoo import api, fields, models

class GiuongbenhInformation(models.Model):
    _name = "benhvien.giuongbenh"
    _description = "Giuongbenh Management"

    ma_giuong = fields.Char(string="Mã giường", required=True, copy=False, readonly=True, default="Không cần nhập")
    name = fields.Char(string="Số thứ tự giường", required=True)
    code_phong = fields.Many2one("benhvien.phongbenh", string="Phòng bệnh")
    type = fields.Selection([('private','VIP'),('public','Thường')], default='public', string='Loại giường')
    status = fields.Selection([
        ('free', 'Không sử dụng'),
        ('used', 'Sử dụng')
    ], default='free', string='Trạng thái')


    @api.model
    def create(self, vals):
        if vals.get('ma_giuong', "New") == "New":
            vals['ma_giuong'] = self.env['ir.sequence'].next_by_code('benhvien.giuongbenh') or "GIUONG001"
        return super(GiuongbenhInformation, self).create(vals)

    def action_xem_giuong(self):
        return {
            'name': 'Xem Sử dụng Giường bệnh',
            'type': 'ir.actions.act_window',
            'res_model': 'benhvien.sudunggiuongbenh',
            'view_mode': 'list,form',
            'domain': [('code_giuong', '=', self.id)],  # Chỉ hiển thị giường thuộc phòng này
            'target': 'current'
        }

    def action_tao_giuong(self):
        print("Context:", {
            'default_name': self.name,  # Điền sẵn tên phòng khám
        })
        return {
            'name': 'Tạo mới Sử dụng Giường bệnh',
            'type': 'ir.actions.act_window',
            'res_model': 'benhvien.sudunggiuongbenh',
            'view_mode': 'form',
            'domain': [('code_giuong', '=', self.id)],  # Chỉ hiển thị giường thuộc phòng này
            'target': 'current',
            'context': {
                'default_code_phong': self.code_phong.id,  # Điền sẵn phòng bệnh
                'default_code_giuong': self.id,  # Điền sẵn giường bệnh
            }
        }