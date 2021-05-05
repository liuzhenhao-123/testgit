# https://www.bilibili.com/video/BV1Y7411d7Ys?p=4
# nonlinear激活函数，否则多层神经网络并没有什么实际意义。
# 误差反向传播，计算多层复杂网络的梯度（即代价函数Loss对w求导），不能靠写解析式来实现。
# l.backward()  # 自动计算链路上需要求梯度的地方（requires_grad = True），并将梯度保存到w.grad内
# w.grad=delta Loss/delta w
# tensor是Pytorch构建动态图的重要组成成分，包含data和gradient,储存了权重node和损失函数对权重的导数gradient

import torch
import matplotlib.pyplot as plt
import numpy as np

x_data = torch.Tensor([[1.2], [2.0], [3.0]])
y_data = torch.Tensor([[2.0], [4.5], [6.0]])
plt.scatter(x_data.numpy(),y_data.numpy())
w = torch.Tensor([1.0])
w.requires_grad = True  # 需要计算梯度


# 不单单是矩阵运算，更是在构建计算图的过程
def forward(x):
	return x * w  # x不是tensor格式，但是w是Tensor，因此，pytorch自动将x转换为Tensor


def loss(x, y):
	y_pred = forward(x)
	return (y_pred - y) ** 2


print('Predict before training', 4, forward(4))

for epoch in range(50):
	for x, y in zip(x_data, y_data):
		l = loss(x, y)
		l.backward()  # 自动计算链路上需要求梯度的地方，requires_grad = True，并将梯度保存到w内
		print(l.item())
		print('\tgrad:', x, y, w.grad.item())  # w.grad.item(),要取item，否则Tensor会构建大量的计算图
		w.data = w.data - 0.01 * w.grad.data  # 取data是不会构建计算图的，只会进行纯数值计算；若没有data，就是Tensor格式
		w.grad.data.zero_()  # 若没有这句代码，data会在之前计算的结果上不断累加，而我们要的不是累加值
	xx = np.arange(0, 4, 0.1)
	# plt.clf()
	plt.plot(xx, w.data * xx,linewidth=1)
	plt.ylim([0,8])
	plt.pause(0.1)

print('Predict after training', 4, forward(4))

plt.show()


