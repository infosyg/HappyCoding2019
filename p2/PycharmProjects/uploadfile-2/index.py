# "https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css"
# "https://extra-uru1z3cxu.now.sh/css/extra.css"
# "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.8.2/css/all.css"
# 'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js'

import dominate.tags as dom 
from dominate.document import document
from django_micro import configure,route,run
from django.http import HttpRequest,HttpResponse
CENTER_FRAME = "flex flex-col bg-white shadow-xl p-3 rounded-lg w-120 h-120"
upload_form = "flex fle"

configure({"DEBUG":True})
def link(lk):
    return dom.link(rel="stylesheet",type="text/css",href=lk)

def page():
    doc = document()
    with doc.head:
        link_("https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css")
        link_("https://extra-uru1z3cxu.now.sh/css/extra.css")
        link_("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.8.2/css/all.css")
        link_('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js')
    with doc.body:
        pass
    return doc.render()
print(page())
