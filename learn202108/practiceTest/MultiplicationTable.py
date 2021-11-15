'''
Description: 打印九九乘法表
Author: aLittleMango
Date: 2021-07-20 19:43:23
LastEditTime: 2021-07-20 20:53:48
FilePath: \VSCode-Python\practiceTest\MultiplicationTable.py
'''

'''
for j in range(1,10,1):
    i = 1
    while i <= j : 
        print("%d*%d = %2d"%(i,j,i*j),end = "  ")
        i+= 1
    else:
        print(" ")
'''


for x in range(1,10):
    print("  ")
    for y in range(1,x+1):
        print("%d*%d = %2d"%(x,y,x*y),end="  ")