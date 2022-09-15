from odoo import fields, models, api


class AssetsReport(models.TransientModel):
    _name = 'properti.assetsreport'
    _description = 'Description'


    
    status_pembelian = fields.Selection(
        string='Status',
        selection=[('Assets Sudah Di Beli', 'Di Beli'),
                   ('Assets Belum Di Beli', 'Belum Di Beli'),
                   ])
    
    
    def action_assets_report(self):
        filter = []
        status = self.status_pembelian
        
        if status == 'Assets Sudah Di Beli':
            filter += [('asset', '=', 'Di Beli')]
        elif status == 'Assets Belum Di Beli':
            filter += [('asset', '=', 'Belum Di Beli')]
            
        print(filter)
        penjualan = self.env['properti.assets'].search_read(filter)
        print(penjualan)
        data = {
            'form': self.read()[0],
            'penjualan': penjualan,
        }
        print("_______________________________________________________")
        print(data)
        return self.env.ref('properti.wizzard_assetsreport_pdf').report_action(self, data=data, config=False)

    