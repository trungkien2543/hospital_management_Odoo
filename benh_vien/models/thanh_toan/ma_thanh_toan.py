from odoo import models, fields, api

class MaThanhToan(models.Model):
    _name = 'benhvien.ma_thanh_toan'
    _description = 'Mã Thanh Toán'
    _rec_name = 'ngay_thanh_toan'

    ngay_tao = fields.Datetime(string='Ngày Tạo', default=fields.Datetime.now, readonly=True)
    ngay_thanh_toan = fields.Datetime(
        string='Ngày Thanh Toán',
        compute='_compute_ngay_thanh_toan',
        store=True
    )
    so_tien = fields.Monetary(string='Số Tiền', currency_field='currency_id',required=True)
    mo_ta = fields.Text(string='Mô Tả')

    trang_thai = fields.Selection([
        ('pending', 'Chờ Xử Lý'),
        ('done', 'Hoàn Thành'),
    ], string='Trạng Thái', default='pending')

    hoa_don_id = fields.Many2one('benhvien.hoa_don', string='Hóa Đơn',required=True, ondelete='cascade')

    is_bhyt = fields.Boolean(string="Áp dụng BHYT",default=False, readonly=True)

    phuong_thuc = fields.Selection([
        ('tien_mat', 'Tiền Mặt'),
        ('chuyen_khoan', 'Chuyển Khoản'),
        ('the_tin_dung', 'Thẻ Tín Dụng'),
        ('bhyt', 'Bảo Hiểm Y Tế'),
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


