{
    'name': 'Benh nhan',
    'summary': 'Quan ly thong tin benh nhan',
    'description': '''
        Testing Purpuses.
    ''',
    'version': '18.0.1.0.0',
    'category': 'Healthcare',
    'license': 'LGPL-3',
    'author': 'Odooistic',
    'website': 'https://www.youtube.com/',
    'depends': [
        'base',
    ],
    'data': [
        'views/benhnhan_view.xml',
        'views/benhnhan_action.xml',
        'views/benhnhan_menu.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/patient_data.xml',
    ],

    'installable': True,
    'application': True,
}
