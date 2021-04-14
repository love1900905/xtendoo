{
    'name': 'LCH Administrator',
    'summary': """Administration settings for La Casa del Hostelero""",
    'version': '12.0.1.0.0', 
    'author': 'Daniel Domínguez',
    'company': 'Xtendoo',
    'website': 'https://xtendoo.es/',
    'category': 'Extra Tools',
    'depends': [
        'base',
        'sale',
        'product',
        'sale_margin',
        'product',
        'account',
        'account_invoice_margin',
        'account_invoice_margin_sale',

    ],
    'license': 'AGPL-3',
    'data': [
        'views/sale_order_view_restrict.xml',
        'views/account_payment.xml',
        'views/account_invoice_restrict.xml',
        'views/product_template_restrict.xml',
        'security/security.xml',
    ],
    'installable': True,
    'auto_install': True,
}
