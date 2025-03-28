from odoo import models, fields, api


class PhieuXuatKho(models.Model):
    _name = 'benhvien.phieu_xuat'
    _description = 'Phiếu Xuất Kho'

    ma_phieu_xuat = fields.Char(string="Mã Phiếu Xuất", required=True, copy=False, readonly=True, default="New")
    ngay_xuat = fields.Datetime(string="Ngày Xuất", required=True, default=fields.Datetime.now,readonly=True)
    tong_tien = fields.Monetary(string="Tổng Tiền", compute="_compute_tong_tien", store=True, currency_field="currency_id")
    ghi_chu = fields.Text(string="Ghi Chú")

    currency_id = fields.Many2one(
        "res.currency",
        string="Loại tiền tệ",
        default=lambda self: self.env.company.currency_id,
        readonly=True,
        store=False  # Không lưu vào database
    )

    chi_tiet_xuat = fields.One2many("benhvien.chi_tiet_phieu_xuat", "ma_phieu", string="Chi Tiết Xuất")



    hoa_don = fields.Many2one("benhvien.hoa_don",string="Hóa đơn")



    @api.depends('chi_tiet_xuat.thanh_tien')
    def _compute_tong_tien(self):
        """Tính tổng tiền dựa vào thành tiền của các chi tiết phiếu xuất."""
        for record in self:
            record.tong_tien = sum(record.chi_tiet_xuat.mapped("thanh_tien"))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            print("DEBUG: Giá trị đầu vào", vals)  # In ra để kiểm tra
            if not vals.get('ma_phieu_xuat') or vals['ma_phieu_xuat'] == 'PX0001':
                vals['ma_phieu_xuat'] = self.env['ir.sequence'].next_by_code('benhvien.phieu_xuat') or 'PX0001'

        return super(PhieuXuatKho, self).create(vals_list)
