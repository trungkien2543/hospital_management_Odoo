from odoo import models, fields,api
from odoo.exceptions import UserError


class ChiTietDonThuoc(models.Model):
    _name = "benhvien.chi_tiet_don_thuoc"
    _description = "Chi tiết đơn thuốc"

    ma_don_thuoc = fields.Many2one("benhvien.don_thuoc", string="Mã đơn thuốc", required=True, ondelete="cascade")
    ma_thuoc = fields.Many2one("benhvien.thuoc", string="Mã thuốc", required=True, ondelete="cascade")
    so_luong = fields.Integer(string="Số lượng",required=True)
    chi_dan = fields.Text(string="Chỉ dẫn",required=True)
    don_vi_tinh = fields.Many2one(
        "benhvien.don_vi_tinh",
        string="Đơn vị tính",
        related="ma_thuoc.don_vi_tinh",
        store=True,
        readonly=True
    )

    # @api.constrains là một decorator trong Odoo dùng để xác thực dữ liệu trên các trường cụ thể trước khi lưu vào database.
    @api.constrains('ma_thuoc', 'ma_don_thuoc')
    def _check_drug_interactions(self):
        for record in self:
            # Lấy tất cả thuốc đã có trong đơn thuốc hiện tại
            other_drugs = self.env['benhvien.chi_tiet_don_thuoc'].search([
                ('ma_don_thuoc', '=', record.ma_don_thuoc.id),
                ('id', '!=', record.id)  # Loại bỏ bản ghi hiện tại (tránh kiểm tra chính nó)
            ])

            for other in other_drugs:
                # Kiểm tra xem cặp thuốc này có trong bảng Tương tác thuốc không
                interaction = self.env['benhvien.tuong_tac_thuoc'].search([
                    '|',
                    '&', ('ma_thuoc_1', '=', record.ma_thuoc.id), ('ma_thuoc_2', '=', other.ma_thuoc.id),
                    '&', ('ma_thuoc_1', '=', other.ma_thuoc.id), ('ma_thuoc_2', '=', record.ma_thuoc.id),
                    ('muc_do_nguy_hiem', '=', 'Nguy hiểm')
                ], limit=1)

                if interaction:
                    raise UserError(
                        f"⚠️ Thuốc '{record.ma_thuoc.ten_thuoc}' có tương tác nguy hiểm với '{other.ma_thuoc.ten_thuoc}'! "
                        f"({interaction.mo_ta})"
                    )