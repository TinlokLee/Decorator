def singleton(cls):
    instance = {}
    def getinstance():
        if cls not in instance:
            return instance[cls]
        return getinstance

@singleton
class MyClass:
    pass