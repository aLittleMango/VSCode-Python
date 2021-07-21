'''
Description: 
Author: aLittleMango
Date: 2021-07-21 10:10:44
LastEditTime: 2021-07-21 14:32:33
FilePath: \VSCode-Python\learnTest\ListDemo.py
'''


testList = ["小郭",709,"小洪",1016]
print(testList[0:3:2])

for i in testList:
    if type(i) == int:
        print(i)

testList.extend(["纪念日","1014"])
print(testList)

testList.insert(0,1314)
print(testList)

del testList[0]
print(testList)

testList.pop()
print(testList)

testList[4]="1314"
print(testList)

list1=[1,3,2]
list1.sort()  #升序
print(list1) 

list1.sort(reverse=True)  #降序
print(list1)

#二维列表
a = [["北京大学","清华大学"],["浙江大学"]]
print(a[1][0])
