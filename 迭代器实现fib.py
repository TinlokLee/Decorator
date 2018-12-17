# # 自定义一个迭代器实现斐波那契数列
# class Fib:
#     def __init__(self, max):
#         self.a = 0
#         self.b = 1
#         self.max =max
#         # 设置出口方法
#         self.count = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         n_next = self.a
#         self.a, self.b = self.b, self.a+self.b
#         self.count += 1
#         if self.count > self.max:
#             raise StopIteration
#         return n_next

# f = Fib(9)
# print(next(f))

class Fib:
    def __init__(self,n):
        self.n = n
        self.a = 0
        self.b = 1
        self.count = 0 

    def __iter__(self):
        return self
    
    def __next__(self):
        val =self.a
        self.a, self.b = self.b, self.a+self.b
        self.count += 1
        if self.count >self.n:
            raise StopIteration
        return val

f = Fib(2)
print(next(f))