{
    'name': "Quan ly khoa va phong kham",
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
        'views/khoa_menu.xml',
        'views/phongkham.xml',
        'views/sudungphongkham.xml',
        'views/phongbenh_information.xml',
        'views/giuongbenh_information.xml',
        'views/sudunggiuongbenh_information.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
