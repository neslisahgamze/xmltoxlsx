import xmltodict, json
import xlsxwriter
from collections import OrderedDict

f = open('deneme.xml')
xml = f.read()
o = xmltodict.parse(xml)

products = o['root']['list-item']

workbook = xlsxwriter.Workbook('xmltoxlsx.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})

worksheet.write('A1', 'Name', bold)
worksheet.write('B1', 'Description', bold)
worksheet.write('C1', 'Category', bold)
worksheet.write('D1', 'Vat', bold)
worksheet.write('E1', 'Sku', bold)
worksheet.write('F1', 'Barcode', bold)
worksheet.write('G1', 'Weight', bold)
worksheet.write('H1', 'Stock', bold)
worksheet.write('I1', 'Price', bold)
worksheet.write('J1', 'URL',bold )

row=1
col=0

for odict in products:
	worksheet.write(row, col,   odict['name'])
	worksheet.write(row, col+1, odict['description'])
	worksheet.write(row, col+2, odict['category'])
	worksheet.write(row, col+3, odict['vat'])
	worksheet.write(row, col+4, odict['products']['list-item']['sku'])
	worksheet.write(row, col+5, odict['products']['list-item']['barcode'])
	worksheet.write(row, col+6, odict['products']['list-item']['weight'])
	worksheet.write(row, col+7, odict['products']['list-item']['stock'])
	worksheet.write(row, col+8, odict['products']['list-item']['price'])
	#worksheet.write(row, col+9, json.dumps(odict['products']['list-item']['images']['list-item']).items)
	row += 1
workbook.close()
