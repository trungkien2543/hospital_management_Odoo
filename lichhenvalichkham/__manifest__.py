{
    'name': 'Lich hen va lich kham',
    'summary': 'Quan ly lich hen va lich kham',
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
        'data/sequence.xml',
        'views/datlichhen_view.xml',
        'views/datlichhen_action.xml',
        'views/datlichhen_menu.xml',
        'security/ir.model.access.csv',
    ],

    'installable': True,
    'application': True,
}
