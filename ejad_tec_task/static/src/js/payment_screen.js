odoo.define('ejad_tec_task.payment_screen', function (require) {
    'use strict';

    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    var rpc = require('web.rpc');

    const PosejProductScreen = ProductScreen => class extends ProductScreen {

    async _onClickPay() {
    const order = this.env.pos.get_order();
    const lines = order.get_orderlines();

    lines.forEach((quantity) => {
            var available_qty = quantity.product.qty_available
            if (available_qty < 5) {
            this.showPopup('ErrorPopup', {
                title: 'Custom Message',
                body: "This product under of the Re-Order Point measure",
            });
            const result =   rpc.query({
                model: 'product.product',
                method: 'send_notification',
                args: [quantity.product.id],
                kwargs: {
                product_id: quantity.product.id,
                },
            })
        }
       })
       await super._onClickPay()
    }}
    Registries.Component.extend(ProductScreen, PosejProductScreen);

    return ProductScreen;
});
