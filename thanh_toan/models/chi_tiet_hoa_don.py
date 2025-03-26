from odoo import models, fields,api
class ChiTietHoaDon(models.Model):
    _name = "benhvien.chi_tiet_hoa_don"
    _description = "Chi tiết hóa đơn"

    ma_hoa_don = fields.Many2one("benhvien.hoa_don", string="Mã hóa đơn", required=True, ondelete="cascade")
    ma_dich_vu = fields.Many2one("benhvien.dich_vu", string="Mã dịch vụ", required=True)
    so_luong = fields.Integer(string="Số lượng", required=True, default=1)
    thanh_tien = fields.Monetary(string="Thành tiền", currency_field="currency_id", compute="_compute_thanh_tien", store=True)
    currency_id = fields.Many2one("res.currency", string="Loại tiền tệ")

    @api.depends('so_luong', 'ma_dich_vu')
    def _compute_thanh_tien(self):
        for record in self:
            record.thanh_tien = (record.so_luong or 0) * (record.ma_dich_vu.don_gia or 0)
