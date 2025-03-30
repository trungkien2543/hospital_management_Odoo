from odoo import models, fields, api

class HoaDon(models.Model):
    _name = 'benhvien.hoa_don'
    _description = 'Hóa Đơn'

    benh_an_id = fields.Many2one(
        'benhvien.hosobenhan',
        string='Bệnh Án',
        required=True,
        ondelete='cascade'
    )


    paid_amount = fields.Monetary(string='Đã Thu', currency_field='currency_id', default=0.0,readonly=True)
    patient_pay = fields.Monetary(string='Phải Thu', currency_field='currency_id', compute='_compute_patient_pay', store=True)
    remaining_debt = fields.Monetary(string='Còn Nợ', currency_field='currency_id', compute='_compute_remaining_debt', store=True)

    has_bhyt = fields.Boolean(string='Áp Dụng BHYT', compute='_compute_has_bhyt', store=True, readonly=True)

    status = fields.Selection([
        ('pending', 'Chờ Thanh Toán'),
        ('partially_paid', 'Thanh Toán Một Phần'),
        ('paid', 'Đã Thanh Toán')
    ], string='Trạng Thái', compute='_compute_status', store=True)

    created_at = fields.Datetime(string='Ngày Lập Hóa Đơn', default=fields.Datetime.now, readonly=True)

    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.ref('base.VND').id,
        readonly=True
    )

    chi_tiet_hoa_don_ids = fields.One2many("benhvien.chi_tiet_hoa_don", "hoa_don_id", string="Chi tiết hóa đơn")

    phieu_xuat_ids = fields.One2many("benhvien.phieu_xuat","hoa_don",string="Phiếu xuất")

    ma_thanh_toan = fields.One2many("benhvien.ma_thanh_toan","hoa_don_id",string="Mã thanh toán")



    @api.depends('chi_tiet_hoa_don_ids.patient_pay', 'phieu_xuat_ids.tong_phai_thu')
    def _compute_patient_pay(self):
        for record in self:
            record.patient_pay = sum(record.chi_tiet_hoa_don_ids.mapped("patient_pay")) + sum(record.phieu_xuat_ids.mapped("tong_phai_thu"))

    @api.depends('patient_pay', 'paid_amount')
    def _compute_remaining_debt(self):
        for record in self:
            record.remaining_debt = record.patient_pay - record.paid_amount

    @api.depends('benh_an_id.ma_benh_nhan')
    def _compute_has_bhyt(self):
        for record in self:
            patient = record.benh_an_id.ma_benh_nhan
            if patient:
                bhyt_record = self.env['benhvien.bhyt'].search([
                    ('ma_benh_nhan', '=', patient.id),
                    ('ngay_hieu_luc', '<=', fields.Date.today()),
                    ('ngay_het_han', '>=', fields.Date.today())
                ], limit=1)
                record.has_bhyt = bool(bhyt_record)
            else:
                record.has_bhyt = False



    @api.model_create_multi
    def create(self, vals_list):
        records = super(HoaDon, self).create(vals_list)
        for record in records:
            record._create_bhyt_payment()
        return records


    def _create_bhyt_payment(self):
        """Tạo mã thanh toán BHYT sau khi hóa đơn được tạo."""
        if self.has_bhyt and not self.env['benhvien.ma_thanh_toan'].search(
                [('hoa_don_id', '=', self.id), ('phuong_thuc', '=', 'bhyt')]):
            self.env['benhvien.ma_thanh_toan'].create({
                'hoa_don_id': self.id,
                'so_tien': sum(self.chi_tiet_hoa_don_ids.mapped("discount_amount")) + sum( self.phieu_xuat_ids.mapped("tong_mien_giam")),
                'phuong_thuc': 'bhyt',
                'trang_thai': 'pending',
                'is_bhyt':True,
                'ngay_tao': fields.Datetime.now(),
                'mo_ta': 'Thanh toán bảo hiểm y tế',
                'currency_id': self.currency_id.id
            })