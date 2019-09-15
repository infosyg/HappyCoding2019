
#locals 和globals 内置 函数locals例子
# https://blog.csdn.net/scelong/article/details/6977867
# def foo(arg,a):
#     x = 1
#     y = "xxxx"
#     for i in range(10):
#         j = 1
#         k = i
#         print (locals())
# foo(1,2)
#
#装饰器的用法
#https://www.jb51.net/article/158814.htm
def w1(func):
    def inner():
        print('...验证权限...')
        func()
    return inner

@w1
def f1():
    print('f1 called')
@w1
def f2():
    print('f2 called')
f1()
f2()