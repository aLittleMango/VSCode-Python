'''
Description: 
Author: aLittleMango
Date: 2021-07-22 11:31:59
LastEditTime: 2021-07-22 15:43:29
FilePath: \VSCode-Python\learnTest\errorDemo.py
'''
import time

'''
try:
    print("-"*10,"test---1-----")
    f = open("123.txt","r")
    print("-"*10,"test---1-----")
except IOError: #捕获异常，文件没找到，属于IO异常
    pass  #捕获异常后，执行的代码

try:
    print(num)
except NameError: #异常类型想要被捕获，需要一致
    print("name error")

try:
    print("-"*10,"test---1-----")
    f = open("123.txt","r")
    print("-"*10,"test---1-----")

    print(num)
except (NameError,IOError) as result:  #或者直接用Exception
    print("产生错误了")
    print(result)
'''
#-----------try finally 和嵌套
try:
    f=open("test.txt","r")
    
    try:
        while True:
            content = f.readline()
            if len(content)==0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭")
except Exception as result:
    print("发生异常")