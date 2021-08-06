'''
Description: 
Author: aLittleMango
Date: 2021-08-03 20:30:32
LastEditTime: 2021-08-05 13:14:18
FilePath: \VSCode-Python\flaskDemo\app.py
'''
from flask import Flask,render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index')
def home():
    return index()

@app.route('/movie')
def movie():
    datalist = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("movie.html",movies = datalist)
    

@app.route('/score')
def score():
    score = []
    num = []
    country = []
    num2 = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql1 = "select score,count(score) from movie250 group by score"
    sql2 = "select year,count(year) from movie250 group by year"
    data = cur.execute(sql1)
    for item in data:
        score.append(item[0])
        num.append(item[1])

    data2 = cur.execute(sql2)
    for item2 in data2:
        country.append(item2[0])
        num2.append(item2[1])
    cur.close()
    con.close()
    return render_template("score.html",score = score,num = num,country = country,num2 = num2)

@app.route('/word')
def word():
    return render_template("word.html")

@app.route('/team')
def team():
    return render_template("team.html")

if __name__ == '__main__':
    app.run(debug = True)