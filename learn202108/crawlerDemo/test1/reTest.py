'''
Description: 
Author: aLittleMango
Date: 2021-07-29 09:53:58
LastEditTime: 2021-07-30 10:16:14
FilePath: \VSCode-Python\crawlerDemo\test1\reTest.py
'''

import re

# #创建模式对象
# pat = re.compile("AA")
# m = pat.search("CBAA")
# print(m)

# #没有模式对象
# m = re.search("ASD","ASDD") #前面的字符是规则（模板），后面的字符串是被校验的对象
# print(m)

# print(re.findall("[A-Z]+", "1bbaABa"))

# print(re.sub("a", "A", "aaaAAA")) #在string中找到pattern用repl代替

# #建议在正则表达式中，被比较的字符串前面加上r，不用担心转义字符的问题
# a = r"\a\t\c\n"
# print(a)

str = ('<p class=""> \
                            导演: 弗兰克·德拉邦特 Frank Darabont   主演: 蒂姆·罗宾斯 Tim Robbins /...<br/> \
                            1994 / 美国 / 犯罪 剧情 \
                        </p>')
bd_dir = re.compile("导演: (.*)主演")
bd_actor = re.compile("主演: (.*) [0-9]")
bd_year = re.findall("[0-9]+",str)
bd_country = re.compile("[0-9] / (.*) / ")
bd_type = re.compile("[0-9] / .* / (.*)")
print(re.findall(bd_dir,str))
print(re.findall(bd_actor,str))
print(bd_year)
print(re.findall(bd_country,str))
print(re.findall(bd_type,str))

            
             
