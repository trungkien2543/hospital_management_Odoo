# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Medicine Manage',
    'version': '1.0.0',
    'summary': 'Manage your stock and logistics activities',
    'website': '',
    'depends': [],
    'category': 'Hopital',
    'sequence': 25,
    'demo': [

    ],
    'data': [
        'security/ir.model.access.csv',
        'views/medicine_action.xml',
        'views/medicine_menus.xml',
        'views/medicine_views.xml',
        'views/don_vi_tinh_views.xml',
        'views/tuong_tac_thuoc.xml',
        'views/phieu_nhap_views.xml',
        'data/medicine_sequence.xml',
        'data/phieu_nhap_sequence.xml',
        'data/lo_hang_sequence.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
