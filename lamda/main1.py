# x = lambda a, b, c: a + b + c
# print(x(5,10,40))

def plus(n):
    return lambda a: a * n

_plus = plus(10)

print(_plus(2))