from odoo import http, _
from odoo.http import request

class PosOrder(http.Controller):

    @http.route('/api/pos_session_orders', type='json', auth='user')
    def get_pos_session_orders(self, session_id=None):
        try:
            if session_id:
                pos_session = request.env['pos.session'].browse(int(session_id))

            if not pos_session:
                return 'No open POS session found.'

            orders = pos_session.order_ids.read(['name', 'amount_total', 'state'])
            return {'orders': orders}

        except Exception as e:
            return {'error': str(e)}

    @http.route('/api/get_orders', type='json', auth='user')
    def get_orders(self, start_date=None, end_date=None):
        try:

            domain = []

            if start_date:
                domain.append(('create_date', '>=', start_date))
            if end_date:
                domain.append(('create_date', '<=', end_date))

            orders = request.env['sale.order'].search_read(domain, ['name', 'amount_total', 'state'])
            return {'orders': orders}

        except Exception as e:
            return {'error': str(e)}

    @http.route('/api/pos_products', type='json', auth='user')
    def get_rop_products(self):
        try:
            products = request.env['product.template'].search_read([('rop_count', '>=', 1)], ['name'])
            return {'products': products}

        except Exception as e:
            return {'error': str(e)}
    @http.route('/api/ropcount', type='json', auth='user', methods=['POST'])
    def add_rop_count_to_product(self, product_id=None, rop=None):
        try:
            if not product_id or not rop:
                return 'Both product_id and rop parameters are required.'

            product = request.env['product.template'].browse(int(product_id))
            if not product:
                return 'Product not found.'

            product.write({'has_rop': True,'rop_count':rop })

            return {'success': 'rop_count added successfully.'}

        except Exception as e:
            return {'error': str(e)}

    @http.route('/api/rop-product', type='json', auth='user')
    def get_rop_products(self):
        try:
            rop_products = request.env['product.template'].search_read([('qty_available', '<', 5)],
                                                                      ['name', 'list_price', 'qty_available'])
            return {'rop_products': rop_products}

        except Exception as e:
            return {'error': str(e)}