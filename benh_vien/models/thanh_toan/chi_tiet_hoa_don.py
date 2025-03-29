from datetime import date
from email.policy import default

from odoo import models, fields, api
from odoo.exceptions import UserError


class ChiTietHoaDon(models.Model):
    _name = 'benhvien.chi_tiet_hoa_don'
    _description = 'Chi Tiết Hóa Đơn'

    hoa_don_id = fields.Many2one('benhvien.hoa_don', string='Hóa Đơn',readonly=True)
    dich_vu = fields.Many2one('benhvien.dich_vu', string='Dịch Vụ',required =True)
    so_luong = fields.Integer(string='Số Lượng',required =True,default=1)
    thanh_tien = fields.Monetary(string='Thành Tiền', currency_field='currency_id',readonly=True,compute = '_compute_thanh_tien',store=True)
    don_gia = fields.Monetary(string='Đơn giá', currency_field='currency_id', compute = '_compute_don_gia',store=True,readonly=True)
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.ref('base.VND').id,
        readonly=True
    )


    gia_bhyt = fields.Monetary(string='Giá sau BHYT', currency_field='currency_id',readonly=True,compute = '_compute_gia_bhyt',store=True)

    ghi_chu = fields.Selection(
        [
            ('ap_dung_bhyt', 'Áp dụng BHYT'),
            ('khong_co_bhyt', 'Không có BHYT'),
            ('bhyt_het_han', 'BHYT hết hạn'),
            ('dich_vu_khong_bhyt', 'Dịch vụ không áp dụng BHYT')
        ],
        string="Ghi chú",
        required=True,
        compute="_compute_gia_bhyt",
        default="khong_co_bhyt",
        readonly=True,
        store=True
    )


    @api.depends("dich_vu")
    def _compute_don_gia(self):
        """Lấy giá dịch vụ."""
        for record in self:
            record.don_gia = record.dich_vu.don_gia if record.dich_vu else 0.0


    @api.depends("so_luong", "don_gia")
    def _compute_thanh_tien(self):
        """Tính tổng tiền = số lượng * đơn giá."""
        for record in self:
            record.thanh_tien = record.so_luong * record.don_gia if record.so_luong and record.don_gia else 0.0


    @api.depends("hoa_don_id", "dich_vu", "so_luong")
    def _compute_gia_bhyt(self):
        """Kiểm tra bảo hiểm của bệnh nhân và cập nhật giá sau BHYT (chỉ khi thêm mới)."""
        today = date.today()
        discount_rate = 0.5  # Giảm 50% nếu áp dụng BHYT


        for record in self:

            print(f"Before Compute: {record.ghi_chu}, {record.gia_bhyt}")


            if not record.dich_vu.bhyt:
                record.ghi_chu = 'dich_vu_khong_bhyt'
                record.gia_bhyt = record.thanh_tien
                continue


            patient = record.hoa_don_id.benh_an_id.ma_benh_nhan
            if not patient:
                record.gia_bhyt = record.thanh_tien
                record.ghi_chu = 'khong_co_bhyt'
                continue


            bhyt_record = self.env['benhvien.bhyt'].search([
                ('ma_benh_nhan', '=', patient.id)
            ], limit=1, order="ngay_het_han DESC")


            if bhyt_record:
                if bhyt_record.ngay_het_han < today:
                    record.ghi_chu = 'bhyt_het_han'
                    record.gia_bhyt = record.thanh_tien
                else:
                    record.ghi_chu = 'ap_dung_bhyt'
                    record.gia_bhyt = record.thanh_tien * discount_rate
            else:
                record.ghi_chu = 'khong_co_bhyt'
                record.gia_bhyt = record.thanh_tien

            print(f"After Compute: {record.ghi_chu}, {record.gia_bhyt}")



    def write(self, vals):
        """Không cho phép chỉnh sửa bản ghi sau khi đã tạo"""
        if self.ids:  # Nếu bản ghi đã có ID, tức là đã lưu vào database
            raise UserError("Bạn không thể chỉnh sửa dịch vụ sau khi đã thêm.")
        return super(ChiTietHoaDon, self).write(vals)
