# -*- coding: utf-8 -*-
{
    'name': "Distribution - Remove the price",

    'summary': """
        This module will remove the prices when the
        partner is not loged in""",

    'description': """
        The purpouse of this module is to remove the prices when the partner is not
        loged in and offer a distribution register to get in touch with the leads.
        
        This also imroves the contact form by making the phone field required.
    """,

    'author': "Tomás Pereira Cruz",
    'website': "http://www.percar.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    'images' : [],
    'installable' : True,
    'application' : True,
}
