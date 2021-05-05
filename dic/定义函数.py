import numpy as np


def area_of_circle(r):
    s = np.pi * r ** 2
    print(s)


def power(x, n=2):
    s = x ** n
    return s


# 参数个数可变
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


area_of_circle(1)

print(max(1, 6, 2, 3, -9))
print(hex(255))
print(power(20, 3))
print(calc(2, 6, 1, 2))
print(fact(7))

g = lambda x, y: x + y
print(g(3, 4))
