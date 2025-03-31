from odoo import models, fields, api

class Kehoachdieutri(models.Model):
    _name = "benhvien.kehoachdieutri"
    _description = "Ke Hoach Dieu Tri Management"

    ma_kehoach = fields.Char(string="Mã kế hoạch", required=True, copy=False, readonly=True, default="Không cần nhập")
    name = fields.Char(string="Tên kế hoạch", required=True)
    mo_ta = fields.Text(string="Mô tả")

    ma_benh_an = fields.Integer(string="Mã bệnh án", required=True)
    ma_bac_si = fields.Integer(string="Mã bác sĩ", required=True)
    ngay_bat_dau = fields.Date(string="Ngày bắt đầu", required=True)
    ngay_ket_thuc = fields.Date(string="Ngày kết thúc")
    ngay_tao = fields.Date(string="Ngày tạo", default=fields.Date.today)
    ngay_cap_nhat = fields.Date(string="Ngày cập nhật", default=fields.Date.today)

    trang_thai = fields.Selection([
        ('dangdieutri', 'Đang điều trị'),
        ('theodoithem', 'Theo dõi thêm'),
        ('choxuly', 'Chờ xử lý'),
        ('hoanthanh', 'Hoàn thành'),
        ('huybo', 'Hủy bỏ')
    ], string="Trạng thái", store=True)

    @api.model
    def create(self, vals):
        if vals.get('ma_kehoach', "New") == "New":
            vals['ma_kehoach'] = self.env['ir.sequence'].next_by_code('benhvien.kehoachdieutri') or "KH001"
        return super(Kehoachdieutri, self).create(vals)
    
    def write(self, vals):
        vals['ngay_cap_nhat'] = fields.Date.today()
        return super(Kehoachdieutri, self).write(vals)

    def unlink(self):
        for record in self:
            if record.trang_thai == 'hoanthanh':
                raise UserError("Không thể xóa kế hoạch đã hoàn thành.")
        return super(Kehoachdieutri, self).unlink()
