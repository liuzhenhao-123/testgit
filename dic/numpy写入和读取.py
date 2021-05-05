import numpy as np

# # 将0-99写入a.csv
# a = np.arange(100).reshape(5, 20)
# np.savetxt('a.csv', a, fmt='%d', delimiter=';')

# # 从a.csv中读取数据
# b = np.loadtxt('a.csv', dtype=np.int, delimiter=';')
# print(b)

# # a.tofile()
# c = np.arange(100).reshape(10, 2, 5)
# c.tofile("c.bat", sep=",", format='%d')
# print(c)

# # a.fromfile()
# d = np.fromfile("c.bat", dtype=np.int, sep=',').reshape(10, 5, 2)
# print(d)

# np.save()
# np.savez()
# np.load()

# # 随机数函数np.random
# print(np.random.rand(4, 3, 2))  # 0-1随机数
# print(np.random.randn(2,3,4))  # 0-1正态分布
# print(np.random.randint(2,8,5))  # 5个2-7随机数
# print(np.random.seed())
# print(np.random.uniform(0,1,(3,6)))  # 0-1随机浮点数
# print(np.random.normal(0,1,(3,6)))  # 0-1浮点正态分布

# # Array的统计特征
# a = np.arange(100).reshape(5, 20)
# print(a)
# print(np.sum(a, axis=1))  # axis=1,行内运算
# print(np.mean(a))  # 平均值
# print(np.average(a, axis=0,weights=[1,3,5,7,9]))  # 列内加权平均
# print(np.std(a))  # 标准差
# print(np.var(a))  # 方差
# print(np.max(a, axis=1))  # 行内最值
# print(np.argmax(a,axis=0))  # 列内最大值的位置
# print(np.median(a))  # 中位数
# print(np.ptp(a))  # 极差
