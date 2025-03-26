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

    # hoa_don = fields.One2many("benhvien.hoa_don","id","Hóa đơn")
    #
    # sudunggiuongbenh = fields.One2many("benhvien.sudunggiuongbenh","benhan_id","Sử dụng giường bệnh")
    #
    # xetnghiem = fields.One2many("benhvien.xetnghiem","ma_benh_an","Xét nghiệm")
    #
    # hinhanh = fields.One2many("benhvien.hinhanh","ma_benh_an","Hình ảnh")

    @api.model_create_multi
    def create(self, vals_list):
        print("hello world")
        for vals in vals_list:
            # Tạo mã hồ sơ bệnh án nếu chưa có
            if vals.get('ma_ho_so', "New") == "New":
                vals['ma_ho_so'] = self.env['ir.sequence'].next_by_code('benhvien.hosobenhan') or "HS-000"

        records = super().create(vals_list)

        # for record in records:
        #     # Tạo hóa đơn trống khi tạo hồ sơ bệnh án
        #     self.env['benhvien.hoa_don'].create({
        #         'benh_an': record.id,
        #         'tong_tien': 0.0,
        #         'so_tien_da_thanh_toan': 0.0,
        #         'con_no': 0.0,
        #         'so_tien_benh_nhan': 0.0,
        #         'so_tien_BHYT': 0.0,
        #         'trang_thai': 'draft',
        #         'currency_id': self.env.company.currency_id.id
        #     })

        return records

    # @api.constrains('hoa_don')
    # def _check_hoa_don(self):
    #     for record in self:
    #         if len(record.hoa_don) > 1:
    #             raise exceptions.ValidationError("Chỉ được phép có một hóa đơn cho mỗi hồ sơ bệnh án!")