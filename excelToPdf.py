import openpyxl

# wb = openpyxl.load_workbook('payslip blank.xlsx')
# sheet = wb.active
# cellValue = sheet[f'A2'].value
#
# print(cellValue)
# sheet[f'B2'].value = '16020013'
#
# wb.save('payslip blank.xlsx')


from win32com import client

xlApp = client.Dispatch("Excel.Application")
books = xlApp.Workbooks.Open("C:\\Users\\SURAJ\\Desktop\\payslip blank.xlsx")
ws = books.Worksheets[0]
ws.Visible = 1
ws.ExportAsFixedFormat(0, "C:\\Users\\SURAJ\\Desktop\\final.pdf")
