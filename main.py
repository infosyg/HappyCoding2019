#-*- coding: utf-8 -*-
# from django_micro import configure, route, run
# from django.http import HttpResponse
#
# DEBUG = True
# limit = 10
#
# configure(locals())
#
# @route('', name='home')
# def homepage(request):
#     global limit
#     limit = limit - 1
#     limit2 = 10-limit
#     html = f'''
#     <div style="background-color:#77DFF5;height:100%">
# 		<h1 style="color:white;text-align:center">It's your {limit2  } times visit~ </h1>
#         <h1 style="color:white;text-align:center">You have { limit } times left~ </h1>
#         <image src="https://file-geieweypjd.now.sh/" style="margin:auto;display:block">
#     </div>
#     '''
#     print(limit)
#     if limit > 0:
#         return HttpResponse(html)
#     else:
#         return HttpResponse("haha can't touch this")
#
# application = run()

user_input = ""
# another_thing = False
if user_input:
    print("hello")
elif user_input.startswith("1"):
    print("we got 1 ")
elif user_input.endswith("2"):
    print("we got 2")
# else:
#     print("nothing")
