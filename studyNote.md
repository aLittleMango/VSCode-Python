# studyNote

date：7月15日

主题：python爬虫和数据可视化

学习内容：

1. 基础知识
2. 网络爬虫的技术实现
3. 数据可视化的技术应用

## 一.python基础知识

### 1.1 认识python

ctrl+/ 注释

- python是一门解释性、面向对象的高级编程语言
- python是开源免费的、支持交互式、可跨平台移植的脚本语言

优点：开源、易于维护；可移植；易于使用、简单优雅；广泛的标准库、功能强大；可扩展、可嵌入（单片机

缺点：

1. 运行速度慢（解释型语言 运行时先翻译为机器码），超大型项目会体现出来
2. 代码不能加密

典型应用：自动化脚本；web开发；科学计算；服务器软件；人工智能 网络爬虫

python版本：cmd 输入python 进入了python环境

**变量及类型：**

- 变量可以是任意的数据类型
- 变量名必须是大小写英文、数字和下划线的组合，不能以数字开头

**标识符和关键字：**

- 查看关键字

  ```python
  >>> import keyword
  >>> keyword.kwlist
  ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 
  'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
  ```

**格式化输出**

| %c   | 字符串                      |
| ---- | --------------------------- |
| %s   | 通过str()字符串转换来格式化 |
| %d   | 有符号十进制整数            |
| \t   | 空格                        |
| \n   | 换行                        |

**输入**

- 注意输入的数据类型

**运算符和表达式**

### 1.2 判断语句和循环语句

#### a. 条件判断IF

条件判断

- true：非0和非空值；False：0或者None
- elif和else要一起用

【简洁优雅】通过缩进的方式表达代码段属于哪一块

**导入相应的模块**：

- import 或者 from...import
- from somemodule import firstfunc, secondfunc,...
- ```from somemodule import  \*```

**课堂练习1：**

实现[Rock] [Paper] [Scissors]

```
input:
Please enter: Scissors (0), Rock (1), Paper (2) :  
output:  
Your input is: scissors (0)  
The randomly generated number is: 1  
Haha, you lost  
```

#### b.循环语句for while

python中循环有两种，一种是for...in循环，另一种是while

**课堂练习2：**

计算1~100的和

#### c. break continue pass

break 可以跳出 for 和 while的循环体

continue 跳出当前循环，直接进行下一轮循环

pass 是空语句 一般用作占位语句，不做任何事

**课堂练习3：**

打印九九乘法表

### 1.3 字符串、列表、元组、字典

#### a. String

- 可用单引号、双引号和三引号[可以保留段落格式]括起来，用放斜杠 \ 表示转义特殊字符 

| \\\\       | 反斜杠符号    |
| ---------- | ------------- |
| \\\'  \\'' | 单引号 双引号 |
| \n         | 换行          |
| \t         | 制表符        |

- 默认UTF-8编码，所有字符串都是Unicode字符串
- 可以用+ 表示拼接，* 乘也可以
- 当加r在前面，转义字符无效
- 字符串常见操作：

| bytes.decode(encoding ='UTF-8',errors='strict') | 以encoding指定的编码格式编码字符串，如果出错默认报异常       |
| ----------------------------------------------- | ------------------------------------------------------------ |
| isalnum()                                       | 如果字符串至少有一个字符并且所有字符都是字母或数字，则返回True |
| isalpha()                                       | 如果字符串至少有一个字符并且所有字符都是字母，则返回True     |
| isdigit()                                       | 如果字符串只包含数字则返回True                               |
| isnumeric()                                     | 如果字符串只包含数字字符则返回True                           |
| join(seq)                                       | 以指定字符串作为分隔符，将seq中所有的元素合并为一个新的字符串 |
| lstrip()                                        | 截掉字符串左边的空格或指定字符                               |

#### b. List 列表★★★

- 列表可以存储多种类型混合在一起
- 以0为开始值，-1为从末尾开始的位置
- 列表的常用操作：

