# -*- coding: utf-8 -*-
{
    'name': "Multiple Discount For Sale & Invoice",

    'summary': """
        Multiple discount in sale and invoicing""",

    'description': """
        Thank you for buying this module.
        This module inherit sale and account to add new feature called multiple discount.
        If you need customization odoo you can email me at alfatihridhont@gmail.com
    """,

    'author': "Alfatih Ridho NT",
    'website': "alfatihridhont@gmail.com",
    'category': 'Sale',
    'license': 'OPL-1',
    'price' : '40',
    'currency' : 'EUR',
    'version' : '12.0.1',
    'support' : 'alfatihridhont@gmail.com',
    'depends': ['base','sale_management'],
    'images': ['images/main_screenshot.jpeg'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
    ],
}