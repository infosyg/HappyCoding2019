# #file.write(str)的参数是一个字符串，就是你要写入文件的内容.
# # file.writelines(sequence)的参数是序列，比如列表，它会迭代帮你写入文件。
# #readlines(sequence) 和 readline（str）一样的道理
#
# # #
# #
# # l = ['a','b','c','d','\ne',"\nf"]
# # str = ''
# # with open("c:/test/k.txt","w") as f :
# #     f.write(str.join(l))
#
#
# from dominate.document import document
# import dominate.tags as dom
# import requests
# from dominate.util import text
# doc = document
# link="/here"
#
# block = dom.div("there",
#                 dom.div("haha"),
#                 dom.a(href="c:/test/k.txt")
#                 )
#
# section = dom.div("dog")
# section.add(dom.div("bork"))
#
# #with context 上下文
# #for...with ..while true..都是声明-->声明带来块区--->有块区就有语法
# root = dom.div()
# with dom.div() as root:
#     dom.div("first")
#     dom.div("second")
#
# import requests
# with requests.sessions()as sesh:
#     sesh.get("url")
# with dom.ul():
#     dom.li(dom.div())
#     with dom.li():
#         dom.li()
#
# with doc:
#     text("first line")
#     this = dom.div("styled!",cls="blue")
#     this["class"] += "red"
#     with dom.div():
#         text("hi")
#         dom.attr(onclick="alert('hi')")
# print(doc)
#
#
#
# ####1,如何从用户获取数据---->2,如何返回数据给用户
# #采用的技术: micro django + dominate + tailwind + intercooler
# #快速实现 在线压缩图片功能
#



#
#



#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
