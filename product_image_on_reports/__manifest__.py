# -*- coding: utf-8 -*-

{
    'name': 'Product Image on Reports',
    'version': '10.0.1.0.0',
    'category': 'Sale',
    'license': 'AGPL-3',
    'summary': '''This module shows image of product on reports such as sales, invoice and purchase''',
    'author': 'Aktiv Software',
    'depends': [
        'sale', 'purchase'
    ],
    'website': 'www.aktivsoftware.com',
    'data': [
        'views/report_invoice.xml',
        'views/sale_report_template.xml',
        'views/purchase_order_templates.xml'

    ],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'installable': True,
    'auto_install': False,
}
