from odoo import models, fields, api

class PhieuNhap(models.Model):
    _name = "benhvien.phieu_nhap"
    _description = 'Phiếu Nhập Kho Dược Phẩm'

    ma_phieu_nhap = fields.Char(string="Mã Phiếu Nhập", required=True, copy=False, readonly=True, default='New')
    tong_tien = fields.Float(string="Tổng Tiền", compute="_compute_tong_tien", store=True)
    hinh_thuc_thanh_toan = fields.Selection([
        ('tien_mat', 'Tiền mặt'),
        ('chuyen_khoan', 'Chuyển khoản'),
        ('the_tin_dung', 'Thẻ tín dụng')
    ], string="Hình Thức Thanh Toán", required=True)
    ghi_chu = fields.Text(string="Ghi Chú")
    nha_cung_cap = fields.Many2one('res.partner', string="Nhà Cung Cấp", required=True)
    lo_hang_ids = fields.One2many('benhvien.lo_hang', 'phieu_nhap', string="Lô Hàng Nhập Kho")

    trang_thai = fields.Selection([
        ('draft', 'Nháp'),
        ('confirmed', 'Đã Xác Nhận'),
        ('done', 'Hoàn Thành'),
        ('cancel', 'Hủy')
    ], string="Trạng Thái", default="draft", required=True)

    @api.depends('lo_hang_ids.gia_nhap', 'lo_hang_ids.so_luong_ton_kho')
    def _compute_tong_tien(self):
        for record in self:
            record.tong_tien = sum(lh.gia_nhap * lh.so_luong_ton_kho for lh in record.lo_hang_ids)

    @api.model_create_multi
    def create(self, vals_list):
        """
        Ghi đè phương thức create để tự động tạo mã phiếu nhập (ma_phieu_nhap) khi thêm mới bản ghi.
        """
        for vals in vals_list:
            if not vals.get('ma_phieu_nhap') or vals['ma_phieu_nhap'] == 'PN0001':
                vals['ma_phieu_nhap'] = self.env['ir.sequence'].next_by_code('benhvien.phieu_nhap') or 'PN0001'

        return super(PhieuNhap, self).create(vals_list)
