# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'DemoVersie',
    'version': '1.0.0',
    'category': 'Demo',
    'author': 'Odoo mates',
    'sequence': -100,
    'summary': ' management system',
    'description': """Odoo DemoVersie""",
    'depends': ['mail', 'product', 'sale', 'sales_team', 'contacts', 'mrp', 'account', 'base_iban', 'base_vat',
                'base_address_extended',
                'l10n_nl',
                'l10n_latam_invoice_document',
                'l10n_latam_base',
                'base_setup',
                'base',
                'account_edi_ubl_bis3',
                'stock',
                'resource',
                'barcodes',
                'digest',
                'base_setup',
                'analytic',
                'purchase_stock',
                ],
    'data': [
        'data/data.xml',
        'data/data_products.xml',
        'data/data_bills.xml',
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3',
}