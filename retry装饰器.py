import time

class Retry(object):
    def __init__(self,max_retries=3,wait=0,exceptions=(Exception,)):
        self.max_retries = max_retries
        self.wait = wait
        self.exceptions = exceptions

    def __call__(self,func):
        def wrapper(*args,**kwargs):
            for i in range(self.max_retries+1):
                try:
                    ressult = func(*args,*kwargs)
                except self.exceptions:
                    time.sleep(self.wait)
                    continue
                else:
                    return ressult
            return wrapper

''' 使用 '''
a = Retry(5)
print(a) 
b = Retry(999) 
print(b)          