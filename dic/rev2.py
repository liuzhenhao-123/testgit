# !/usr/bin/python
# -*- coding: UTF-8 -*-

"""
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5, 8, 3, 5, 6, 4])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
"""
'''
# 打印属性，删除属性
class Coordinate:
    x = 10
    y = -5
    z = 0
point1 = Coordinate()
print('x = ', point1.x)
print('y = ', point1.y)
print('z = ', point1.z)
print(hasattr(point1, 'x'))
print(hasattr(point1, 'y'))
print(hasattr(point1, 'z'))
print(hasattr(point1, 'no'))  # 没有该属性
delattr(Coordinate, 'z')
print('--删除 z 属性后--')
print('x = ', point1.x)
print('y = ', point1.y)
print('z = ', point1.z)# 触发错误
'''
"""
import random
x=random.choice(range(10))
print(x)
"""
'''
x = set('runoob')
y = set('google')
print(x)
print(x - y)  # 交集
'''
"""
f = open('test.txt')
for line in f:
    print(line)
f.close()
"""
'''
print(round(52.611641648,8))
'''
"""
import time

print("---RUNOOB EXAMPLE ： Loading 效果---")

print("Loading", end="")
for i in range(20):
    print(".", end='', flush=True)
    time.sleep(0.5)
"""
# Fibonacci series: 斐波纳契数列
a, b = 0, 1
while b < 30:
    print(b, end=',')
    a, b = b, a + b


def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]

    print(inputWords)

    # 重新组合字符串
    output = ' '.join(inputWords)

    return output


if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)