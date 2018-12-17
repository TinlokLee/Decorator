# def fib(max):
#     x,y = 0,1
#     while y < max:
#         yield y
#         print(y)
#         x, y = y, x+y
     
#     return 'OK!'

# print(fib(8))

def fib(n):
    m, a, b = 0, 0, 1
    while m <n:
        print(b)
        a, b = b, a + b
        m += 1
    
    #return 'OK!'

print(fib(5))

# def fib(num):
#     a, b, n = 0, 0, 1
#     while n <= num:
#         yield n
#         a, b = b, b+a
#         n += 1
# # for i in fib(5):
# #     print(i)
# a = fib(5)
# print(a)