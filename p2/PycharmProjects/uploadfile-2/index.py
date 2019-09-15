import dominate.tags as dom
from dominate.document import document
from django_micro import configure, route, run
from django.http import HttpRequest, HttpResponse, FileResponse

CENTER_FRAME = "flex flex-col items-center justify-center bg-gray-800 h-screen"
CARD = "flex flex-col bg-white shadow-xl p-3 rounded-lg w-120 h-120 p-2"
UPLOAD_FORM = "flex flex-col items-center justify-center border-dashed border-4 border-gray-200 h-full"
UPLOAD_ICON = "fas fa-file-upload text-gray-300 font-medium text-6xl"
BUTTON = "flex flex-row items-center justify-center bg-green-400 px-3 py-2 mt-4 text-white rounded shadow"
RESULT_CONTAINER = "flex flex-col"
RESULT_ITEM = "flex flex-row items-center justify-between bg-gray-700 p-4 border-t border-gray-600 w-96"

configure({"DEBUG": True})


def link_(lk):
    return dom.link(rel="stylesheet", type="text/css", href=lk)


def page():
    doc = document()
    with doc.head:
        link_("https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css")
        link_("https://extra-uru1z3cxu.now.sh/css/extra.css")
        link_("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.8.2/css/all.css")
        dom.script('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js')

    with doc.body:
        with dom.div(cls=CENTER_FRAME) as CenterFrame:
            with dom.div(cls=CARD) as Card:
                with dom.form(cls=UPLOAD_FORM) as UploadForm:
                    dom.i(cls=UPLOAD_ICON, onclick='''$('#fileupload').click()''')
                    dom.p("Find File", id=1, cls="text-gray-500 mt-4")
                    dom.button("Upload", cls=BUTTON)
                    dom.input(cls="hidden", type="file", id="fileupload",
                              onchange='''$('#1').text(this.value.split("\\\\").pop(-1))''')
            with dom.div(cls=RESULT_CONTAINER) as ResultContainer:
                for _ in range(4):
                    with dom.div(cls=RESULT_ITEM) as ResultItem:
                        dom.p("filename.jpg", cls="text-xl text-gray-400")
                        dom.i(cls="fas fa-download text-xl text-gray-400")

    return doc.render()


@route('')
def index(req: HttpRequest):
    return HttpResponse(page())


app = run()
