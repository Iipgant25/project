from odoo import models, fields

class PartnerXlsx(models.AbstractModel):
    _name = 'report.properti.report_properti_assets_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    
    def generate_xlsx_report(self, workbook, data, assets):
        sheet = workbook.add_worksheet('Daftar Penyewa')
        bold = workbook.add_format({'bold': True})
        sheet.write(1, 0, 'Kode Assets', bold)
        sheet.write(1, 1, 'Nama Assets', bold)
        sheet.write(1, 2, 'Lokasi', bold)
        sheet.write(1, 3, 'Luas Assets', bold)
        sheet.write(1, 4, 'Harga Assets', bold)
        sheet.write(1, 5, 'Pemilik', bold)
        sheet.write(1, 6, 'Status', bold)
        row = 2
        for obj in assets:
            col = 0
            sheet.write(row, col, obj.kode_assets)
            sheet.write(row, col+1, obj.name)
            sheet.write(row, col+2, obj.lokasi)
            sheet.write(row, col+3, obj.luas_assets)
            sheet.write(row, col+4, obj.harga_assets)
            sheet.write(row, col+5, obj.pemilik)
            sheet.write(row, col+6, obj.asset)
            
            row += 1