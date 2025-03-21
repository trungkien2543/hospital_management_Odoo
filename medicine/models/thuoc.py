from odoo import fields, models, api

class Thuoc(models.Model):
    _name = "benhvien.thuoc"
    _description = "Medicine Manage"
    _rec_name = "ten_thuoc"

    ma_thuoc = fields.Char(string="Mã thuốc", required=True, copy=False, readonly=True, default="MED0001")
    ten_thuoc = fields.Text(string="Tên thuốc", required=True)  # TEXT NOT NULL
    nhom_thuoc = fields.Text(string="Nhóm thuốc", required=True)  # TEXT NOT NULL
    dang_bao_che = fields.Text(string="Dạng bào chế", required=True)  # TEXT NOT NULL
    quy_tac_dong_goi = fields.Text(string="Quy tắc đóng gói", required=True)  # TEXT NOT NULL
    lieu_dung = fields.Text(string="Liều dùng", required=True)  # TEXT NOT NULL
    chong_chi_dinh = fields.Text(string="Chống chỉ định", required=True)  # TEXT NOT NULL
    tac_dung_phu = fields.Text(string="Tác dụng phụ", required=True)  # TEXT NOT NULL
    don_vi_tinh = fields.Many2one("benhvien.don_vi_tinh",string="Đơn vị tính", required=True)  # INTEGER NOT NULL
    ghi_chu = fields.Text(string="Ghi chú", required=True)  # TEXT NOT NULL
    so_luong_ton_kho = fields.Integer(string="Số lượng tồn kho", required=True, default=0)  # INTEGER NOT NULL
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection([
        ('available', 'Còn hàng'),
        ('low_stock', 'Sắp hết hàng'),
        ('out_of_stock', 'Hết hàng')
    ], string="Trạng thái", required=True, copy=False, default='available')

    tuongtacthuoc_ids = fields.One2many("benhvien.tuong_tac_thuoc","ma_thuoc_1",string="Tương tác thuốc")

    lohang_ids = fields.One2many("benhvien.lo_hang","thuoc",string="Thông tin lô hàng")

    _sql_constraints = [
        ('unique_ma_thuoc', 'unique(ma_thuoc)', 'Mã thuốc phải là duy nhất!'),
        ('unique_ten_thuoc', 'unique(ten_thuoc)', 'Tên thuốc không được trùng nhau!'),
        ('check_so_luong_ton_kho', 'CHECK(so_luong_ton_kho >= 0)', 'Số lượng tồn kho không thể âm!')
    ]

    @api.model
    def create(self, vals):
        """
        Ghi đè phương thức create để tự động tạo mã thuốc (ma_thuoc) khi thêm mới bản ghi.
        """

        # Kiểm tra nếu 'ma_thuoc' không có trong 'vals' hoặc giá trị là 'New'
        if vals.get('ma_thuoc', 'MED0001') == 'MED0001':
            # Lấy số tiếp theo từ sequence 'benhvien.medicine' để tạo mã thuốc
            vals['ma_thuoc'] = self.env['ir.sequence'].next_by_code('benhvien.thuoc') or 'MED0001'

        # Gọi phương thức create gốc để tạo bản ghi trong database
        return super(Thuoc, self).create(vals)