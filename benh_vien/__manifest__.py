{
    'name': "Quản lý bệnh viện",
    'version': '1.1',
    'depends': ['base'],
    'author': "Nhóm 3_DACN",
    'category': 'Healthcare',
    'summary': "A module for managing hospital operations, patients, and doctors",
    'description': """
        This module helps in managing hospital records, including patients, doctors, and appointments.
    """,
    'data': [

        'views/nhansu_action.xml',

        # Views cho khoa
        'views/khoa/khoa_action.xml',
        'views/khoa/khoa_menu.xml',
        'views/khoa/khoa.xml',
        'views/khoa/phongkham.xml',
        'views/khoa/loaiphongkham.xml',
        'views/khoa/sudungphongkham.xml',
        'views/khoa/phongbenh.xml',
        'views/khoa/giuongbenh.xml',
        'views/khoa/sudunggiuongbenh.xml',


        'views/xetnghiem_chandoan/chandoan_action.xml',
        'views/xetnghiem_chandoan/chandoan_menu.xml',
        'views/xetnghiem_chandoan/xetnghiem.xml',
        'views/xetnghiem_chandoan/hinhanh.xml',
        'views/xetnghiem_chandoan/loaichandoan.xml',
        # 'data/loaixetnghiem_data.csv',
        'data/xetnghiem_chandoan/sequence.xml',


        'views/salary_views.xml',
        'views/allowance_views.xml',
        'views/allowance_detail_views.xml',
        'views/my_employee_view.xml',  # View cho nhân sự
        'views/my_experience_view.xml',  # View cho kinh nghiệm
        'views/my_skill_view.xml',  # View cho kỹ năng

        # Views cho thuốc
        'views/thuoc/medicine_action.xml',
        'views/thuoc/medicine_menus.xml',
        'views/thuoc/medicine_views.xml',
        'views/thuoc/don_vi_tinh_views.xml',
        'views/thuoc/tuong_tac_thuoc.xml',
        'views/thuoc/phieu_nhap_views.xml',
        'views/thuoc/phieu_xuat_views.xml',
        'views/thuoc/don_thuoc_views.xml',


        'security/ir.model.access.csv',

        'data/khoa/khoa_sequence.xml',
        'data/thuoc/sequence.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
