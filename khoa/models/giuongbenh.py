
from odoo import api, fields, models

class GiuongbenhInformation(models.Model):
    _name = "benhvien.giuongbenh"
    _description = "Giuongbenh Management"

    ma_giuong = fields.Char(string="Mã giường", required=True, copy=False, readonly=True, default="Không cần nhập")
    name = fields.Char(string="Số thứ tự giường", required=True)
    code_phong = fields.Many2one("benhvien.phongbenh", string="Phòng bệnh")
    type = fields.Selection([('private', 'VIP'), ('public', 'Thường')], default='public', string='Loại giường')
    status = fields.Selection([
        ('free', 'Không sử dụng'),
        ('used', 'Sử dụng')
    ], default='free', string='Trạng thái')

    sudunggiuong_ids = fields.One2many(
        "benhvien.sudunggiuongbenh",
        "name",
        string="Lịch sử sử dụng giường"
    )

    @api.model
    def create(self, vals):
        if vals.get('ma_giuong', "New") == "New":
            vals['ma_giuong'] = self.env['ir.sequence'].next_by_code('benhvien.giuongbenh') or "GIUONG001"
        return super(GiuongbenhInformation, self).create(vals)


    @api.depends('sudunggiuong_ids')
    def _compute_status(self):
        for record in self:
            if record.sudunggiuong_ids:
                record.status = 'used'
            else:
                record.status = 'free'

    status = fields.Selection([
        ('free', 'Không sử dụng'),
        ('used', 'Sử dụng')
    ], string="Trạng thái", compute="_compute_status", store=True)

    # @api.depends('sudunggiuong_ids.start_time', 'sudunggiuong_ids.end_time')
    # def _compute_status(self):
    #     now = datetime.now()
    #     for record in self:
    #         # Kiểm tra nếu có lịch sử sử dụng giường nào đang trong khoảng thời gian hiện tại
    #         is_used = any(sg.start_time <= now <= sg.end_time for sg in record.sudunggiuong_ids)
    #         record.status = 'used' if is_used else 'free'