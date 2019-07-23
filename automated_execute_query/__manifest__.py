
{
    'name': "Automated Execute Query",

    'summary': """
        Automated Execute Query""",

    'description': """
        You can execute query from your odoo application
    """,

    'author': "Alfatih Ridho NT",
    'website': "alfatihridhont@gmail.com",    
    'category': 'Tools',
    'version': '11.0.1',    
    'license': 'AGPL-3',
    'images': ['images/main_screenshot.jpg'],
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/scheduler.xml',
        'views/templates.xml',
    ],    
}