#-*- coding: utf-8 -*-
from django_micro import route, run, configure
from django.http import HttpRequest, HttpResponse
import web_page
import random, string

DEBUG = True

configure(locals())
# dump data
redeems = []
for i in range(9):
    code = ''
    for i in range(8):
        code += random.choice(string.ascii_letters)
    redeems.append(code)

ai_suggests = [
    "www.a.com",
    "www.b.com",
    "www.c.com",
]


@route("home")
def index(requests: HttpRequest):
    print(redeems)
    # 打印 redeems 应该放在这里，这样会在进入http://127.0.0.1:8000/home页面之后再生成码，只生成一次
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
