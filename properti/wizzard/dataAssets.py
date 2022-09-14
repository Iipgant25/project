from odoo import fields, models, api


class AssetsReport(models.TransientModel):
    _name = 'properti.assetsreport'
    _description = 'Description'

    
    status_pembelian = fields.Selection(
        string='Status',
        selection=[('dibeli', 'Di Beli'),
                   ('belum', 'Belum Di Beli'),
                   ])

    