'''
Description: 
Author: aLittleMango
Date: 2021-07-28 09:22:50
LastEditTime: 2021-07-28 14:43:24
FilePath: \VSCode-Python\crawlerDemo\moduleDemo.py
'''

#-*-coding: utf-8-*-

# import sys
# sys.path.append("F:/VSCode-Python/crawlerDemo/test1")
# import t1

from test1 import t1  #引入自定义的模块
t1.printInfo()

import sys,os #引入系统的模块

#引入第三方模块
import urllib.request,urllib.error #制定url，获取网页数据
from bs4 import BeautifulSoup #网页解析，获取数据
import re #正则表达式，进行文字匹配
import xlwt #进行excel操作
import sqlite3 #进行SQLite数据库操作

