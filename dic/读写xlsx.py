import xlrd
import xlwt

# 读取xlsx
xlsx = xlrd.open_workbook('1.xlsx')
table = xlsx.sheet_by_index(0)
print(table.cell_value(0, 0))
print(table.cell(1, 2).value)
print(table.row(2)[2].value)

# 写入，保存xlsx
new_workbook = xlwt.Workbook()
worksheet = new_workbook.add_sheet('new_test')
worksheet.write(0, 0, 'test')
worksheet.write(6, 9, 'tfest')
new_workbook.save('test.xlsx')