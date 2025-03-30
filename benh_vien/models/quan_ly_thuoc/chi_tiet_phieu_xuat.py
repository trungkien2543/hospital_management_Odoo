from odoo import models, fields, api
from odoo.exceptions import UserError


class ChiTietPhieuXuat(models.Model):
    _name = "benhvien.chi_tiet_phieu_xuat"
    _description = "Chi Tiết Phiếu Xuất"

    ma_phieu = fields.Many2one("benhvien.phieu_xuat", string="Phiếu Xuất", required=True, ondelete="cascade")
    thuoc = fields.Many2one("benhvien.thuoc", string="Thuốc", required=True)
    so_luong = fields.Integer(string="Số Lượng", required=True, default=1)

    don_gia_thuoc = fields.Monetary(string="Đơn Giá Thuốc", compute="_compute_don_gia_thuoc", store=True, currency_field="currency_id")
    gia_chua_giam = fields.Monetary(string="Giá Thuốc Chưa Giảm", compute="_compute_gia_chua_giam", store=True, currency_field="currency_id")
    mien_giam = fields.Monetary(string="Miễn Giảm", default=0.0, currency_field="currency_id", compute="_compute_mien_giam",store=True)
    phai_thu = fields.Monetary(string="Phải Thu", compute="_compute_phai_thu", store=True, currency_field="currency_id")

    ma_lo_hang = fields.Many2one("benhvien.lo_hang", string="Lô Hàng", readonly=True)

    currency_id = fields.Many2one(
        "res.currency",
        string="Loại tiền tệ",
        default=lambda self: self.env.company.currency_id,
        readonly=True
    )

    @api.depends("thuoc")
    def _compute_don_gia_thuoc(self):
        """Lấy đơn giá của thuốc từ model `benhvien.thuoc`."""
        for record in self:
            record.don_gia_thuoc = record.thuoc.gia_ban if record.thuoc else 0.0

    @api.depends("so_luong", "don_gia_thuoc")
    def _compute_gia_chua_giam(self):
        """Tính tổng tiền trước khi giảm giá."""
        for record in self:
            record.gia_chua_giam = record.so_luong * record.don_gia_thuoc

    @api.depends("gia_chua_giam", "mien_giam")
    def _compute_phai_thu(self):
        """Tính số tiền phải thu = Giá thuốc chưa giảm - Miễn giảm."""
        for record in self:
            record.phai_thu = max(0, record.gia_chua_giam - record.mien_giam)



    @api.depends("gia_chua_giam", "ma_phieu.hoa_don.has_bhyt", "thuoc.bhyt")
    def _compute_mien_giam(self):
        """Tính số tiền miễn giảm dựa trên BHYT."""
        for record in self:
            record.mien_giam = 0.0  # Mặc định không miễn giảm

            if record.ma_phieu and record.ma_phieu.hoa_don:
                hoa_don = record.ma_phieu.hoa_don

                if hoa_don.has_bhyt and record.thuoc.bhyt:
                    # Nếu có BHYT và thuốc được BHYT chi trả, miễn giảm theo tỷ lệ

                    record.mien_giam = record.gia_chua_giam * 0.8



    @api.model_create_multi
    def create(self, vals_list):
        """Tự động chọn lô hàng theo hạn sử dụng khi xuất kho."""
        new_records = []
        for vals in vals_list:
            thuoc_id = vals.get("thuoc")
            so_luong_can_xuat = vals.get("so_luong", 0)

            if not thuoc_id or so_luong_can_xuat <= 0:
                raise UserError("Thuốc và số lượng phải hợp lệ!")

            # Lấy các lô hàng của thuốc theo hạn sử dụng (FIFO)
            lo_hangs = self.env["benhvien.lo_hang"].search([
                ("thuoc", "=", thuoc_id),
                ("so_luong_ton_kho", ">", 0),
                ("trang_thai", "=", "su_dung")
            ], order="han_su_dung ASC")

            if not lo_hangs:
                raise UserError(f"Không có lô hàng nào khả dụng cho thuốc ID {thuoc_id}!")

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
                    "don_gia_thuoc": lo_hang.thuoc.gia_ban
                })
                record = super(ChiTietPhieuXuat, self).create(new_vals)
                new_records.append(record)

                # Cập nhật số lượng tồn kho của lô hàng
                lo_hang.sudo().write({"so_luong_ton_kho": lo_hang.so_luong_ton_kho - so_luong_tru})

            if so_luong_con_lai > 0:
                ten_thuoc = self.env['benhvien.thuoc'].browse(thuoc_id).ten_thuoc
                raise UserError(f"Số lượng thuốc {ten_thuoc} trong kho không đủ để thực hiện xuất. Vui lòng kiểm tra lại số lượng hoặc liên hệ quản trị viên.")

        return new_records
