'''
Description: 获取第n位的斐波那契数列
Author: aLittleMango
Date: 2021-10-24 09:42:16
LastEditTime: 2021-10-29 09:51:12
FilePath: \VSCode-Python\jobTest\fibs.py
'''

def fibs(n):
	temp = []
	a = 0
	b = 1
	temp.append(a)
	temp.append(b)
	while(1):
		a,b  = b,a+b
		temp.append(b)
		try:
			temp[n-1] 
			return temp[n-1]
		except:
			continue

n = eval(input("请输入一个整数："))
a = fibs(n)
print("第{}位斐波那契数列的值为：{}".format(n,a))








