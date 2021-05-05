import time
import torch
from torch import autograd

# a = torch.tensor([3.], requires_grad=True)
# b = torch.tensor([2.], requires_grad=True)
# x = torch.tensor([2])
# y = a ** 2 * x + b * x + 1
#
# grads = autograd.grad(y, [a, b])
# print(y)
# print(a.grad)
# print(b.grad)
# print(grads)

# start = time.time()
# a = torch.rand(100, 2000000)
# b = torch.rand(2000000, 300)
# c = torch.matmul(a, b)
# end = time.time()
# print(c)
# print(c.shape)
# print(end - start)

# conda list
# conda --version
# Nvida显卡+ Cuda 运算平台 +Cudnn DL和GPU的融合
# nvcc -V
# add to environment variable

