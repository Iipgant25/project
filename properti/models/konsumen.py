from odoo import api, fields, models


class Nasabah(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    tgl_daftar = fields.Date(string='Tanggal Pendaftaran', default = fields.Datetime.now())
    status = fields.Char(string='Status')
    
    transaksi_ids = fields.One2many('properti.transaksi', 'konsumen_id', string='Transaksi')