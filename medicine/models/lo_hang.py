from odoo import models, fields, api

class LoHang(models.Model):
    _name = "benhvien.lo_hang"
    _description = "Lô Hàng Dược Phẩm"
    _rec_name = "ma_lo_hang"  # Hiển thị tên lô hàng trên các form liên quan

    ma_lo_hang = fields.Char(string="Mã Lô Hàng", required=True, copy=False)
    han_su_dung = fields.Date(string="Hạn Sử Dụng", required=True)
    ngay_nhap = fields.Date(string="Ngày Nhập", required=True, default=fields.Date.today)
    gia_nhap = fields.Float(string="Giá Nhập", required=True)
    gia_ban = fields.Float(string="Giá Bán", required=True)
    so_luong_ton_kho = fields.Integer(string="Số lượng tồn kho", required=True, default=0)
    trang_thai = fields.Selection([
        ('con_hang', 'Còn Hàng'),
        ('het_hang', 'Hết Hàng'),
        ('khong_su_dung', 'Không Sử Dụng')
    ], string="Trạng Thái", default="con_hang", required=True)
    tinh_trang_chat_luong = fields.Text(string="Tình Trạng Chất Lượng")

    thuoc = fields.Many2one("benhvien.thuoc", string="Thuốc", required=True)

    supplier_id = fields.Many2one('res.partner', string="Nhà cung cấp", domain=[('supplier_rank', '>', 0)])

    phieu_nhap = fields.Many2one("benhvien.phieu_nhap", string="Phiếu Nhập", required=True)


    _sql_constraints = [
        ('unique_ma_lo_hang', 'unique(ma_lo_hang)', 'Mã lô hàng phải là duy nhất!')
    ]
