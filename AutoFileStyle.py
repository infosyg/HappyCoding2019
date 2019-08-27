from django_micro import configure, route, run
from django.http import HttpResponse

DEBUG = True
configure(locals())


@route('', name='homepage')
def homepage(request):
    name = request.GET.get('name', 'World')
    return HttpResponse('Hello, {}!'.format(name))


application = run()


