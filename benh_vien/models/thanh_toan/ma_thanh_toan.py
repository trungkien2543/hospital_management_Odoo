from odoo import models, fields, api
from odoo.exceptions import ValidationError


class MaThanhToan(models.Model):
    _name = 'benhvien.ma_thanh_toan'
    _description = 'Mã Thanh Toán'
    _rec_name = 'ma_thanh_toan'

    # Thêm trường "Mã Thanh Toán" sử dụng ir.sequence
    ma_thanh_toan = fields.Char(
        string='Mã Thanh Toán',
        default=lambda self: self.env['ir.sequence'].next_by_code('benhvien.ma_thanh_toan'),
        readonly=True,
        copy=False
    )

    ngay_tao = fields.Datetime(string='Ngày Tạo', default=fields.Datetime.now, readonly=True)
    ngay_thanh_toan = fields.Datetime(
        string='Ngày Thanh Toán',
        compute='_compute_ngay_thanh_toan',
        store=True
    )
    so_tien = fields.Monetary(string='Số Tiền', currency_field='currency_id', required=True)


    mo_ta = fields.Text(string='Mô Tả')

    trang_thai = fields.Selection([
        ('pending', 'Chờ Xử Lý'),
        ('done', 'Hoàn Thành'),
    ], string='Trạng Thái', default='pending', compute="_compute_is_trang_thai_editable", store=True)

    hoa_don_id = fields.Many2one('benhvien.hoa_don', string='Hóa Đơn', required=True, ondelete='cascade')

    is_bhyt = fields.Boolean(string="Mã cho công ty BHYT", default=False, readonly=True)

    phuong_thuc = fields.Selection([
        ('tien_mat', 'Tiền Mặt'),
        ('chuyen_khoan', 'Chuyển Khoản'),
        ('the_tin_dung', 'Thẻ Tín Dụng'),
    ], string="Phương Thức Thanh Toán", default="tien_mat")

    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.ref('base.VND').id,
        readonly=True
    )

    @api.depends('trang_thai')
    def _compute_ngay_thanh_toan(self):
        for record in self:
            if record.trang_thai == 'done' and not record.ngay_thanh_toan:
                record.ngay_thanh_toan = fields.Datetime.now()


    @api.depends('phuong_thuc')
    def _compute_is_trang_thai_editable(self):
        for record in self:
            record.is_trang_thai_editable
