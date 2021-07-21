'''
Description: 
Author: aLittleMango
Date: 2021-07-21 15:19:29
LastEditTime: 2021-07-21 16:04:48
FilePath: \VSCode-Python\learnTest\DictDemo.py
'''


info = {"name":"小郭","age":21}

print(info["name"])

print(info.get("num","m"))  #找对应的键，默认返回None,也可以设定默认值

#增
info["lover"]="小红"
print(info["lover"])
#改
info["age"]=22
print(info["age"])
#查找
print(info.keys()) #得到所有的键（列表）
print(info.values()) #得到所有的值（列表）
print(info.items()) #得到所有的项（列表），每一个键值对是一个元组
#遍历所有的值
for key,value in info.items():
    print("key = %s , value = %s "%(key,value))
#删
print("删除前：%s"%info["name"])
del info["name"]
print("删除后：%s"%info.get("name"))
#清空
print("清空前: %s"%info)
info.clear()
print("清空后：%s"%info)
