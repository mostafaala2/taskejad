from odoo import api,_, models,fields
from odoo.exceptions import ValidationError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    @api.constrains('scheduled_date')
    def _check_scheduled_date(self):
        for picking in self:
            if picking.picking_type_id.code == 'outgoing' and picking.scheduled_date  >= fields.Date.today():
                raise ValidationError(_("Picking type is outgoing and picking date is not valid."))

