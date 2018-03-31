# -*- coding: utf-8 -*-

{
    'name': 'Product Image on Sales Invoice Purchase Report',
    'version': '1.0',
    'category': 'Sale',
    'summary': '''
        ''',
    'author': 'Aktiv Software',
    'depends': [
        'sale', 'purchase'
    ],
    'website': 'www.aktivsoftware.com',
    'data': [
        'views/report_invoice.xml',
        'views/report_saleorder.xml',
        'views/report_purchaseorder.xml',

    ],
    'images': [],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'auto_install': False,
}
