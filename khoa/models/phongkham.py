
from odoo import api, fields, models

class PhongkhamInformation(models.Model):
    _name = "benhvien.phongkham"
    _description = "Phongkham Management"

    ma_phong = fields.Char(string="Mã phòng khám", required=True, copy=False, readonly=True, default="Không cần nhập")
    name = fields.Char(string="Tên Phòng khám")
    type = fields.Selection([('private','Xét nghiệm'),('public','Phòng khám')], default='public', string='Loại phòng khám')
    khoa = fields.Many2one("benhvien.khoa", string="Khoa", required=True)

    sudungphong_ids = fields.One2many(
        "benhvien.sudungphongkham",
        "name",
        string="Lịch sử sử dụng phòng"
    )

    @api.model
    def create(self, vals):
        if vals.get('ma_phong', "New") == "New":
            vals['ma_phong'] = self.env['ir.sequence'].next_by_code('benhvien.phongkham') or "PKHAM001"
        return super(PhongkhamInformation, self).create(vals)

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
