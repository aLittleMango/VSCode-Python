'''
Description: 
Author: aLittleMango
Date: 2021-07-28 15:16:32
LastEditTime: 2021-07-28 15:16:33
FilePath: \VSCode-Python\crawlerDemo\spider.py
'''
import urllib.request,urllib.error
def main():

    base_url = "https://movie.douban.com/top250?start="

    datalist = get_Data(base_url)
    save_path = ".\\豆瓣电影TPO250.xls"

    print(ask_URL("https://movie.douban.com/top250?start=0"))


#1.爬取网页
def get_Data(base_url):
    datalist = []
    for i in range(0,10):   #获取页面信息，10页250个
        url = base_url +str(i*25)
        html = ask_URL(url)  #保存获取到的网页源码

    #2.解析数据
    #逐一解析数据
    return datalist


#得到指定一个URL的网页内容
def ask_URL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
    } #作用：伪装，发送请求时让服务器端认为我是浏览器而不是爬虫
    req = urllib.request.Request(url=url,headers=head) #封装好的request对象去请求网址
    html = ""
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html


 #3.保存数据
def save_Data(save_path):
    print("save...")

if __name__ == "__main__": #当程序执行时
#调用函数    
    main()
