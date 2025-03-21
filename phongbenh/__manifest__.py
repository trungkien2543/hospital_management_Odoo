{
    'name': "Quan ly phong benh",
    'version': '1.1',
    'depends': ['base'],
    'author': "Your Name",
    'category': 'Healthcare',
    'summary': "A module for managing phong benh",
    'description': """
        This module helps in managing phong benh.
    """,
    'data': [
        'views/phongbenh_menu.xml',
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
