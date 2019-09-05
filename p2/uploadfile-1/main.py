from django_micro import route, run, configure
from django.http import HttpRequest, HttpResponse, FileResponse
import dominate.tags as dom
from dominate.document import document
from PIL import Image

DEBUG = True
configure(locals())

def page():
    doc = document()
    with doc as root:
        with doc.body:
            with dom.form(action="/file",method="post",enctype="multipart/form-data"):
                dom.input(type="file",name="image")
                dom.button("submit",type="submit")

    return root.render()

@route('')
def index(request: HttpRequest):
    return HttpResponse(page())

@route('file')
def filehandler(request:HttpRequest):
    user_image = request.FILES.get("image")
    img = Image.open(user_image)
    img.save(f"{user_image.name}",optimize=True,quality=70)
    resp = FileResponse(open(f"{user_image.name}","rb"))
    resp["content-type"] = "image/jpeg"
    resp["content-disposition"] = "attachment"
    return resp
app = run()
