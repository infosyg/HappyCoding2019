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










