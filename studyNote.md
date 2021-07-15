# studyNote

date：7月15日

主题：python爬虫和数据可视化

学习内容：

1. 基础知识
2. 网络爬虫的技术实现
3. 数据可视化的技术应用

## 1.python基础知识

### 1.1 认识python

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

#### b.循环语句for

python中循环有两种，一种是for...in循环，另一种是while

break 可以跳出 for 和 while的循环体

continue 跳出当前循环，直接进行下一轮循环

pass 是空语句 一般用作占位语句，不做任何事



### 1.3 字符串、列表、元组、字典



### 1.4 函数



### 1.5 文件操作







### 1.6 错误与异常







