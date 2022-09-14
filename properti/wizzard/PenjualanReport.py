from odoo import fields, models, api


class PenjualanReport(models.TransientModel):
    _name = 'properti.penjualanreport'
    _description = 'Description'

    konsumen_id = fields.Many2one(
        comodel_name='res.partner',
        string='Konsumen',
        required=False, 
        domain=[('status', '=', 'konsumen')])
    
    states = fields.Selection(
        string='Status',
        selection=[('draft', 'Draft'),
                   ('confirm', 'Confirm'),
                   ('done', 'Done'),
                   ('cancelled', 'Cancelled'),
                   ],
        default='draft')

    def action_penjualan_report(self):
        filter = []
        konsumen_id = self.konsumen_id
        status = self.states
        if konsumen_id:
            filter += [('konsumen_id', '=', konsumen_id.id)]
        if status == 'draft':
            filter += [('state', '=', 'draft')]
        if status == 'confirm':
            filter += [('state', '=', 'confirm')]
        if status == 'done':
            filter += [('state', '=', 'done')]
        if status == 'cancelled':
            filter += [('state', '=', 'cancelled')]
            
        print(filter)
        penjualan = self.env['properti.transaksi'].search_read(filter)
        print(penjualan)
        data = {
            'form': self.read()[0],
            'penjualan_assets': penjualan,
        }
        print(data)
        return self.env.ref('properti.wizzard_penjualanreport_pdf').report_action(self, data=data)
