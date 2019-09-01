#-*- coding: utf-8 -*-
from django_micro import route, run, configure
from django.http import HttpRequest, HttpResponse
import web_page
# web_page.py 这个文件中使用了第三方库 dominate，需安装，安装方式是在终端输入 pip install dominate
import random, string

DEBUG = True

configure(locals())
# dump data
redeems = []
for i in range(20):
    code = ""
    for i in range(12):
        code += random.choice(string.hexdigits)
    redeems.append(code)

ai_suggests = [
    "www.a.com",
    "www.b.com",
    "www.c.com",
]


@route("home")
def index(requests: HttpRequest):
    print(redeems)
    return HttpResponse(web_page.doc.render())


@route('result')
def get_code(requests: HttpRequest):
    code = requests.POST.get("code")
    if code in redeems:
        return HttpResponse("ok")
    else:
        #<li>www.a.com</li>
        # join()
        data = '<!-- dump data -->'.join("<li>" + i + "</li>" for i in ai_suggests)
        html = f'''
        <h1>Sorry but we bring you these</h1>
        <ul> { data } </ul>
        '''
        return HttpResponse(html)


app = run()
import sys
sys.path.extend(((())))