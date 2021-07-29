'''
Description: 
Author: aLittleMango
Date: 2021-07-28 15:33:34
LastEditTime: 2021-07-28 15:33:35
FilePath: /VSCode-Python/crawlerDemo/test1/urllibTest.py
'''

import urllib.request


# #获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8")) #对获取到的网页源码进行utf-8解码

# #获取一个post请求
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding ="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data = data)
# print(response.read().decode("utf-8"))

# #超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout = 3)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out")

# #获取信息的细节
# response = urllib.request.urlopen("http://httpbin.org/get",timeout = 3)
# print(response.status)
# print(response.getheader("Server"))

##伪装浏览器发送
# url = "http://httpbin.org/post"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding ="utf-8")
# req = urllib.request.Request(url=url, data = data, headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

url = "https://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
}
req = urllib.request.Request(url=url,headers=headers) #封装好的request对象去请求网址
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))