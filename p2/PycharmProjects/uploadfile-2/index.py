import dominate.tags as dom
from dominate.document import document
from django_micro import configure,route,run
from django.http import HttpRequest,HttpResponse,FileResponse
from PIL import Image

CENTER_FRAME = "flex flex-col items-center justify-center bg-gray-800 h-screen"
CARD        = "flex flex-col bg-white shadow-xl p-3 rounded-lg w-120 h-120 p-2"
UPLOAD_FORM_ATTRS = {
    "class":"flex flex-col items-center justify-center border-dashed border-4 border-gray-200 h-full",
    "ic-post-to":"/file",
    "ic-target":"#here",          #新增
    "ic-replace-target":"true",
    "enctype":"multipart/form-data"
}
UPLOAD_ICON = "fas fa-file-upload text-gray-300 font-medium text-6xl"
BUTTON      = "flex flex-row items-center justify-center bg-green-400 px-3 py-2 mt-4 text-white rounded shadow"
RESULT_CONTAINER  = "flex flex-col"
RESULT_ITEM       = "flex flex-row items-center justify-between bg-gray-700 p-4 border-t border-gray-600 w-96"

configure({"DEBUG":True})

def link_(lk):
    return dom.link(rel="stylesheet",type="text/css",href=lk)
def script_(s):
    return dom.script(src=s)
def Page():
    doc = document()
    with doc.head:
        link_("https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css")
        link_("https://extra-uru1z3cxu.now.sh/css/extra.css")
        link_("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.8.2/css/all.css")
        script_('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js')
        script_('http://intercoolerjs.org/release/intercooler-1.2.2.js')
    with doc.body:
        with dom.div(cls=CENTER_FRAME) as CenterFrame:
            with dom.div(cls=CARD) as Card:
                with dom.form(UPLOAD_FORM_ATTRS) as UploadForm:
                    dom.i(cls=UPLOAD_ICON, onclick='''$('#fileupload').click()''')
                    dom.p("Find File",id=1, cls="text-gray-500 mt-4")
                    dom.button("Upload",type="submit",cls=BUTTON)
                    dom.input(cls="hidden",type="file",name="image",id="fileupload",onchange='''$('#1').text(this.value.split("\\\\").pop(-1))''')
            with dom.div(id="there",cls=RESULT_CONTAINER) as ResultContainer:
                dom.span(id="here")         #新增
    return doc.render()
def Item(file_name):
    with dom.div(cls=RESULT_ITEM) as ResultItem:
        dom.p(f"{ file_name }.jpg", cls="text-xl text-gray-400")
        dom.i(cls="fas fa-download text-xl text-gray-400")
    return ResultItem.render() +dom.span(id="here").render()                                                          #新增
@route('')
def index(req:HttpRequest):
    return HttpResponse(Page())
@route('file')
def result(req:HttpRequest):
    if req.FILES:
        image = req.FILES.get("image")
        img = Image.open(image)
        img.save(f'{image.name}', optimize=True, quality=70)
        name = image.name.split(".")[0]
    return HttpResponse(Item(name))

app = run()