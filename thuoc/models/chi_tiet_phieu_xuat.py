from odoo import models, fields, api
from odoo.exceptions import UserError


class ChiTietPhieuXuat(models.Model):
    _name = "benhvien.chi_tiet_phieu_xuat"
    _description = "Chi Tiết Phiếu Xuất"

    ma_phieu = fields.Many2one("benhvien.phieu_xuat", string="Phiếu Xuất", required=True, ondelete="cascade")
    thuoc = fields.Many2one("benhvien.thuoc", string="Thuốc", required=True)
    so_luong = fields.Integer(string="Số Lượng", required=True, default=1)
    don_gia = fields.Float(string="Đơn Giá", compute="_compute_don_gia", store=True)
    thanh_tien = fields.Float(string="Thành Tiền", compute="_compute_thanh_tien", store=True)
    ma_lo_hang = fields.Many2one("benhvien.lo_hang", string="Lô Hàng", readonly=True)

    @api.depends("thuoc")
    def _compute_don_gia(self):
        """Lấy giá bán từ thuốc."""
        for record in self:
            record.don_gia = record.thuoc.gia_ban if record.thuoc else 0.0

    @api.depends("so_luong", "don_gia")
    def _compute_thanh_tien(self):
        """Tính tổng tiền = số lượng * đơn giá."""
        for record in self:
            record.thanh_tien = record.so_luong * record.don_gia if record.so_luong and record.don_gia else 0.0

    @api.model_create_multi
    def create(self, vals_list):
        """Tự động chọn lô hàng theo hạn sử dụng khi xuất kho."""
        new_records = []
        for vals in vals_list:
            thuoc_id = vals.get("thuoc")
            so_luong_can_xuat = vals.get("so_luong", 0)

            if not thuoc_id or so_luong_can_xuat <= 0:
                raise ValueError("Thuốc và số lượng phải hợp lệ!")

            # Lấy các lô hàng của thuốc theo hạn sử dụng (FIFO)
            lo_hangs = self.env["benhvien.lo_hang"].search([
                ("thuoc", "=", thuoc_id),
                ("so_luong_ton_kho", ">", 0),
                ("trang_thai", "=", "su_dung")
            ], order="han_su_dung ASC")

            if not lo_hangs:
                raise ValueError(f"Không có lô hàng nào khả dụng cho thuốc ID {thuoc_id}!")

            # Duyệt từng lô để trừ số lượng (FIFO)
            so_luong_con_lai = so_luong_can_xuat
            for lo_hang in lo_hangs:
                if so_luong_con_lai <= 0:
                    break

                so_luong_tru = min(lo_hang.so_luong_ton_kho, so_luong_con_lai)
                so_luong_con_lai -= so_luong_tru

                # Tạo chi tiết phiếu xuất cho lô hàng này
                new_vals = vals.copy()
                new_vals.update({
                    "ma_lo_hang": lo_hang.id,
                    "so_luong": so_luong_tru,
                    "don_gia": lo_hang.thuoc.gia_ban
                })
                record = super(ChiTietPhieuXuat, self).create(new_vals)
                new_records.append(record)

                # Cập nhật số lượng tồn kho của lô hàng
                lo_hang.sudo().write({"so_luong_ton_kho": lo_hang.so_luong_ton_kho - so_luong_tru})

            if so_luong_con_lai > 0:
                ten_thuoc = self.env['benhvien.thuoc'].browse(thuoc_id).ten_thuoc
                raise UserError(f"Số lượng thuốc {ten_thuoc} trong kho không đủ để thực hiện xuất. Vui lòng kiểm tra lại số lượng hoặc liên hệ quản trị viên.")

        return new_records
