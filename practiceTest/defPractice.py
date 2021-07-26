'''
Description: 
Author: aLittleMango
Date: 2021-07-22 09:41:22
LastEditTime: 2021-07-22 09:48:51
FilePath: \VSCode-Python\practiceTest\defPractice.py
'''


def printInfo(num):
    print("-"*num)

user_num = input("请输入数字：")
printInfo(int(user_num))

def sum_three(num1,num2,num3):
    return num1+num2+num3

print(sum_three(1,1,1))


def sum_average(num1,num2,num3):
    return sum_three(num1,num2,num3)/3

print(sum_average(2,2,1)) 