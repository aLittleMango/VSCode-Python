'''
Description: 列表的练习
Author: aLittleMango
Date: 2021-07-21 12:00:39
LastEditTime: 2021-07-21 16:15:56
FilePath: \VSCode-Python\practiceTest\shoppingCart.py
'''

product = [['iphone',6888],['MacPro',14800],['小米6',2499],['Coffee',31],['Book',60],['Nike',699]]
print('-'*10+"商品列表"+'-'*10)
'''
for i in range(0,6):
    print("%s\t%s\t    %s"%(i,product[i][0],product[i][1]))
'''

for j,x in enumerate(product):
    print("%d\t%s\t    %s"%(j,x[0],x[1]))


shopping_cart = [] 
sum_money = 0

while 1:
    user_in = input("请问你需要买什么?输入商品编号(q为结账):")
    if user_in!="q" and 0 <= int(user_in) <= 5:
        user_in = int(user_in)
        shopping_cart.append(product[user_in][0])
        sum_money+=product[user_in][1]
    elif user_in == "q":
        print("你购买的商品有：")
        for i in shopping_cart:
            print(i,end = ", ")
        print('\b')
        print("一共%d元，谢谢光临！"%sum_money)
        break
    else:
        print("你输入的商品编码不存在，请重新输入：")


