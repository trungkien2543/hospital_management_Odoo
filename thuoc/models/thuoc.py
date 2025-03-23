from odoo import fields, models, api
from odoo.api import readonly


class Thuoc(models.Model):
    _name = "benhvien.thuoc"
    _description = "Medicine Manage"
    _rec_name = "ten_thuoc"

    ma_thuoc = fields.Char(string="Mã thuốc", required=True, copy=False, readonly=True,default="MED0001")
    ten_thuoc = fields.Text(string="Tên thuốc", required=True)  # TEXT NOT NULL
    nhom_thuoc = fields.Text(string="Nhóm thuốc", required=True)  # TEXT NOT NULL
    dang_bao_che = fields.Text(string="Dạng bào chế", required=True)  # TEXT NOT NULL
    quy_tac_dong_goi = fields.Text(string="Quy tắc đóng gói", required=True)  # TEXT NOT NULL
    lieu_dung = fields.Text(string="Liều dùng", required=True)  # TEXT NOT NULL
    chong_chi_dinh = fields.Text(string="Chống chỉ định", required=True)  # TEXT NOT NULL
    tac_dung_phu = fields.Text(string="Tác dụng phụ", required=True)  # TEXT NOT NULL
    don_vi_tinh = fields.Many2one("benhvien.don_vi_tinh",string="Đơn vị tính", required=True)  # INTEGER NOT NULL
    ghi_chu = fields.Text(string="Ghi chú", required=True)  # TEXT NOT NULL
    gia_ban = fields.Float(string="Giá Bán", compute="_compute_gia_ban", store=True)
    so_luong_ton_kho = fields.Integer(string="Số lượng tồn kho", required=True,readonly=True, default=0)  # INTEGER NOT NULL
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection([
        ('available', 'Còn hàng'),
        ('low_stock', 'Sắp hết hàng'),
        ('out_of_stock', 'Hết hàng')
    ], string="Trạng thái", required=True, copy=False, readonly=True,default='out_of_stock',compute="_compute_state")

    tuongtacthuoc_ids = fields.One2many("benhvien.tuong_tac_thuoc","ma_thuoc_1",string="Tương tác thuốc")

    lohang_ids = fields.One2many("benhvien.lo_hang","thuoc",string="Thông tin lô hàng")

    _sql_constraints = [
        ('unique_ma_thuoc', 'unique(ma_thuoc)', 'Mã thuốc phải là duy nhất!'),
        ('unique_ten_thuoc', 'unique(ten_thuoc)', 'Tên thuốc không được trùng nhau!'),
        ('check_so_luong_ton_kho', 'CHECK(so_luong_ton_kho >= 0)', 'Số lượng tồn kho không thể âm!')
    ]

    @api.model_create_multi
    def create(self, vals_list):
        """
        Ghi đè phương thức create để tự động tạo mã thuốc (ma_thuoc) khi thêm mới bản ghi. a
        """

        for vals in vals_list:
            # Kiểm tra nếu 'ma_thuoc' không có trong 'vals' hoặc giá trị là 'MED0001'
            if 'ma_thuoc' not in vals or vals['ma_thuoc'] == 'MED0001':
                # Lấy số tiếp theo từ sequence 'benhvien.thuoc' để tạo mã thuốc
                vals['ma_thuoc'] = self.env['ir.sequence'].next_by_code('benhvien.thuoc') or 'MED0001'

        # Gọi phương thức create gốc để tạo bản ghi trong database
        return super(Thuoc, self).create(vals_list)

    @api.depends("so_luong_ton_kho")
    def _compute_state(self):
        """
        Hàm tính toán trạng thái thuốc dựa trên số lượng tồn kho.
        """
        for record in self:
            if record.so_luong_ton_kho <= 0:
                record.state = 'out_of_stock'  # Hết hàng
            elif record.so_luong_ton_kho < 10:
                record.state = 'low_stock'  # Sắp hết hàng
            else:
                record.state = 'available'  # Còn hàng

    @api.depends("lohang_ids.gia_nhap")
    def _compute_gia_ban(self):
        """Cập nhật giá bán dựa trên giá nhập cao nhất từ các lô hàng."""
        for record in self:
            if record.lohang_ids:
                record.gia_ban = max(record.lohang_ids.mapped("gia_nhap"))
            else:
                record.gia_ban = 0.0  # Nếu không có lô hàng, giá bán mặc định là 0