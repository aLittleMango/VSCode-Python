'''
Description: 
Author: aLittleMango
Date: 2021-07-28 15:16:32
LastEditTime: 2021-07-30 17:06:07
FilePath: \VSCode-Python\crawlerDemo\spider.py
'''

import sqlite3
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import re
import xlwt


def main():
    base_url = "https://movie.douban.com/top250?start="
    datalist = get_Data(base_url)
    # #保存到xls
    # save_path = ".\\豆瓣电影TPO250.xls"
    # save_Data(datalist,save_path)
    
    #保存到数据库
    dbpath = "movie.db"
    save_Data2DB(datalist, dbpath)


#全局变量
findLink = re.compile(r'<a href="(.*?)">')  #影片详情链接
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  #影片的图片
findTitle = re.compile(r'<span class="title">(.*?)</span>')
findRating = re.compile(
    r'<span class="rating_num" property="v:average">(.*)</span> <span content',
    re.S)
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')  #影片概述
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)  #影片其他信息
findDir = re.compile(r'导演: (.*)主演')  #导演
findActor = re.compile(r'主演: (.*).<br/>', re.S)  #主演
findYear = re.compile(r'<br/> ([0-9]+) ', re.S)  #年份
findCountry = re.compile(r'[0-9] / (.*) / ')  #国家
findType = re.compile(r'[0-9] / .* / (.*)</p> <div class="star">')


#1.爬取网页
def get_Data(base_url):
    datalist = []
    for i in range(0, 10):  #获取页面信息，10页250个 #先只打印一页
        url = base_url + str(i * 25)
        html = ask_URL(url)  #保存获取到的网页源码

        #2.解析数据  逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  #查找符合要求的字符串
            data = []  #保存一部电影的所有信息
            item = str(item)
            item = ' '.join(item.split())

            # print(item)
            # break
            link = re.findall(findLink, item)[0]  #re库用来通过正则表达式查找指定的字符串
            data.append(link)
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)
            titles = re.findall(findTitle, item)
            if (len(titles) == 2):  #添加z中文名和外国名
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")  #去掉无关的符号
                otitle = re.sub("\xa0", "", otitle)  #去掉
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(" ")  #如果没有，外文名留空

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append(" ")

            dir = re.findall(findDir, item)
            if len(dir) != 0:
                dir = dir[0].replace("。", "")
                data.append(dir)
            else:
                data.append(" ")

            actor = re.findall(findActor, item)
            if len(actor) != 0:
                actor = actor[0].replace("。", "")
                data.append(actor)
            else:
                data.append(" ")

            year = re.findall(findYear, item)
            if len(year) != 0:
                year = year[0].replace("。", "")
                data.append(year)
            else:
                data.append(" ")

            country = re.findall(findCountry, item)
            if len(country) != 0:
                country = country[0].replace("。", "")
                data.append(country)
            else:
                data.append(" ")

            type = re.findall(findType, item)
            if len(type) != 0:
                type = type[0].replace("。", "")
                data.append(type)
            else:
                data.append(" ")

            # type = re.findall(findType,item)[0]
            # data.append(type)

            datalist.append(data)

    return datalist


#得到指定一个URL的网页内容
def ask_URL(url):
    head = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
    }  #作用：伪装，发送请求时让服务器端认为我是浏览器而不是爬虫
    req = urllib.request.Request(url=url, headers=head)  #封装好的request对象去请求网址
    html = ""
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


#3.保存数据
def save_Data(datalist, save_path):
    print("save...")
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('豆瓣电影top250')
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外国名", "评分", "评价数", "概况", "导演", "主演",
           "年份", "国家", "类型")
    for i in range(0, 12):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 12):
            sheet.write(i + 1, j, data[j])
    book.save('Test.xls')


def save_Data2DB(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in datalist: 
        for index in range(len(data)):
            if index == 4 or index == 5 or index == 9:
                continue
            data[index] = '"'+data[index]+'"'
        sql = '''
                insert into movie250
                (info_link,pic_link,cname,ename,score,rate,intro,director,actor,year,country,type)
                values(%s)'''%",".join(data)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()

    print("保存成功")


def init_db(dbpath):
    #创建数据表
    sql = '''
        create table movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rate numeric,
        intro text,
        director text,
        actor text,
        year char,
        country text,
        type text
        );
    '''
    #创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":  #当程序执行时
    #调用函数
    main()