| 操作名称                                               | 操作方法                 | 举例                 |
| ------------------------------------------------------ | ------------------------ | -------------------- |
| 访问list中的元素                                       | 下标访问                 | lsit1[0]             |
| 列表的切片                                             | 使用[::]                 | list1[0:3:2]         |
| 遍历列表                                               | 通过for循环              | for i in list1:      |
| 【增1】增加一个列表元素                                | append                   | list1.append(5)      |
| 【增2】逐一增加每个元素                                | extend                   | list1.extend(list2)  |
| 【增3】列表数据插入，（下标，对象）                    | insert                   | list1.insert(1,3)    |
| 【删1】删除列表中的指定位置的元素                      | del                      | del list1[1]         |
| 【删2】删除/弹出末尾最后一个元素                       | pop                      | list1.pop()          |
| 【删3】直接删除指定位置的元素（第一个）                | remove                   | list1.remove()       |
| 【改】修改指定下标的元素内容                           | list1[4]="abc"           |                      |
| 【查】查找在或者不在                                   | in, not in               | if list2 in list1:   |
| 【查】在范围内[左闭右开]查找指定的元素内容，返回下标值 | index                    | list1.index("a",1,4) |
| 【查】统计某个元素出现几次                             | count                    | list1.count("a ")    |
| 将列表所有元素反转                                     | reverse                  | list1.reverse()      |
| 升序                                                   | sort                     | list1.sort()         |
| 降序                                                   | list1.sort(reverse=True) |                      |

```python
for i,x in enumerate(mylist):

	print(i,x)
```

**课堂练习4：打印购物车**

#### c. tuple 元组

- 元祖与列表类似，不同之处在于tuple的元素不能修改
- 元组的元素不可变，但可以包含可变对象，如list
- 定义一个只有1个元素的tuple，必须加逗号
- 不能修改，删除是删除了整个元组变量
- 可以新增（连接），用+

#### d. dict 字典★★★

- 字典是无序的对象集合，使用键值对（key-value）存储，具有很快的查找速度
- key必须使用不可变连续
- key是唯一的

```python
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
```

#### e. set 集合

- 集合和字典类似，也是key的集合，但不存储value
- set是无序的，重复元素在set中自动被过滤

### 1.4 函数

- 需要某块代码多次，为了提高编写的效率以及代码的重用，因此把具有独立功能的代码块组织为一个模块，这就是函数

函数的定义和调用

全局变量和局部变量 global 

### 1.5 文件操作

- 文件就是把一些数据存放起来，省时省力

| r      | 默认模式，以只读方式打开文件，文件指针在文件的开头           |
| ------ | ------------------------------------------------------------ |
| **w**  | 打开一个文件用于写入，如果该文件已经存在则将其覆盖，如果不存在则创建新文件 |
| a      | 打开一个文件用于追加                                         |
| **rb** | 二进制只读                                                   |
| **wb** | 二进制写入                                                   |

文件的相关操作d

文件重命名

```python
import os 
os.rename("test1.txt","test2.txt")
```

删除文件

```python
import os 
os.remove("test1.txt")
```

### 1.6 错误与异常

- 异常：如 打开一个不存在的文件

**课堂练习5：文件操作+函数**

![image-20210722154632091](C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20210722154632091.png)

## 二、Python爬虫

### 1. 任务介绍

> 爬取豆瓣电影tpo250的基本信息，https://movie.douban.com/top250
>
> 包括电影的 名称、豆瓣得分、评价数、电影概况、电影链接等

### 2. 爬虫初识

网络爬虫，是按照**一定规则**，**自动抓取**互联网信息的程序或者脚本。能通过浏览器访问的数据都可以通过爬虫获取。

蜘蛛从索引区出发爬取网页，将爬取到的网页存放到临时库中进行处理，临时库符合规则就进入索引区，在索引区中进行分类、归档、排序，然后将结果反馈给用户。

### 3. 基本流程

$\bigstar$​ ​**准备工作**

通过浏览器查看分析目标网页，学习编程基础规范

$\bigstar$ **获取数据**

通过http库向目标站点发起请求，请求可以包含额外的header等信息，如果服务器能正常响应，会得到一个response，便是索要获取的页面内容

$\bigstar$ **解析内容**

得到的内容可能是html、json等格式，可以用页面解析库、正则表达式等进行解析

$\bigstar$ **保存数据**

保存形式多样，可以存为文本，也可以保存到数据库，或者保存特定格式的文件

#### a.准备工作

`https://movie.douban.com/top250?start=100&filter=`

页面包括250条数据，每页25条，start=0,25,50...225

F12进入开发者模式，左上角箭头小标题

当你在凝视深渊时，深渊也在凝视你

user-agent ：表明我们是什么版本的浏览器

cookie：很重要，爬取登录以后操作的信息

**编码规范：**

1、一般python程序中第一行需要加入 `-*-coding: utf-8-*-或者coding =utf-8`

2、多用函数 def，提高可读性和代码重复利用率

3、加入main函数用于测试程序 `if __name__ == "__main__":`

**引入模块：**

模块 module ：用来从逻辑上组织python代码（变量、函数、类），本质就是py文件，提高代码的可维护性

VScode中要将模块放在相同文件夹下

