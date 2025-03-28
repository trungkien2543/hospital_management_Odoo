from odoo import models, fields, api
from odoo.exceptions import UserError


class BHYT(models.Model):
    _name = 'benhvien.bhyt'  # Định danh model
    _description = 'Bảo Hiểm Y Tế'

    ma_bhyt = fields.Char(string='Mã BHYT', required=True)
    noi_dang_ky = fields.Many2one(
        'res.partner',
        string='Nơi Đăng Ký',
        domain=[('category_id.name', '=', 'Bảo Hiểm Y Tế')],
        required=True
    )

    ngay_hieu_luc = fields.Date(string='Ngày Hiệu Lực', required=True)

    ngay_het_han = fields.Date(string='Ngày Hết Hạn', required=True)

    ma_benh_nhan = fields.Many2one('benhvien.benhnhan', string='Bệnh nhân', required=True, ondelete='cascade')

    _sql_constraints = [
        ('unique_ma_bhyt', 'UNIQUE(ma_bhyt)', 'Mã bảo hiểm y tế là duy nhất!')
    ]

    @api.constrains('ngay_hieu_luc', 'ngay_het_han')
    def _check_dates(self):
        for record in self:
            if record.ngay_het_han and record.ngay_hieu_luc:
                if record.ngay_het_han <= record.ngay_hieu_luc:
                    raise UserError("Ngày hết hạn phải lớn hơn ngày hiệu lực!")