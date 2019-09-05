from django_micro import route, run, configure
from django.http import HttpRequest, HttpResponse
import web_page
import random, string

DEBUG = True

configure(locals())
redeems = []
for i in range(20):
    code = ''
    for i in range(12):
        code += random.choice(string.ascii_letters+string.digits)
    redeems.append(code)

@route("home")
def index(requests: HttpRequest):
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
        <h1>Sorry, this reedem is not avaliable</h1>
        '''
        return HttpResponse(html)


app = run()