```python
import urllib.request,urllib.error #制定url，获取网页数据
from bs4 import BeautifulSoup #网页解析，获取数据
import re #正则表达式，进行文字匹配
import xlwt #进行excel操作
import sqlite3 #进行SQLite数据库操作
```

- 下载库要进入到3.9版本的Scripts

<img src="C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20210728150808970.png" alt="image-20210728150808970" style="zoom:67%;" />

```python
def main():
#1.爬取网页
    base_url = "https://movie.douban.com/top250?start="

    datalist = get_Data(base_url)
    save_path = ".\\豆瓣电影TPO250.xls"

#2.解析数据
def get_Data(base_url):
    datalist = []
    #逐一解析数据
    return datalist

 #3.保存数据
def save_Data(save_path):
    print("save...")

if __name__ == "__main__": #当程序执行时
#调用函数    
    main()
```

#### b. 获取数据

- 扩展内容：urllib

http://httpbin.org/

获取get请求

获取post请求

超时处理

当`response.status` 为418时，对方已经发现你在爬虫

#### c. 解析内容

- 扩展内容bs4

文档搜索、文档遍历

- 扩展内容 re模块

| 操作符 | 说明                             | 实例                                    |
| ------ | -------------------------------- | --------------------------------------- |
| .      | 表示任何单个字符                 |                                         |
| [ ]    | 字符集，对单个字符给出的取值范围 | [abc]表示a、b、c，[a-z]表示a到z单个字符 |
| [^ ]   | 非字符集，对单个字符给出排除范围 | [^abc]表示非a或b或c的单个字符           |
| *      | 前一个字符0次或者无限次扩展      | abc* 表示ab、abc、abccc等               |
| +      | 前一个字符1次或者无限次扩展      | abc+ 表示 abc、abccccc等                |
| ?      | 前一个字符0次或者1次扩展         | abc？表示ab、abc                        |
| \|     | 左右表达式任意一个               | abc\|def 表示abc、def                   |
| {m}    | 扩展前一个字符m次                | ab{2}c 表示abbc                         |
| {m,n}  | 扩展前一个字符m至n次（含n）      | ab{1，2}c 表达abc、abbc                 |
| ^      | 匹配字符串开头                   | ^abc 表示abc且在一个字符串的开头        |
| $      | 匹配字符串结尾                   | abc$ 表示abc且在一个字符串的结尾        |
| ( )    | 分组标记，内部只能使用\|操作符   |                                         |
| \d     | 数字，等价于[0-9]                |                                         |
| \w     | 单词字符，等价于[A-Z a-z 0-9]    |                                         |

re库主要功能函数

| 函数              | 说明                                                         |
| ----------------- | ------------------------------------------------------------ |
| **re.search( )**  | 扫描整个字符串并返回第一个成功的匹配                         |
| **re.match( )**   | 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none |
| **re.findall( )** | 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表 |
| re.split( )       | 将一个字符串按照正则表达式匹配结果进行分割，返回列表类型     |
| re.finditer( )    | 和findall类似，在字符串中找到正则表达式所匹配的所有子串，并返回一个迭代器，每个迭代元素是match对象 |
| **re.sub( )**     | 在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串 |

控制匹配模式

| 修饰符 | 描述                                             |
| ------ | ------------------------------------------------ |
| re.l   | 使匹配对大小写不敏感                             |
| re.L   | 做本地化识别（locale-aware）匹配                 |
| re.M   | 多行匹配，影响 ^ 和 $                            |
| re.S   | 使.匹配包括换行在内的所有字符                    |
| re.U   | 根据Unicode字符集解析字符                        |
| re.X   | 给予你更灵活的格式以便将正则表达式写得更易于理解 |

对爬取的htm文件解析解析

**标签解析**

<img src="C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20210729105242932.png" alt="image-20210729105242932" style="zoom:67%;" />

**正则提取**

```python
findLink = re.compile(r'<a href="(.*?)">')  #影片详情链接
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S) #影片的图片
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*)</p>',re.S)
```

#### d.保存数据

excel表储存

![image-20210729171949100](C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20210729171949100.png)

sqlite3 数据库保存

# 三、数据可视化

## 1.Flask入门

- flask 是一个轻量级的web 应用程序开发 Python 框架,
- http请求，访问
- flask框架的核心就是werkzeug和jinja2包装响应 

为了避免重复造轮子（稍微了解一下就行

**flask补充知识**

- 路由路径不能重复，用户通过唯一路径访问特定的函数
- render_template 渲染模板
- html代码

iconfont

## 2.Echarts应用

- 开源的图标框架，需要先下载echarts.min.js文件

官网下载就可以用 > 五分钟快速上手



## 3.WordCloud应用

- 词云，图片显示字词

## 4.项目说明

