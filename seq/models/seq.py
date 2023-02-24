from odoo import fields, models, api


class SequenceOrder(models.Model):
    _name = "sequence.order"

    sequence = fields.Char("Order Reference", required=True, index=True, copy=False, default="New", readonly=True)
    name = fields.Char(string="Name", required=True)
    country = fields.Many2one('res.country', string="Country")

    @api.model
    def create(self, vals):
        if vals.get('sequence', 'New'):
            vals['sequence'] = self.env['ir.sequence'].next_by_code('sequence.order') or 'New'
        return super(SequenceOrder, self).create(vals)

    # def demo_cron_method(self):
    # 	print("---------------------------------------------------------------------------------------")

    def action_copy_seq(self):
        for i in self.browse(self.env.context['active_ids']):
            print(
                "=======================================================================================")
            i.copy()
            print("-------------------------------------------------------------------------------", i)
        return i
