'''from django_micro import configure, route, run
from django.http import HttpResponse

DEBUG = True
configure(locals())


@route('', name='homepage')
def homepage(request):
    name = request.GET.get('name', 'World')
    return HttpResponse('Hello, {}!'.format(name))


application = run()'''

from django_micro import configure,route,run
from django.http import HttpResponse

DEBUG = True
limit = 10
html='''
<div style="background-color:#77DFF5;height:100%">
    <h1 style="color:white;text-align:center">Yeah~</h1>
    <image src="https://file-geieweypjd.now.sh/" style="margin:auto;display:block">
</div>

'''
configure(locals())
@route('', name='home')
def homepage(request):
    name = request.GET.get('name', 'world')
    return HttpResponse(html)
application = run()
