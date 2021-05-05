from sklearn.datasets import load_boston
from sklearn import preprocessing
# import torch
import pandas as pd
import os
import numpy as np

# 载入数据，并预处理
category_list = os.listdir('./record')
category_path_list = ['./record/' + category_list[i] for i in range(len(category_list))]
print(category_path_list)

Datas = pd.DataFrame(data=None, columns=['GSR', 'ECG', 'EMG', 'HR'])
print(Datas)

total = 0
for j in category_path_list:
    Volunteers = os.listdir(j)
    num = len(Volunteers)
    total += num
    for k in range(num):
        # fullpath = j + '/' + Volunteers[k]
        fullpath = os.path.join(j, Volunteers[k])
        print(fullpath)
        Data = pd.read_csv(fullpath)
        # print(Data.head(3))
print('志愿者数量=', total)
Data = pd.Series([1, 2, 35, 8])
Datas = pd.concat(Datas, Data)

# X, y = load_boston(return_X_y=True)
# X = preprocessing.scale(X[:100, :])
# y = preprocessing.scale(y[:100].reshape(-1, 1))
#
# # 定义超参数
# data_size, D_input, D_output, D_hidden = X.shape[0], X.shape[1], 1, 50
# lr = 1e-5
# epoch = 200000
#
# # 转换为Tensor
# # X = torch.Tensor(X).type(dtype)
# # y = torch.Tensor(y).type(dtype)
# X = torch.from_numpy(X).type(dtype)
# y = torch.from_numpy(y).type(dtype)
#
# # 定义训练参数
# w1 = torch.randn(D_input, D_hidden).type(dtype)
# w2 = torch.randn(D_hidden, D_output).type(dtype)
#
# # 进行训练
# for i in range(epoch):
#
#     # 前向传播
#     h = torch.mm(X, w1)  # 计算隐层
#     h_relu = h.clamp(min=0)  # relu
#     # y_pred = torch.mm(h_relu, w2)  # 输出层
#     y_pred = h_relu.mm(w2) # 输出层
#
#     # loss计算，使用L2损失函数
#     loss = (y_pred - y).pow(2).sum()
#
#     if i % 10000 == 0:
#         print('epoch: {} loss: {:.4f}'.format(i, loss))
#
#     # 反向传播，计算梯度
#     grad_y_pred = 2.0 * (y_pred - y)
#     grad_w2 = torch.mm(h_relu.t(), grad_y_pred)
#     grad_h_relu = torch.mm(grad_y_pred, w2.t())
#
#     # relu函数的倒数 右半段=1 左半段=0
#     grad_h = grad_h_relu.clone()
#     grad_h[h < 0] = 0
#
#     grad_w1 = torch.mm(X.t(), grad_h)
#
#     # 更新计算的梯度
#     w1 -= lr * grad_w1
#     w2 -= lr * grad_w2
