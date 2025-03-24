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
        'views/khoa.xml',
        'views/phongkham.xml',
        'views/loaiphongkham.xml',
        'views/sudungphongkham.xml',
        'views/phongbenh.xml',
        'views/giuongbenh.xml',
        'views/sudunggiuongbenh.xml',
        'security/ir.model.access.csv',
        'data/khoa_sequence.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
