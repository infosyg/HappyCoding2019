from django_micro import route, run,configure
from django.http import HttpResponse, HttpRequest,FileResponse
import dominate.tags as dom
from dominate.document import document
from PIL import Image


DEBUG = True
configure(locals())

def page():
    doc = document()
    with doc as root:
        with doc.body:  ## form input button;input三个属性：type，name，value
            with dom.form(action="/file",method="post",enctype="multipart/form-data"):
                dom.input(type="file",name="image")
                dom.button("submit",type="submit")
    return root.render()


@route("")
def index(request:HttpRequest):
    return HttpResponse(page())

@route('file')
def filehandler(request:HttpRequest):
    #创建一个 PIL 的image 的对象，顺便给它压缩 保存
    user_image = request.FILES.get("image")
    img = Image.open(user_image)
    img.save(f"{user_image.name}",optimize=True,quality=70)
    # 使用FileResponse返回文件
    resp = FileResponse(open(f"{user_image.name}","rb"))
    # 使用content - type修改返回文件的类型
    resp["content-type"] = "image/jpeg"
    resp["content-disposition"] = "attachment"
    return resp
app = run()
