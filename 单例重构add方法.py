from copy import deepcopy

class D(dict):
    def __add__(self,other):
        if isinstance(other,dict):
            new = deepcopy(self)
            new.update(other)
            return new
        else:
            raise TypeError('not a dict')
''' 相当于 d.update(other) '''
a = ['Nina', 'Jim', 'Rainman', 'Hell']
for i in range(len(a)):
    print(i,a[i])