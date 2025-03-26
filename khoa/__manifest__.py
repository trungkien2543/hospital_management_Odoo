{
    'name': "Quản lý Khoa và Nhân sự",
    'version': '1.1',
    'depends': ['base'],
    'author': "Your Name",
    'category': 'Healthcare',
    'summary': "A module for managing hospital operations, patients, and doctors",
    'description': """
        This module helps in managing hospital records, including patients, doctors, and appointments.
    """,
    'data': [
        'views/khoa_action.xml',
        'views/nhansu_action.xml',
        'views/khoa_menu.xml',
        'views/khoa.xml',
        'views/phongkham.xml',
        'views/loaiphongkham.xml',
        'views/sudungphongkham.xml',
        'views/phongbenh.xml',
        'views/giuongbenh.xml',
        'views/sudunggiuongbenh.xml',

        'views/salary_views.xml',
        'views/allowance_views.xml',
        'views/allowance_detail_views.xml',
        'views/my_employee_view.xml',  # View cho nhân sự
        'views/my_experience_view.xml',  # View cho kinh nghiệm
        'views/my_skill_view.xml',  # View cho kỹ năng

        'security/ir.model.access.csv',
        'data/khoa_sequence.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
