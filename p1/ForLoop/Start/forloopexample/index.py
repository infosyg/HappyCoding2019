#-*- coding: utf-8 -*-
from django_micro import route, run, configure
from django.http import HttpRequest, HttpResponse
import web_page


# web_page.py 这个文件中使用了第三方库 dominate，需安装，安装方式是在终端输入 pip install dominate

DEBUG = True

configure(locals())

redeems = ['RRMNDiqkT',
           'ABUkKrEXE',
           'UeLRwjmBq',
           'FaZHYFFpr',
           'yEcDvixGW',
           'WvwyVtMLk',
           'NQYnQAVDu',
           'kwBpUMrIc']


@route("home")
def index(requests:HttpRequest):
    return HttpResponse(web_page.doc.render())

@route('result')
def get_code(requests:HttpRequest):
    code = requests.POST.get("code")
    if code in redeems:
        return HttpResponse("ok")
    else:
        return HttpResponse("wrong")


app = run()
