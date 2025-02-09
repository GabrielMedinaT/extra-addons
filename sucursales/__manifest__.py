# -*- coding: utf-8 -*-
{
    'name': "Sucursales",

    'summary': """
        Modulo de sucursales donde tendremos unas con cajero y otras sin""",

    'description': """
        Modulo de sucursales
    """,

    'author': "Sucursales",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'reports/reparaciones_report.xml',
        'reports/reparaciones_report_view.xml',
        'reports/cajeros_report.xml',
        'reports/cajeros_report_view.xml',
        'reports/sucursales_report.xml',
        'reports/sucursales_report_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':'True',
}
