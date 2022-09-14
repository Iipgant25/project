import random
from odoo import api, fields, models
from dateutil.relativedelta import relativedelta
from datetime import date
from odoo.exceptions import UserError, ValidationError


class Transaksi(models.Model):
    _name = 'properti.transaksi'
    _description = 'New Description'

    name = fields.Char(string='Kode Transaksi')
    konsumen_id = fields.Many2one(comodel_name='res.partner', string='Konsumen', domain=[('status', '=', 'konsumen')])
    assets_id = fields.Many2one(comodel_name='properti.assets', string='Data Assets', domain=[('asset', '=', 'Belum Di Beli')])
    tgl_transaksi = fields.Date(string='Tanggal Transaksi', default = fields.Datetime.now(), readonly=True)

    harga = fields.Char(compute='_compute_asset', string='Harga Assets', readonly=True)
    kode = fields.Char(compute='_compute_asset', string='Kode Assets')
    
    state = fields.Selection(
        string='Status',
        selection=[('draft', 'Draft'),
                   ('confirm', 'Confirm'),
                   ('done', 'Done'),
                   ('cancelled', 'Cancelled'),
                   ],
        required=True, readonly=True, default='draft')
    
    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_done(self):       
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_draft(self):
        self.write({'state': 'draft'})
    
    
    @api.depends('assets_id')
    def _compute_asset(self):
        for record in self:
            a = self.env['properti.assets'].search([('id', '=', record.assets_id.id)])
            record.harga = a.harga_assets
            record.kode = a.kode_assets
            
    @api.model
    def create(self, vals):
        rec = super(Transaksi, self).create(vals)
        if rec.assets_id:
            a = self.env['properti.assets'].search([('id', '=', rec.assets_id.id)])
            if a.asset == 'Belum Di Beli':
                self.env['properti.assets'].search([('id', '=', rec.assets_id.id)]).write({'asset': 'Di Beli'})
            else :
               raise ValidationError("Mohon Maaf Assets Yang Anda Pilih Telah Di beli oleh Nasabah Lain!!!")
        return rec
    
    @api.ondelete(at_uninstall=False)
    def __ondelete_penyewaan(self):
        if self.assets_id:
            if self.filtered(lambda line: line.state != 'draft'):
                raise UserError("Tdak dapat menghapus jika status BUKAN DRAFT")
            else:
                for rec in self:
                    self.env['properti.assets'].search([('id', '=', rec.assets_id.id)]).write({'asset': 'Belum Di Beli'})
                
            
    def write(self, vals):
        for rec in self:
            self.env['properti.assets'].search([('id', '=', rec.assets_id.id)]).write({'asset': 'Belum Di Beli'})
                
        record = super(Transaksi,self).write(vals)
        
        for rec in self:
            if rec.assets_id:
                a = self.env['properti.assets'].search([('id', '=', rec.assets_id.id)])
                if a.asset == 'Belum Di Beli':
                    self.env['properti.assets'].search([('id', '=', rec.assets_id.id)]).write({'asset': 'Di Beli'})
                else :
                    raise ValidationError("Mohon Maaf Assets Yang Anda Pilih Telah Di Beli Oleh Nasabah Lain!!!")
            
        return record