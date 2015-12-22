# -*- coding: utf-8 -*-
from openerp import http

# class WebsiteSaleDistribution(http.Controller):
#     @http.route('/website_sale_distribution/website_sale_distribution/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_sale_distribution/website_sale_distribution/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_sale_distribution.listing', {
#             'root': '/website_sale_distribution/website_sale_distribution',
#             'objects': http.request.env['website_sale_distribution.website_sale_distribution'].search([]),
#         })

#     @http.route('/website_sale_distribution/website_sale_distribution/objects/<model("website_sale_distribution.website_sale_distribution"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_sale_distribution.object', {
#             'object': obj
#         })
import werkzeug

from openerp import SUPERUSER_ID
from openerp import http
from openerp.http import request
from openerp.tools.translate import _
from openerp.addons.website.models.website import slug
from openerp.addons.web.controllers.main import login_redirect

from openerp.addons.website_sale.controllers.main import website_sale

# res.partner.bank.type
# iban = 
# bank = 
class WebsiteSale(website_sale):
    
    # def checkout_values(self, data=None):
    #     cr, uid, context, registry = request.cr, request.uid, request.context, request.registry
    #     orm_bank_type = registry.get('res.partner.bank.type')
    #     banks_type_ids = orm_bank_type.search(cr, SUPERUSER_ID, [], context=context)
    #     bank_types = orm_bank_type.browse(cr, SUPERUSER_ID, banks_type_ids, context)


    #mandatory_billing_fields = ["name", "phone", "email", "street2", "city", "country_id", "vat", "zip", "state_id", "bank_account"]
    mandatory_billing_fields = ["name", "phone", "email", "street2", "city", "country_id", "vat", "zip", "state_id", ]
    optional_billing_fields = ["street", "vat_subjected"]
    mandatory_shipping_fields = ["name", "phone", "street", "city", "country_id","state_id", "zip"]
    optional_shipping_fields = []