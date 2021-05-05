#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']


path = 'C:/Users/Administrator/Desktop/MyoFile/RealTimeRecord/2020-08-13_20-30-05.txt'

# np.loadtxt(path,encoding='utf-8')

# r=open(path,encoding='utf-8').read()
# print(r)

# print(r2[0])
# print(r2.iloc[1,1])
# r2.drop()
# print(data.iloc[:, 1])
# plt.plot(data.iloc[:,0])

# plt.xticks([0,50,100], [-10,0,10], rotation=90)
# print(list(range(100)[::2]))

data = pd.read_table(path, sep='\s+')
print('原始数据：\n',data.head())
print('原始数据shape：\n',data.shape)

for i in range(data.shape[0]):
    if np.mod(i, 2) == 1:
        data.drop(axis=0, index=i, inplace=True)
print('删除NAN空行后的数据：\n',data)

plt.plot(range(2000), data.iloc[:2000, 1])
plt.plot(range(2000), data.iloc[:2000, 2])
plt.plot(range(2000), data.iloc[:2000, 3])
plt.plot(range(2000), data.iloc[:2000, 4])
plt.plot(range(2000), data.iloc[:2000, 5])
plt.plot(range(2000), data.iloc[:2000, 6])
plt.legend([('通道',i) for i in range(6)])


plt.xticks(range(2000)[::90], data.iloc[:2000, 0][::90], rotation=90)
plt.vlines(0, 120, 180)
plt.vlines(2000, 120, 180)
plt.show()