from odoo import fields, models, api
from odoo.exceptions import ValidationError


class TuongTacThuoc(models.Model):
    _name = "benhvien.tuong_tac_thuoc"
    _description = "Tương tác giữa các thuốc"

    ma_thuoc_1 = fields.Many2one("benhvien.thuoc",string="Thuốc 1", required=True, copy = False)
    ma_thuoc_2 = fields.Many2one("benhvien.thuoc",string="Thuốc 2", required=True, copy = False)
    mo_ta = fields.Text(string="Mô tả", required=True)  # TEXT NOT NULL
    muc_do_nguy_hiem = fields.Selection([
        ('Thấp', 'Thấp'),
        ('Trung bình', 'Trung bình'),
        ('Nguy hiểm', 'Nguy hiểm')
    ], string="Mức độ nguy hiểm", required=True, default="Thấp")

    _sql_constraints = [
        ('unique_drug_pair', 'unique(ma_thuoc_1, ma_thuoc_2)', 'Mỗi cặp thuốc chỉ có thể có một mức độ nguy hiểm!')
    ]

    @api.constrains('ma_thuoc_1', 'ma_thuoc_2')
    def _check_unique_pair(self):
        for record in self:
            if record.ma_thuoc_1 == record.ma_thuoc_2:
                raise ValidationError("Một thuốc không thể tương tác với chính nó!")

            existing_pair = self.env['benhvien.tuong_tac_thuoc'].search([
                '|',
                ('ma_thuoc_1', '=', record.ma_thuoc_1.id), ('ma_thuoc_2', '=', record.ma_thuoc_2.id),
                ('ma_thuoc_1', '=', record.ma_thuoc_2.id), ('ma_thuoc_2', '=', record.ma_thuoc_1.id)
            ])

            if existing_pair:
                raise ValidationError("Tương tác giữa hai thuốc này đã tồn tại trong hệ thống!")