'''
Description: 
Author: aLittleMango
Date: 2021-07-28 17:42:06
LastEditTime: 2021-07-29 09:01:57
FilePath: \VSCode-Python\crawlerDemo\test1\bs4Test.py
'''

# BeautifulSoup4将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:

# （1）Tag 通俗点讲就是HTML中的一个个标签以及其内容，默认拿到找到的第一个内容
# （2）NavigableString 获取标签内部的文字用 .string 即可
# （3）BeautifulSoup 表示的是一个文档的内容
# （4）Comment 表示的是一个文档的内容

from bs4 import BeautifulSoup
import re

file = open("F:\\VSCode-Python\\crawlerDemo\\baidu.html", "rb")

html = file.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")

print(bs.title) #(1)
print(bs.title.string) #(2)

print(bs.name) #(3)
print(bs)

print(bs.a.string)
#文档的遍历
#获取tag的所有子节点，返回一个list
print(bs.head.contents)
print(bs.head.contents[3])

#文档的搜索
#(1) find_all()
t_list = bs.find_all("a")
print(t_list)

#(2) 正则表达式搜索：使用search()方法来匹配内容
t_list = bs.find_all(re.compile("a"))
print(t_list)


#(3.1) 传入一个函数（方法），根据函数的要求来搜索
def name_is_exists(tag):
    return tag.has_attr("name")


t_list = bs.find_all(name_is_exists)
for item in t_list:
    print(item)

#(3.2) kwargs 参数
t_list = bs.find_all(id = "head")
for item in t_list:
    print(item)

t_list = bs.find_all(href="http://news.baidu.com")
for item in t_list:
    print(item)

#(3.3) text参数
t_list = bs.find_all(text = ["hao123","地图"])
for item in t_list:
    print(item)

#(3.4) limit参数
t_list = bs.find_all("a", limit=3)
for item in t_list:
    print(item)

#(4) css选择器
t_list = bs.select("title") #通过标签来查找

for item in t_list:
    print(item)