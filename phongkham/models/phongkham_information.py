
from odoo import api, fields, models

class PhongkhamInformation(models.Model):
    _name = "benhvien.phongkham"
    _description = "Phongkham Management"

    name = fields.Char(string="Tên Phòng khám")
    type = fields.Selection([('private','Xét nghiệm'),('public','Phòng khám')], default='public', string='Loại phòng khám')
    khoa = fields.Many2one("benhvien.khoa", string="Khoa", required=True)



    def action_xem_phong(self):
        return {
            'name': 'Xem Sử dụng Phòng khám',
            'type': 'ir.actions.act_window',
            'res_model': 'benhvien.sudungphongkham',
            'view_mode': 'list,form',
            'domain': [('name', '=', self.id)],  # Chỉ hiển thị phòng khám này
            'target': 'current'
        }

    def action_tao_phong(self):
        print("Context:", {
            'default_name': self.name,  # Điền sẵn tên phòng khám
        })
        return {
            'name': 'Tạo mới Sử dụng Phòng khám',
            'type': 'ir.actions.act_window',
            'res_model': 'benhvien.sudungphongkham',
            'view_mode': 'form',
            'target': 'current',
            'context': {
                'default_name': self.id,  # Điền sẵn tên phòng khám
            }
        }
