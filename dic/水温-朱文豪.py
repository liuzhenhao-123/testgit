import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

# 原始数据:水温-时间曲线
T = np.array(
    [38, 39, 42, 45, 48, 50, 51, 53, 56, 64, 68, 72, 79, 82, 89, 95, 98, 100, 94, 82, 73, 60, 55, 52, 50, 42, 37, 34,
     31, 28, 26, 27, 29, 34, 38, 41, 46, 52, 59, 64, 68, 72, 79, 82, 89, 95, 98, 100, 94, 82, 73, 60, 55, 52, 50, 42,
     37])
plt.plot(T)

# 绘制温度增量曲线
deltaT = T[1:] - T[:-1]
# print(deltaT)
# print(len(T))
# print(len(deltaT))
plt.plot(deltaT)

# 正确曲线标签
plt.plot(np.arange(0, 56).reshape(-1, 1), [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20,
                                           25, 25, 25, 25, 25, 25, 25, 25,
                                           20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20,
                                           20, 20, 20,
                                           25, 25, 25, 25, 25, 25, 25, 25,20])

# 绘制预测曲线
Arr = []
for j in range(len(T) - 1):
    if T[j] < 50:
        Arr.append(10)
    elif deltaT[j] > 0:
        Arr.append(10)
    else:
        Arr.append(15)
plt.plot(range(len(T) - 1), Arr)

plt.legend(['原始数据', '温度增量', '预测曲线', '正确曲线标签'],loc='upper left')
plt.xticks(np.arange(61))
plt.yticks(np.arange(0,101,5))
# plt.yticks([0, 1, 10], ['0', '加温', '停止加温'])

plt.hlines(0, 0, 60)
plt.hlines(50, 0, 60)
plt.hlines(100, 0, 60)
plt.vlines(17, 0, 100)
plt.vlines(24, 0, 100)
plt.vlines(47, 0, 100)
plt.vlines(54, 0, 100)

plt.show()
