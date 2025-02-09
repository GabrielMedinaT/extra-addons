# -*- coding: utf-8 -*-
{
    'name': "Sucursales",

    'summary': """
        Gestión de sucursales bancarias con administración de empleados, cajeros y reparaciones""",

    'description': """
        Este módulo permite la gestión y control de las sucursales de un banco, diferenciando entre aquellas que cuentan con cajeros y las que no. 

        Funcionalidades principales:
        - Administración de sucursales con empleados y cajeros.
        - Control de cajeros automáticos, su estado y reparaciones.
        - Gestión de roles de usuario: supervisor, encargado, cajero y reparador.
        - Vistas tree y form para sucursales, empleados, cajeros y reparaciones.
        - Listados de empleados y cajeros dentro de cada sucursal con pestañas organizadas.
        - Campo calculado para contar los cajeros en cada sucursal.
        - Registro de reparaciones con asignación de empleados y firma digital.
        - Reportes e historiales de averías de los cajeros.
        - Configuración con opciones para visualizar el historial de averías y requerir firma en reparaciones.
        
        El módulo está diseñado para optimizar la gestión operativa de las sucursales y garantizar un control eficiente de los cajeros automáticos.""",

    'author': "Sucursales",
    'website': "https://www.yourcompany.com",

    'category': 'Banking',
    'version': '1.0',

    'depends': ['base', 'hr'],

    'data': [
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

    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
