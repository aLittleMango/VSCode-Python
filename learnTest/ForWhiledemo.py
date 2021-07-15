'''
Description: 循环语句
Author: aLittleMango
Date: 2021-07-16 14:20:22
LastEditTime: 2021-07-16 14:31:43
FilePath: \VSCode-Python\learnTest\ForWhiledemo.py
'''

for i in range(5):
    print(i)

for i in range(2, 10, 3):
    print(i)

#遍历字符串
name = "changsha"
for i in name:
    print(i, end="\t")

#遍历列表
a = ["hello", "world", "!", "happy", "friday"]
for i in range(len(a)):
    print(i, a[i])

i = 0
while i < 5:
    print("当前是第%d次循环,i=%d"%(i+1,i))
    i+=1