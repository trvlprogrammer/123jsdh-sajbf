# -*- coding: utf-8 -*-
{
    'name': "Report Creator",

    'summary': """
        With this module you can generate report  xls,csv and pdf without coding
        """,

    'description': """
        With this module you can generate report  xls,csv and pdf without coding, 
        for more development you can email me @alfatihridhont@gmail.com
    """,

    'author': "Alfatih Ridho NT",
    'website': "alfatihridhont@gmail.com",    
    'category': 'Report',
    'sequence': 5,
    'license': 'OPL-1',
    'price' : '98',
    'currency' : 'EUR',
    'version' : '11.0.1',
    'support' : 'alfatihridhont@gmail.com',
    'images': ['images/main_screenshot.jpeg'],  
    'depends': ['base_setup'],
    'data': [
        'security/report_creator.xml',               
        'views/views.xml',
        'views/templates.xml',
        'views/res_config_settings.xml',
        'wizard/wizard_get_report.xml',        
        'security/ir.model.access.csv', 
    ],    
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}