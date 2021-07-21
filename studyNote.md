# studyNote

date：7月15日

主题：python爬虫和数据可视化

学习内容：

1. 基础知识
2. 网络爬虫的技术实现
3. 数据可视化的技术应用

## 1.python基础知识

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

for i,x in enumerate(mylist):

​	print(i,x)

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







### 1.5 文件操作







### 1.6 错误与异常







