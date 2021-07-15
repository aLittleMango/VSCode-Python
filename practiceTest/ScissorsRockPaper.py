'''
Description: 石头剪刀布游戏
Author: aLittleMango
Date: 2021-07-16 11:45:42
LastEditTime: 2021-07-16 14:15:32
FilePath: \VSCode-Python\practiceTest\ScissorsRockPaper.py
'''
import random


user_num = int(input("Please enter: Scissors (0), Rock (1), Paper (2) : "))
if user_num == 0:
    user_str = "Scissors"
elif user_num == 1:
    user_str = "Rock"
else:
    user_str = "Paper"
print("Your input is: %s(%d)"%(user_str,user_num))

x =random.randint(0,2)
if x == 0:
    x_str = "Scissors"
elif x == 1:
    x_str = "Rock"
else:
    x_str = "Paper"
print("The randomly generated number is: %s(%d)"%(x_str,x))


if  (user_num == 0 & x ==2) or (user_num ==1 & x ==0) or (user_num==2 & x ==1):
    print("congratulation, you win!")
elif (user_num==x):
    print("what a coincidence!")
else:
    print("haha, you lost!")