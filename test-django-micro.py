'''from django_micro import configure, route, run
from django.http import HttpResponse

DEBUG = True
configure(locals())


@route('', name='homepage')
def homepage(request):
    name = request.GET.get('name', 'World')
    return HttpResponse('Hello, {}!'.format(name))


application = run()'''

# from django_micro import configure,route,run
# from django.http import HttpResponse
#
# DEBUG = True
# limit = 10
# html='''
# <div style="background-color:#77DFF5;height:100%">
#     <h1 style="color:white;text-align:center">Yeah~</h1>
#     <image src="https://file-geieweypjd.now.sh/" style="margin:auto;display:block">
# </div>
#
# '''
# configure(locals())
# @route('', name='home')
# def homepage(request):
#     name = request.GET.get('name', 'world')
#     return HttpResponse(html)
# application = run()



#正逆向捕捉的例子
# print("Your name below")
# user = input()
# print("Your password below")
# password = input()
# user_db = {
#     "Fin": "human"}
#
# if user in user_db:
#     print("your password below")
#     password = input()
#     if password == user_db.get(user):
#         print(f"wecome back{user}")
#     else:
#         print("user not exist or wrong password")
# else:
#     print("This account is not exist")

#条件表达式

# print("write your comment")
# post = input()
#
# if "@" in post:
#     print("invalid input")
# elif len(post) > 10:
#     print("comment cant less than 1 word more than 10 words")
# elif not post:
#     print("coment cant less than 1 word more than 10 words")
# else:
#     print(f"you said:{post}")
#
# #使用列表解析解决标点符号的问题
#     import string
#     print(string.punctuation)
#     print("write your comment")
#     post = input()
#     if any(p in post for p in string.punctuation):
#     ##(注释，之前的代码) if "@" in post:
#         print("Invalid input")
#     elif len(post) > 10:
#         print("comment cant less than 1 word more than 10 words")
#     elif not post:
#         print("comment cant less than 1 word more than 10 words")
#     else:
#         print(f"You said: { post }")


#三目运算
# x = int(input("输入第一个数："))
# y = int(input("输入第二个数："))
# z = int(input("输入第三个数："))
#
# #三目运算符的第一种写法
# print((x if (x>y) else y) if ((x if (x>y) else y)>z) else z)
# #三目运算符的第二种写法
# a=(x if (x>y) else y)
# print(a if (a>z) else z)
#
# #####################另一个三目运算例子
# a = 1
# b = 2
# h = ""
# h = a-b if a>b else a+b
# print(h)

#循环
# for i in range(21):
#     if i == 4:
#         continue
#     print(12/i)
#
import random
import string

#
# redeems = []
#
# for i in range(20):
#     code = ''
#     # print(code)
#     for j in range(8):
#         code += random.choice(string.ascii_letters)
#         # print(code)
#     redeems.append(code)
#     # print()
# print(redeems)
#
#
#

 #  函数
 # import requests as f #可以用as 修改原函数的名字
 # f.get()
 #

 # height = 10
 # tb = 2
 # ub = 3
 #
# def result(height=3,tb=2,ub=2):
#     return (tb+ub)*height * 1/2
#
# l = result()
#
# a = 1
# b = 2
#
#
# def do(first_int, second_int):
#     return first_int * second_int
#
#
# do(a, b)
# l = do
#
# print(l)
# #函数的类型推断trick ,有助于项目中减少出错的几率
# def example (head:str,butt:str):
#     if head.startswith('?'):
#         pass
#     head.startswith()
#     return head + butt

# 实现2018-01-11这种格式
# def formatter(num):
#     if 1 <= num <=9:
#         return f'0{num}'
#     return num
#
# def date_gen(m,d,y=2019):
#     m = formatter(m)
#     d  = formatter(d)
#     return f'{y}-{m}-{d}'
#
# print(date_gen(m=1,d=11,y=2018))

# 结果==87,a=12 这里的a只是变量赋给minus(a),传参到第一个位置
# def minus(c,a=99):
#     return a - c
# a = 12
# print(minus(a))

#让结果等于22
# def add_plus(a,*args,b=12):
#     return a  + sum(args) +b
# print(add_plus(1,2,3,4))
#
#

import datetime


def show_time(sep=":", use_24_hours=True, with_seconds=False):
    if use_24_hours and with_seconds:
        time = datetime.datetime.now().strftime(f"%H{ sep }%M{ sep }%S")
    elif use_24_hours:
        time = datetime.datetime.now().strftime(f"%H{ sep }%M")
    elif not use_24_hours and with_seconds:
        time = datetime.datetime.now().strftime(f"%I{ sep }%M{ sep }%S %p")
    elif not use_24_hours and not with_seconds:
        time = datetime.datetime.now().strftime(f"%I{ sep }%M %p")
    return time

def normal_time():
    return show_time(use_24_hours=False, sep=":")
print(normal_time())