''' 自定义装饰器，实现首字母大写 '''

def deco(func):
    def wrap(*args, **kwargs):
        msg = func(*args, **kwargs)
        res = msg[0].upper() + msg[1:]
        return res
    return wrap

@deco
def getTxt(word='hello word'):
    #return word.lower()
    print(word.lower())

x = [1,2,3]
x.insert(1,4)  # insert(index, obj)
print(x)