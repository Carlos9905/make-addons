ODOO_14 = '14.0.0.0.0'
ODOO_15 = '15.0.0.0.0'
WEB_SITE_MULTISERVICIOS = 'https://www.multiserviciosrl.co.cr'
WEB_SITE_BRAINTECH = 'https://www.braintch.net'
MANIFEST_FILE_MULTISERVICIOS = {
    'name': 'Model Name',
    'version': ODOO_14,
    'summary': """ Model Name""",
    'description': """Model Name.""",
    'author': 'José Carlos Aguilar',
    'company': 'Multiservicios R&L SRL',
    'maintainer': 'Multiservicios R&L SRL',
    'website': WEB_SITE_MULTISERVICIOS,
    'license': 'LGPL-3', 
    'depends': ['base'],
    'data': [
             'security/ir.model.access.csv',
             ],
    'installable': True,
    'application': True,
}
MANIFEST_FILE_BRAINTECH = {
    'name': 'Model Name',
    'version': ODOO_15,
    'summary': """ Model Name""",
    'description': """Model Name.""",
    'author': 'José Carlos Aguilar',
    'company': 'Multiservicios R&L SRL',
    'maintainer': 'Multiservicios R&L SRL',
    'website': WEB_SITE_BRAINTECH,
    'license': 'LGPL-3', 
    'depends': ['base'],
    'data': [
             'security/ir.model.access.csv',
             ],
    'installable': True,
    'application': True,
}