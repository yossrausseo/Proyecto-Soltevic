{
    'name': 'Ocultar Balance en el POS',
    'version': '17.0.1.0.0',
    'summary': 'Oculta el valor del balance en la vista kanban del POS',
    'description': 'Este módulo oculta el valor del balance en la vista kanban de configuraciones POS',
    'category': 'Point of Sale',
    'author': 'Yosmari Rausseo',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_config_views.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}