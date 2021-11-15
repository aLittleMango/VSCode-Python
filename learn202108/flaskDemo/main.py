'''
Description:补充的学习的例子 
Author: aLittleMango
Date: 2021-08-03 11:23:37
LastEditTime: 2021-08-03 20:30:45
FilePath: \VSCode-Python\flaskDemo\main.py
'''


from flask import Flask,render_template,request
import datetime

app = Flask(__name__)

#路由解析，通过用户访问的路径，匹配相应的函数
# @app.route("/") 
# def hello_world():
#     return "你好!"
@app.route("/user/<name>")
def welcome(name):
    return "你好,%s"%name

#此外，还有float类型
@app.route("/user/<int:id>") 
def welcome2(id):
    return "你好,%d 号的会员"%id

#返回给用户渲染后的网页文件
#向页面传递一个变量
@app.route("/")
def index2():
    time = datetime.date.today()  #普通变量
    name = ['小张','小王','小赵']  #列表类型
    task = {"任务":"打扫卫生","时间":"3小时"} #字典类型
    return render_template("index.html",var = time,list = name,task = task)

#表单提交
@app.route('/test/register')
def register():
    return render_template('test/register.html')

#接收表单提交的路由，需要指定method
@app.route('/result',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("test/result.html",result=result)


if __name__ == '__main__':
    #debug 模式开始
    app.run(debug = True)
    