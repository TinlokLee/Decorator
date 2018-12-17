import time
''' 
    装饰器作用：为已存在对象，增加额外功能
    应用场景：  缓存、权限校验、性能检测、日志、统计、事物处理等
'''

def deco(func):
    def wrapper(*args, **kwagrs):
        t1 = time.time()
        func(*args, **kwagrs)
        t2 = time.time()
        res = t2 - t1
        print('time is {}'.format(res))
        return res
    return wrapper

# 装饰器的调用，打印出结果和函数执行时间
@deco
def foo(x, y):
    print(x*y)
    return x*y

foo(22, 44)
def foo():
    return [lambda x :i+x for i in range(4)]

print(foo())
print([x(3) for x in foo()]) 


