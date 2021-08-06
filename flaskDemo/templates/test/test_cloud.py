'''
Description: 
Author: aLittleMango
Date: 2021-08-05 14:24:46
LastEditTime: 2021-08-06 15:04:52
FilePath: \VSCode-Python\flaskDemo\templates\test\test_cloud.py
'''

import jieba #分词
from matplotlib import pyplot as plt  #绘图，数据可视化
from wordcloud import WordCloud #词云
from PIL import Image #图片处理
import numpy as np #矩阵运算
import sqlite3 #数据库

con = sqlite3.connect("movie.db")
cur = con.cursor()
sql = 'select intro from movie250'
data = cur.execute(sql)
text = ""
#把词都连接起来
for item in data:
    text = text +item[0]
cur.close()
con.close()

#分词
cut = jieba.cut(text)
str = " ".join(cut)

# 导入停词，用于去掉文本中类似于'啊'、'你'，'我'之类的词

stop_words = open(r"F:\VSCode-Python\flaskDemo\stopword.txt","r",encoding="utf-8").read().split(" ")

# 使用WordCloud生成词云

img = Image.open(r'flaskDemo\static\assets\img\tree.jpg') #打开遮罩图片
img_array = np.array(img) #将图片转换为数组
cloud = WordCloud(
    background_color = 'white',
    mask = img_array, 
    font_path='C:\Windows\Fonts\msyh.ttc',
    stopwords= stop_words
)
cloud.generate_from_text(str)

#绘制图片
fig = plt.figure(1)
plt.imshow(cloud)
plt.axis('off') #是否显示坐标轴

#plt.show() #显示生成的词云图片

plt.savefig(r'flaskDemo\static\assets\img\word.jpg',dpi = 500)



