{
    'name': 'Sales Custom',
    'version': '1.0',
    'depends': ['base', 'sale'],
    'data': [
        'views/sale_order_view.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend': [
            'sales_custom/static/src/js/*.js',
            'sales_custom/static/src/css/*.css',
        ],
    },
}
