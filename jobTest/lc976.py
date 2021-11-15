'''
Description: 
给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
如果不能形成任何面积不为零的三角形，返回 0。

本质是排序
如果相邻的两个数都不能比第三个数大，那最大数直接抛弃
Author: aLittleMango
Date: 2021-10-29 09:52:19
LastEditTime: 2021-10-29 10:21:40
FilePath: \VSCode-Python\jobTest\lc976.py
'''



class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for i in range(len(A)-2):
            if A[i]<A[i+1]+A[i+2]:
                return A[i]+A[i+1]+A[i+2]
        return 0
