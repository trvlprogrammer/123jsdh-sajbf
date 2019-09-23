# -*- coding: utf-8 -*-
{
    'name': "Scheduler Report Creator",
    'summary': """
        Scheduler for report creator""",
    'description': """
        Scheduler for report creator to generet report automatically.
    """,    
    'author': "Alfatih Ridho NT",
    'website': "alfatihridhont@gmail.com",
    'category': 'Sale',
    'license': 'OPL-1',
    'price' : '40',
    'currency' : 'EUR',
    'version' : '10.0.1',
    'support' : 'alfatihridhont@gmail.com',
    'images': ['images/main_screenshot.jpeg'],
    'depends': ['report_creator'],    
    'data': [        
        'views/views.xml',
        'views/scheduler.xml',
    ],        
}