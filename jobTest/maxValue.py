'''
Description: 请设计算法完成如下功能，对于输入的整数数组，返回组合最大的结果
Author: aLittleMango
Date: 2021-10-24 09:57:42
LastEditTime: 2021-10-24 10:15:47
FilePath: \VSCode-Python\practiceTest\maxValue.py
'''

def max_value(lt):
    m = len(lt)
    for i in range(m-1):
        for j in range(m-1-i):
            if str(lt[j])+str(lt[j+1]) < str(lt[j+1])+str(lt[j]):
                lt[j], lt[j+1] = lt[j+1], lt[j]
    temp = ''
    # 遍历排好序的列表
    for value in lt:
        temp += str(value)
    return int(temp)

n = eval(input("请输入一个数组："))
a = max_value(n)
print("组合最大的结果为%d"%(a))


