'''
Description: 
Author: aLittleMango
Date: 2021-07-21 15:06:52
LastEditTime: 2021-07-21 16:21:21
FilePath: \VSCode-Python\learnTest\TupleDemo.py
'''

tup1 = (11, 22, "aa")
print(type(tup1))
print(tup1)

#不能修改元素内容，但可以新增（连接）
tup2 = ("bb",)  #一定要是元组类型
tup_add = tup1 + tup2
print(tup_add)

#删除了整个元组变量
del tup1
