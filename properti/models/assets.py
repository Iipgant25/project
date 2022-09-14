from odoo import api, fields, models
import random

class Assets(models.Model):
    _name = 'properti.assets'
    _description = 'New Description'


    name = fields.Char(string='Nama Assets')
    type = fields.Selection([
        ('sawah', 'Sawah'),
        ('ladang', 'Ladang'),
        ('rumah', 'Rumah')
    ], string='Type Assets')
    
    alamat = fields.Char(string='Alamat Pemilik')
    kode_assets = fields.Char(onchange='_compute_kode_assets', string='Kode Assets')
    harga_assets = fields.Integer(string='Harga Assets')
    pemilik = fields.Char(string='Pemilik Assets')
    asset = fields.Char(string='Status Pembeli')
    lokasi = fields.Char(string='Lokasi')
    luas_assets = fields.Char(string='Luas Assets')
 
    
    
    @api.onchange('type')
    def _onchange_kode_assets(self):
        
        kode = str(random.randint(1, 1e3))
        
        if self.type == 'sawah':
            self.kode_assets = 'SWH' + kode
        elif self.type == 'ladang':
            self.kode_assets = 'LDG' + kode
        elif self.type == 'rumah':
            self.kode_assets = 'RMH' + kode
            
        
