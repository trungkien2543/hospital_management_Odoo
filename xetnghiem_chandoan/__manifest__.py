{
    'name': "Quan ly xet nghiem va chan doan",
    'version': '1.1',
    'depends': ['base'],
    'author': "Your Name",
    'category': 'Healthcare',
    'summary': "A module for managing hospital operations, patients, and doctors",
    'description': """
        This module helps in managing hospital records, including patients, doctors, and appointments.
    """,
    'data': [
        'views/chandoan_action.xml',
        'views/chandoan_menu.xml',
        'views/xetnghiem.xml',
        'views/hinhanh.xml',
        'views/loaixetnghiem.xml',
        'views/loaihinhanh.xml',
        'security/ir.model.access.csv',
        'data/loaixetnghiem_data.csv',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
