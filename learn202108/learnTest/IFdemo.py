'''
Description: 判断语句IF
Author: aLittleMango
Date: 2021-07-15 20:23:08
LastEditTime: 2021-07-16 11:27:56
FilePath: \VSCode-Python\learnTest\IFandFOR.py
'''

#输入三个数，比大小
a, b, c = input("please input the value of a,b,c:").split(",")

max = 0

if a > b:
    max = a
elif b > c:
    max = b
else:
    max = c

print("max value is:%s" % max)
