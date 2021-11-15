'''
Description: 
Author: aLittleMango
Date: 2021-07-29 15:53:24
LastEditTime: 2021-07-30 11:13:13
FilePath: \VSCode-Python\crawlerDemo\test1\sqliteTest.py
'''

import sqlite3

#1.链接数据库
conn = sqlite3.connect('test.db')

print("Opened database successfully")

c = conn.cursor() #获取游标

#2.创建数据表
sql = '''
    create table company
        (id int primary key not null,
        name next not null,
        age int not null,
        address char(50),
        salary real);
'''
c.execute(sql) #执行sql语句

#3.插入数据
sql1 = '''
    insert into company (id,name,age,address,salary)
    values(1,'张三',32,'成都',8000);
'''

sql2 = '''
    insert into company (id,name,age,address,salary)
    values(2,'李四',22,'北京',6000);
'''
c.execute(sql1)
c.execute(sql2)
print("插入数据完毕")
conn.commit() #提交数据库操作
conn.close() #关闭数据库链接
#4. 查询数据库
sql = "select id,name,address,salary from company"
cursor=c.execute(sql)
for row in cursor:
    print("id = ",row[0])
    print("name = ",row[1])
    print("address = ",row[2])
    print("salary = ",row[3],"\n")

conn.close() #关闭数据库链接


print("查询完毕")
