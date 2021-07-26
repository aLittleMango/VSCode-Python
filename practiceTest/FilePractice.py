'''
Description: 
Author: aLittleMango
Date: 2021-07-22 15:44:43
LastEditTime: 2021-07-22 17:17:22
FilePath: \VSCode-Python\practiceTest\FilePractice.py
'''

poem ="Two roads diverged in a yellow wood,\n\
And sorry I could not travel both\n\
And be one traveler,long I stood\n\
And looked down one as far as I could\n\
To where it bent in the undergrowth"

 #创建文件的函数
def file_def(name):
    f = open(name, "w")
    f.close()
 #读文件的函数
def file_read(name):
    f = open(name, "r")
    content = f.readlines() # 一次性读取全部文件为列表，每行一个字符串元素
    f.close()
    return content
#写文件的函数
def file_write(name,content):
    f = open(name,"w")
    for temp in content:
        f.write(temp)
    f.close()
#复制文件的函数
def file_copy(original,copy,poem):
    file_def(original)
    file_def(copy)
    file_write(original,poem)
    content = file_read(original)
    file_write(copy,content)
    print("复制完毕")
file_copy("gushi.txt", "copy.txt",poem)


