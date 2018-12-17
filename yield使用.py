'''def f123():
    yield 1
    yield 2
    yield 3
for item in f123:
    print(item)
    #TypeError: 'function' object is not iterable'''

def some_func():
    for i in range(4):
        yield i 
for i in some_func():
    print(i)

x = iter(range(3))  # 实例对象 x 
x1 = next(x)
print(x1)   # 执行过程：0,1,2,3 函数挂起，next 方法进入for循环调用一次0 >> 01230
print('------------')
x2 = next(x)
print(x2)
print('************')
# mm = some_func()
# mm.send(3)
# print(mm)
# x4 = next(x)
# print(x4)
#  0,1,2, StopIteration
def foo():
    print('7777')
    m = yield 1
    print(m)
    n = yield 2
    print(n)

f = foo()
print(next(f))
print(f.send('nihao'))