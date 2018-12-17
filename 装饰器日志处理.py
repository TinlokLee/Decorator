'''
    打印日志的装饰器

'''
def log(func):
    def wrapper(*args, **kwargs):
        print("call %s" % func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log
def foo():
    print("2018-12-14")

print(foo())

print("--------------------------------------------")
#  日志本身需要传参
def log(text):
    def deco(func):
        def wrapper(*args, **kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return deco

@log("execute")
def foo():
    print("2018-12-14")

print(foo())

print("=================================")
import functools


# def log(text):
#     def deco(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             print('%s %s()' % (text, func.__name__))
#             return func
#         return wrapper
#     return deco

# @log("execute")
# def foo():
#     print("带参装饰器")
# print(foo())
