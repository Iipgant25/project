from odoo import models, fields

class PartnerXlsx(models.AbstractModel):
    _name = 'report.properti.report_properti_transaksi_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    
    def generate_xlsx_report(self, workbook, data, pembelian):
        sheet = workbook.add_worksheet('Daftar Pembeli')
        bold = workbook.add_format({'bold': True})
        sheet.write(1, 0, 'Kode Assets', bold)
        sheet.write(1, 1, 'Nama Pembeli', bold)
        sheet.write(1, 2, 'Tanggal Transaksi', bold)
        sheet.write(1, 3, 'Nama Assets', bold)
        sheet.write(1, 4, 'Harga Assets', bold)
        row = 2
        for obj in pembelian:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.nasabah_id.display_name)
            
            date = str(obj.tgl_transaksi)
            sheet.write(row, col+2, date)
            
            sheet.write(row, col+3, obj.assets_id.name)
            sheet.write(row, col+4, obj.harga)
            
            row += 1