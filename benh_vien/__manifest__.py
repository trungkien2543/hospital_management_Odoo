{
    'name': "Quản lý bệnh viện",
    'version': '1.1',
    'depends': ['base', 'mail'],
    'author': "Nhóm 3_DACN",
    'category': 'Healthcare',
    'summary': "A module for managing hospital operations, patients, and doctors",
    'description': """
        This module helps in managing hospital records, including patients, doctors, and appointments.
    """,
    'data': [



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

        'views/nhansu/nhansu_action.xml',
        'views/nhansu/nhansu_menu.xml',
        'views/nhansu/salary_views.xml',
        'views/nhansu/allowance_views.xml',
        'views/nhansu/allowance_detail_views.xml',
        'views/nhansu/my_employee_view.xml',  # View cho nhân sự
        'views/nhansu/my_experience_view.xml',  # View cho kinh nghiệm
        'views/nhansu/my_skill_view.xml',  # View cho kỹ năng

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
        'data/thuoc/sequence.xml',
        
        #benhnhan
        'views/benhnhan/benhnhan_view.xml',
        'views/benhnhan/benhnhan_action.xml',
        'views/benhnhan/benhnhan_menu.xml',
        'data/benhnhan/sequence.xml',
        'data/benhnhan/patient_data.xml',

        #lichhenvalichkham
        'data/lichhenvalichkham/sequence.xml',
        'views/lichhenvalichkham/datlichhen_view.xml',
        'views/lichhenvalichkham/datlichhen_action.xml',
        'views/lichhenvalichkham/datlichhen_menu.xml',
        'views/lichhenvalichkham/lichkham_view.xml',
        'views/lichhenvalichkham/lichkham_action.xml',
        'views/lichhenvalichkham/lichkham_menu.xml',
        'data/lichhenvalichkham/email_template.xml',

        #thanh toan
        'views/thanh_toan/thanh_toan_action.xml',
        'views/thanh_toan/thanh_toan_menus.xml',
        'views/thanh_toan/dich_vu_views.xml',
        'views/thanh_toan/hoa_don_views.xml',
        'views/thanh_toan/ma_thanh_toan.xml',


        #tuanthu_quydinh
        'views/tuanthu_quydinh/tuanthu_action.xml',
        'views/tuanthu_quydinh/tuanthu_menu.xml',
        'views/tuanthu_quydinh/chungnhan.xml',
        'views/tuanthu_quydinh/kiemtra.xml',
        'views/tuanthu_quydinh/quydinh.xml',
        'data/tuanthu_quydinh/sequence.xml',

        #quan_ly_dieutri_chamsoc
        'views/dieutri_chamsoc/kehoachdieutri_action.xml',
        'views/dieutri_chamsoc/tientrinh_action.xml',
        'views/dieutri_chamsoc/kehoachdieutri_menu.xml',
        'views/dieutri_chamsoc/kehoachdieutri.xml',
        'views/dieutri_chamsoc/tientrinh_menu.xml',
        'views/dieutri_chamsoc/tientrinh.xml',
        'data/dieutri_chamsoc/sequence_kehoach.xml',

    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
