import xlwt

# 使用xlwt库生成excel文件
book = xlwt.Workbook(encoding='utf-8')
sheet1 = book.add_sheet('Sheet1')
sheet2 = book.add_sheet('Sheet2')

# 前两个参数是坐标（注意第一行和第一列不计入坐标），第三个参数是内容
sheet1.write(1, 1, '世界，你好')
sheet1.write(2, 2, '用Python操作Excel文件')
sheet2.write(2, 2, 'Hello World')

book.save('demo.xls')
