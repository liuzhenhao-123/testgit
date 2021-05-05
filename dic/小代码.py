import numpy as np
import pandas as pd
import math

# 向下取整
x = math.floor(3.35)
print(x)

# 加r表示不转义，原样输出
print(r'hello\\')

# 三撇表示跨行输出；另一种含义是跨行注释
print('''Hello,my
name
is Jack''')

# 逻辑运算and
print(True and False)

# 默认序号从0开始；补充缺失值为0
A = pd.Series([2, 4, 6])
B = pd.Series([1, 3, 5], index=[1, 2, 3])
print(A + B)
print(A.add(B, fill_value=0))

# 求平均值
rng = np.random.RandomState(42)
A = pd.DataFrame(rng.randint(0, 20, (2, 2)), columns=list('AB'))
print(A)
print(A.stack().mean())

# 随机状态
rng = np.random.RandomState(1)
x = 10 * rng.rand(50)
print(x.shape)

# for 循环
print([x * x for x in range(1, 11)])

# for循环
d = {'a': 1, 'b': 2, 'c': 3}
for value in d.values():
    print(value)

# 水平方向拼接数组
array_1 = [1, 2, 3, 4, 5]
array_2 = [6, 7, 8, 9, 10]
array_3 = np.hstack((array_1, array_2))
print(array_3)
print(array_3.shape)

# 计算人体BMI指数
x = input('身高：')
y = input('体重：')
x1 = float(x) ** 2
y1 = float(y)
bmi = y1 / x1
if bmi < 18.5:
    print('thin')
else:
    print('fat')


# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    if 0 == len(s):
        return s

    while ' ' == s[0]:
        s = s[1:]
        if 0 == len(s):
            return s

    while ' ' == s[-1]:
        s = s[:-1]
        if 0 == len(s):
            return s

    return s
