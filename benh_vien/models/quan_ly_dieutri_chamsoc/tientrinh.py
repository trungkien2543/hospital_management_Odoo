from odoo import models, fields, api

class Tientrinh(models.Model):
    _name = "benhvien.tientrinh"
    _description = "Tiến Trình Điều Trị"

    ma_tien_trinh = fields.Char(string="Mã tiến trình", required=True, copy=False, readonly=True, default="Không cần nhập")
    ma_ke_hoach = fields.Many2one("benhvien.kehoachdieutri", string="Mã kế hoạch", required=True)
    ngay_ghi_nhan = fields.Date(string="Ngày ghi nhận", required=True, default=fields.Date.today)
    huyet_ap = fields.Integer(string="Huyết áp")
    nhip_tim = fields.Integer(string="Nhịp tim")
    luong_duong = fields.Integer(string="Lượng đường")
    nhiet_do = fields.Float(string="Nhiệt độ")
    BMI = fields.Float(string="BMI")
    trieu_chung_hien_tai = fields.Text(string="Triệu chứng hiện tại")
    phan_hoi = fields.Text(string="Phản hồi")
    ghi_chu = fields.Text(string="Ghi chú")
    ngay_cap_nhat = fields.Date(string="Ngày cập nhật", default=fields.Date.today)

    @api.model
    def create(self, vals):
        if vals.get('ma_tien_trinh', "New") == "New":
            vals['ma_tien_trinh'] = self.env['ir.sequence'].next_by_code('benhvien.tientrinh') or "TT001"
        return super(Tientrinh, self).create(vals)
    
    def write(self, vals):
        vals['ngay_cap_nhat'] = fields.Date.today()
        return super(Tientrinh, self).write(vals)

    def unlink(self):
        return super(Tientrinh, self).unlink()