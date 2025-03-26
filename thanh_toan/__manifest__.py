# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Quan ly thanh toan',
    'version': '1.0.0',
    'summary': 'Manage your invoice',
    'depends': [],
    'category': 'Healthcare',
    'sequence': 25,
    'demo': [

    ],
    'data': [
        'security/ir.model.access.csv',
        'views/thanh_toan_actions.xml',
        'views/thanh_toan_menus.xml',
        'views/dich_vu_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
