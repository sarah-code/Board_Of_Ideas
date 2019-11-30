# -*- coding: utf-8 -*-
{
    'name': "Board of ideas",

    'summary': """
        This addon facilitates the management of ideas in a company.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "sarah-code",
    'website': "https://github.com/sarah-code",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Tools",
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/boi_views.xml',
        
    ],
    'installable': True,
    'application': True,

}