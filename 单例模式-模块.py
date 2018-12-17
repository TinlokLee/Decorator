# class Singleton(object):
#     def foo(self):
#         pass
# singleton = Singleton()

def singleton(cls):
    """ 使用 decorator 实现 singleton """
    _instance = {}
    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return _singleton

@singleton
class A:
    a = 1
    def __init__(self, x=0):
        self.x = x

a1 = A(2)
a2 = A(3)
a = A(9)
print(a,a1,a2)

class A(object):
    obj = None 
    def __new__(cls):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            return cls.obj
        else:
            return cls.obj


class MySingleton(object):
    obj = None
    def __new__(cls):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            return cls.obj
        else:
            return cls.obj
def mySingleton(cls):
    _instance = {}
    def wra():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return mySingleton

