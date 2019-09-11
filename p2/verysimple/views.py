from django.http import HttpResponse

def index(request):
    return HttpResponse(open("./index.html"))
