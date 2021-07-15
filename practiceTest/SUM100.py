'''
Description: 1-100求和
Author: aLittleMango
Date: 2021-07-16 14:32:46
LastEditTime: 2021-07-16 17:47:28
FilePath: \VSCode-Python\practiceTest\SUM100.py
'''
import time

start1 = time.time()
sum_1 = 0
i = 1
while i < 1001:
    sum_1 += i
    i += 1
print("1-100的求和为：%d" % (sum_1))

end1 = time.time()
print("The runtime of while is:%.10fs"%(end1-start1))

start2 = time.time()
sum_2 = 0
for i in range(1, 1001):
    sum_2 += i
print("1-100的求和为：%d" % (sum_2))
end2 = time.time()
print("The runtime of for is:%.10fs"%(end2-start2))