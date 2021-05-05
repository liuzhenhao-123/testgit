import torch
import numpy as np
import torch.nn as nn

'''x = torch.tensor([[
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]]
]])
print(x.shape)
y = nn.Flatten(start_dim=0,end_dim=-2)(x)
print(y)'''

# x = torch.ones(5)  # input tensor
x = torch.FloatTensor([1, 2, 3, 4, 5])  # input tensor
y = torch.zeros(3)  # expected output
w = torch.randn(5, 3, requires_grad=True)
b = torch.randn(3, requires_grad=True)
z = torch.matmul(x, w) + b
loss = torch.nn.functional.binary_cross_entropy_with_logits(z, y)

print(w)
print(b)
print(loss)

# print('Gradient function for z =',z.grad_fn)
# print('Gradient function for loss =', loss.grad_fn)
loss.backward()
print(w.grad)
print(b.grad)

# z = torch.matmul(x, w)+b
# print(z.requires_grad)
#
# with torch.no_grad():
#     z = torch.matmul(x, w)+b
# print(z.requires_grad)
#
# z = torch.matmul(x, w)+b
# z_det = z.detach()
# print(z_det.requires_grad)




# x = torch.Tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(x,type(x))
#
# y=np.array([0, 1, 2.3, 3, 4, 5, 6, 7, 8, 9])
# print(y,type(y),y.dtype)
#
# z=torch.from_numpy(y)
# print(z,type(z))
#
# c1=torch.ones_like(z)
# c1=torch.zeros_like(z)
# c1=torch.rand_like(z)
#
# print(c1,type(c1),c1.device)
# print(torch.cuda.is_available())
# print(c1[0],c1[0].item())