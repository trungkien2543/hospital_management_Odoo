from odoo import models, fields

class MedicalPerformanceReview(models.Model):
    _name = 'medical.performance.review'
    _description = 'Đánh giá hiệu suất nhân viên y tế'

    employee_id = fields.Many2one('benhvien.nhansu', string='Nhân viên được đánh giá', required=True)
    review_date = fields.Date(string='Ngày đánh giá', required=True)
    reviewer_id = fields.Many2one('benhvien.nhansu', string='Người đánh giá', required=True)
    score = fields.Integer(string='Điểm đánh giá', help='Thang điểm từ 1 đến 10')
    comments = fields.Text(string='Nhận xét')
