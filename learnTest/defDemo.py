'''
Description: 
Author: aLittleMango
Date: 2021-07-22 09:32:02
LastEditTime: 2021-08-06 15:06:22
FilePath: \VSCode-Python\learnTest\defDemo.py
'''

def printInfo():
    print("-"*30)
    print("函数定义的例子")
    print("-"*30)

printInfo()

#返回多个值的函数
def divid(a,b):
    shang = a//b
    yushu = a%b
    return shang,yushu
#一定要用多个值返回接收一下
sh,yu = divid(5,2)

print("商: %d, 余数: %d"%(sh,yu))

print("-"*10,"全局变量和局部变量","-"*10)
a =100
def test1():
    global a
    print("test1 修改前: a = %d"%a)
    a = 200
    print("test1 修改后: a = %d"%a)

def test2():
    print("test2 : a = %d"%a)

test1()
test2()

