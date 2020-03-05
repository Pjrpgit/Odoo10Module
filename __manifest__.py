# -*- coding: utf-8 -*-
{
    'name': "fct_barajas",

    'summary': """
        Administración y gestión para las FCT""",

    'description': """
        Ayuda al profesorado en la administración de tareas basicas requeridas
        en el proceso de prácticas del alumno. Permitiendo consultar, insertar,
        actualizar y borrar datos""",

    'author': "Pedro J. Rivera",
    'website': "http://www.yourcom.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.4',

    # any module necessary for this one to work correctly
    'depends': ['base','report'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/report_empresa.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
