from odoo import models, fields, api
from datetime import datetime

class LoHang(models.Model):
    _name = "benhvien.lo_hang"
    _description = "Lô Hàng Dược Phẩm"
    _rec_name = "ma_lo_hang"

    ma_lo_hang = fields.Char(string="Mã Lô Hàng", required=True, copy=False, readonly=True, default="New")
    han_su_dung = fields.Date(string="Hạn Sử Dụng", required=True)
    ngay_nhap = fields.Date(string="Ngày Nhập", required=True, default=fields.Date.today)
    gia_nhap = fields.Monetary(string="Giá Nhập", required=True,currency_field="currency_id")
    so_luong_ton_kho = fields.Integer(string="Số lượng", required=True, default=0)
    trang_thai = fields.Selection([
        ('su_dung', 'Sử dụng'),
        ('khong_su_dung', 'Không Sử Dụng')
    ], string="Trạng Thái", default="su_dung")
    tinh_trang_chat_luong = fields.Text(string="Tình Trạng Chất Lượng")

    thuoc = fields.Many2one("benhvien.thuoc", string="Thuốc", required=True)
    phieu_nhap = fields.Many2one("benhvien.phieu_nhap", string="Phiếu Nhập", required=True)

    currency_id = fields.Many2one(
        "res.currency",
        string="Loại tiền tệ",
        default=lambda self: self.env.company.currency_id,
        readonly=True,
        store=False  # Không lưu vào database
    )

    _sql_constraints = [
        ('unique_ma_lo_hang', 'unique(ma_lo_hang)', 'Mã lô hàng phải là duy nhất!')
    ]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("ma_lo_hang", "New") == "New":
                sequence = self.env["ir.sequence"].next_by_code("benhvien.lo_hang")
                ngay_nhap = vals.get("ngay_nhap", fields.Date.today())
                ngay_nhap_str = datetime.strptime(str(ngay_nhap), "%Y-%m-%d").strftime("%Y%m%d")

                # Lấy mã thuốc
                thuoc_id = vals.get("thuoc")
                thuoc = self.env["benhvien.thuoc"].browse(thuoc_id)
                ma_thuoc = thuoc.ma_thuoc if thuoc and thuoc.ma_thuoc else "UNK"

                # Sinh mã lô hàng theo format
                vals["ma_lo_hang"] = f"LOH-{ngay_nhap_str}-{ma_thuoc}-{sequence}"

        # Tạo bản ghi lô hàng
        records = super(LoHang, self).create(vals_list)

        # Cập nhật số lượng thuốc tồn kho
        for record in records:
            if record.thuoc:
                record.thuoc.sudo().so_luong_ton_kho += record.so_luong_ton_kho  # Cộng dồn số lượng thuốc

        return records

