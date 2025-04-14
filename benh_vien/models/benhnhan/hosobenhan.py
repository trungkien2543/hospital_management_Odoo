from odoo import api, fields, models, exceptions


class HoSoBenhAn(models.Model):
    _name = 'benhvien.hosobenhan'
    _description = 'Quản lý hồ sơ bệnh án'
    _rec_name = "ma_ho_so"

    ma_ho_so = fields.Char(string="Mã hồ sơ bệnh án", readonly=True, copy=False, default="New")
    ma_benh_nhan = fields.Many2one('benhvien.benhnhan', string="Mã bệnh nhân", required=True)
    ma_bac_si = fields.Many2one('benhvien.nhansu', string="Bác sĩ phụ trách", required=True)
    chuan_doan = fields.Text(string="Chuẩn đoán bệnh")
    trieu_chung = fields.Text(string="Triệu chứng")
    don_thuoc = fields.One2many('benhvien.don_thuoc', 'ho_so_benh', string="Đơn thuốc liên quan")
    ngay_kham = fields.Date(string="Ngày khám", required=True, default=fields.Date.context_today)
    ke_hoach_dieu_tri = fields.One2many('benhvien.kehoachdieutri', 'ma_benh_an', string="Danh sách kế hoạch điều trị")




    hoa_don_ids = fields.One2many(
        'benhvien.hoa_don', 'benh_an_id', string="Hóa đơn liên quan"
    )

    sudunggiuongbenh = fields.One2many("benhvien.sudunggiuongbenh", "benhan_id", string="Sử dụng giường bệnh")
    xetnghiem = fields.One2many("benhvien.xetnghiem", "ma_benh_an", string="Xét nghiệm")
    hinhanh = fields.One2many("benhvien.hinhanh", "ma_benh_an", string="Hình ảnh")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('ma_ho_so', "New") == "New":
                vals['ma_ho_so'] = self.env['ir.sequence'].next_by_code('benhvien.hosobenhan') or "HS-000"

        records = super().create(vals_list)


        return records