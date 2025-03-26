{
    'name': 'Nhân sự & Tiền lương',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Tran khanh duy',
    'category': 'Healthcare',
    'summary': 'Quản lý phụ cấp và tiền lương nhân sự',
    'description': 'Module quản lý phụ cấp và tiền lương cho nhân sự.',
    'data': [
        'security/ir.model.access.csv',
        # 'data/allowance_data.xml',
        # 'data/employee_data.xml',
        'views/salary_views.xml',
        'views/allowance_views.xml',
        'views/allowance_detail_views.xml',
        'views/my_employee_view.xml',  # View cho nhân sự
        'views/my_experience_view.xml',  # View cho kinh nghiệm
        'views/my_skill_view.xml',  # View cho kỹ năng
    ],
    'installable': True,
    'application': True,
}
