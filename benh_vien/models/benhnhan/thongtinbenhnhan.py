from odoo import api, fields, models

class BenhNhan(models.Model):
    _name = 'benhvien.benhnhan'
    _description = 'Quản lý thông tin bệnh nhân'
    _rec_name = "ho_ten"  # Hiển thị tên bệnh nhân thay vì ID

    ma_benh_nhan = fields.Char(string="Mã bệnh nhân", readonly=True, copy=False, default="New")
    ho_ten = fields.Char(string='Họ và tên', required=True)
    ngay_sinh = fields.Date(string='Ngày sinh')
    gioi_tinh = fields.Selection(
        [('nam', 'Nam'), ('nu', 'Nữ'), ('khac', 'Khác')],
        string='Giới tính',
        default='nam'
    )
    hosobenhan = fields.One2many('benhvien.hosobenhan', 'ma_benh_nhan', string="Hồ sơ bệnh án")
    sdt = fields.Char(string='Số điện thoại')
    email = fields.Char(string='Email')
    dia_chi = fields.Text(string='Địa chỉ')
    image = fields.Binary(string="Ảnh đại diện", attachment=True)
    lich_su_benh_ly = fields.Text(string="Lịch sử bệnh lý")
    nguoi_lien_he = fields.Char(string="Người liên hệ khẩn cấp")
    nhom_mau = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O')
    ], string="Nhóm máu",default='A')
    ngay_tao = fields.Datetime(string="Ngày tạo", default=fields.Datetime.now)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('ma_benh_nhan', "New") == "New":
                vals['ma_benh_nhan'] = self.env['ir.sequence'].next_by_code('benhvien.benhnhan') or "New"
        return super().create(vals_list)
