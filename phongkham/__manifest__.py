{
    'name': "Quan ly phong kham",
    'version': '1.1',
    'depends': ['base'],
    'author': "Your Name",
    'category': 'Healthcare',
    'summary': "A module for managing hospital operations, patients, and doctors",
    'description': """
        This module helps in managing hospital records, including patients, doctors, and appointments.
    """,
    'data': [
        'views/phongkham_menu.xml',
        'views/phongkham_information.xml',
        'views/sudungphongkham.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
