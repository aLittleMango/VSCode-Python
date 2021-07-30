'''
Description: 
Author: aLittleMango
Date: 2021-07-29 14:40:06
LastEditTime: 2021-07-29 14:40:07
FilePath: /VSCode-Python/crawlerDemo/test1/xlwtTest.py
'''

import xlwt


workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('Mul_table')
for x in range(1,10):
    print("  ")
    for y in range(1,x+1):
        worksheet.write(x-1,y-1,"%d*%d = %2d"%(x,y,x*y)) 

workbook.save('Test.xls')