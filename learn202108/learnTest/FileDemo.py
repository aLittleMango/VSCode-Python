'''
Description: 
Author: aLittleMango
Date: 2021-07-22 10:14:46
LastEditTime: 2021-07-22 16:06:18
FilePath: \VSCode-Python\learnTest\fileDemo.py
'''

#打开文件，w模式，文件不存在就新建一个
f = open("test.txt","w") 
f.write("hello today is thursday--1\nhello today is thursday--2") 
f.close() #关闭文件

f = open("test.txt","r") 
# content = f.read(5)
# print(content)
content = f.readlines() # 一次性读取全部文件为列表，每行一个字符串元素
print(content)

i = 1
for temp in content:
    print("%d:%s"%(i,temp),end = '')
    i +=1
print("\n")
f.close() #关闭文件
f = open("test.txt","r") 
content = f.readline()
print("读一行: %s"%content)
f.close() #关闭文件

