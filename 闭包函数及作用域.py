'''
    Python 闭包函数及作用域（延时绑定）
    闭包函数特点：
    1  内嵌函数
    2  对外部函数变量引用
    3  外部函数返回内嵌函数
    4  闭包函数特有属性：__closure__验证是否闭包函数

    LEGB 规则
    local     局部作用域
    Enclosing 嵌套作用域
    Global    全局作用域
    Built-in  内建作用域

    Python 解释器查找变量时顺序 L-->E-->G-->B
           只有函数，类，模块会产生作用域，代码块不会

    闭包函数应用场景&作用：
    1  减少函数所需定义的参数数目，在并行运算环境下，每台电脑
       负责一个函数，即一台电脑输出和另一台电脑输入串联起来
    2  提高代码可复用性
    3  自带函数作用域（LEGB法则）
    4  延迟计算（惰性计算）
    5  函数始终保持一种状态


'''


lst = [lambda x:x+i for i in range(4)]
res = [x(3) for x in lst]

print(res)
# 改写函数
def foo():
    return [lambda x: x+i for i in range(4)]
print([x(3) for x in foo()])


#  把 i 变为内部变量，输出【3,4,5,6】
def foo():
    return [lambda x, i=i: x+i for i in range(4)]
print([x(3) for x in foo()])
print('-------------------------------------')

def func1():
    ss_list = []
    for i in range(4):
        def foo1(x, i=i):
            return x+i
        ss_list.append(foo1)
    return ss_list
for m in func1():
    print([m(3)])
print('+++++++++++++++++++++++++++++++++++++')

#  改写为闭包函数形式
def bar():
    ss = []
    # def foo(x):
    for i in range(4):
        def foo(x):
            return x+i
        ss.append(foo)
    return ss

for x in bar():
    print([x(3)])

# def counter(start_at=0):
#     count = [start_at]
#     def incr():
#         count[0] += 1
#         return count[0]
#     return incr


def func1():
    ''' 函数始终保持一种状态 '''
    name = 'Hello Python'
    def func():
        print('I like %s' % name)
    return func
func = func1()
print(func()) 
# 此时func就是一个闭包函数，无论该函数在程序哪个位置调用，结果都一样

def foo():
    print('My name is foo')
    name = 'python'
    def bar():
        print(name)
        print('My name is bar')
    return bar

f1 = foo()
def func():
    print('My name is func')
    name1 = '666'
    print(f1())
    # 验证闭包函数
    print(f1.__closure__)
    print(func())