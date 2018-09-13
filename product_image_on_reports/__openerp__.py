# -*- coding: utf-8 -*-

{
    'name': 'Product Image on Sales Invoice Purchase Report',
    'version': '9.0.1.0.0',
    'license': 'AGPL-3',
    'summary': '''This module shows image of product on reports such as sales, invoice and purchase''',
    'category': 'Sale',
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
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'auto_install': False,
}
