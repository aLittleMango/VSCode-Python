'''
Description: 
Author: aLittleMango
Date: 2021-07-20 20:56:22
LastEditTime: 2021-07-21 10:10:07
FilePath: \VSCode-Python\learnTest\StringDemo.py
'''

s1='abc'
s2 = "ABC"
s3 = ''' 
a B 
C '''
print(s1,s2,s3)

s4 = 'I\'m a student'
print(s4)  #转义字符
print(r'I\'m a student')

s5 = "1234567"
print(s5[0:2]) #左闭右开
print(s5[0:6:2]) #[起始位置：结束位置：步进值]
print(s5[5:0:-1])

print("-"*30)
print(s5+",你好")

print(s4.isalnum())