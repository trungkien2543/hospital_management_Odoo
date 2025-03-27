from odoo import api, fields, models, exceptions



class HoSoBenhAn(models.Model):
    _name = 'benhvien.hosobenhan'
    _description = 'Quản lý hồ sơ bệnh án'

    ma_ho_so = fields.Char(string="Mã hồ sơ bệnh án", readonly=True, copy=False, default="New")
    ma_benh_nhan = fields.Many2one('benhvien.benhnhan', string="Mã bệnh nhân", required=True)
    ma_bac_si = fields.Many2one('benhvien.nhansu', string="Bác sĩ phụ trách", required=True)
    chuan_doan = fields.Text(string="Chuẩn đoán bệnh")
    trieu_chung = fields.Text(string="Triệu chứng")
    don_thuoc = fields.One2many('benhvien.don_thuoc','ma_don_thuoc',string="Đơn thuốc liên quan")
    ngay_kham = fields.Date(string="Ngày khám", required=True, default=fields.Date.context_today)
    ke_hoach_dieu_tri = fields.Text(string="Kế hoạch điều trị")
    hen_ngay_tai_kham = fields.Date(string="Hẹn ngày tái khám")

    hoa_don_ids = fields.Many2one(
        'benhvien.hoa_don',
        string="Hóa đơn",
        ondelete="cascade",
        readonly=True
    )


    sudunggiuongbenh = fields.One2many("benhvien.sudunggiuongbenh","benhan_id","Sử dụng giường bệnh")

    xetnghiem = fields.One2many("benhvien.xetnghiem","ma_benh_an","Xét nghiệm")

    hinhanh = fields.One2many("benhvien.hinhanh","ma_benh_an","Hình ảnh")



    _sql_constraints = [
        ('unique_hoa_don', 'UNIQUE(hoa_don_id)', 'Mỗi hồ sơ bệnh án chỉ có thể có một hóa đơn!')
    ]

    @api.model_create_multi
    def create(self, vals_list):
        print("hello world")
        for vals in vals_list:
            # Tạo mã hồ sơ bệnh án nếu chưa có
            if vals.get('ma_ho_so', "New") == "New":
                vals['ma_ho_so'] = self.env['ir.sequence'].next_by_code('benhvien.hosobenhan') or "HS-000"

        records = super().create(vals_list)

        for record in records:
            hoa_don = self.env['benhvien.hoa_don'].create({
                'benh_an_id': record.id,
                'ngay_lap': fields.Date.context_today(self),
                'tong_tien': 0.0,
                'con_no': 0.0,
                'so_tien_benh_nhan': 0.0,
                'so_tien_bhyt': 0.0,
                'trang_thai': 'draft',
                'currency_id': self.env.company.currency_id.id,
            })
            record.hoa_don_ids = hoa_don

        return records

    @api.onchange('hoa_don_id')
    def _onchange_hoa_don_id(self):
        """ Khi chọn hóa đơn bên bệnh án, cập nhật bệnh án trong hóa đơn """
        if self.hoa_don_ids:
            self.hoa_don_ids.benh_an_id = self