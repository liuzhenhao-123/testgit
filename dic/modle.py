import torch
import torch.nn as nn
from torch import optim
from torchvision import transforms
"p8-17"
# type(a) python自带
# a.type() pytorch内置
# isinstance(a,torch.FloatTensor)
# isinstance(a,torch.cuda.FloatTensor)
# a.cuda()
# isinstance(a,torch.cuda.FloatTensor)
# 标量，向量，
c = torch.tensor([3.3,2.0,5.5])
print(c.type())
print(c.shape)
print(c.size())
print(len(c.shape))

"p20-21合并切割"
a = torch.rand(4, 32, 8)

b = torch.rand(4, 32, 8)

c = torch.cat([a, b], dim=0)

# print(a.size())
# print(b.size())
# print(c.size())

# stack：创建新的维度
d = torch.stack([a, b, a, b,b,b,a], dim=0)
print(d.size())

# split：按照长度进行拆分
# d0, d1 = d.split([3, 1], dim=0)
# print(d0.size())
# print(d1.size())

# chunk：按照数量进行拆分，
# 如果原始数据有7份，要分为3份，那么7/3=2...1，向上取整，
# 因此第一、二份数据均为3份，第三份数据只能取1了
d0, d1,d2 = d.chunk(3, dim=0)
print(d0.size())
print(d1.size())
print(d2.size())


"P22-24 基本运算 数据统计"
'''a=torch.rand(3,3)
b=torch.ones(3,3)
c=torch.matmul(a,b)
d=a@b
print(a)
print(b)
print(c)
print(d)'''

a = torch.rand(4, 3, 28, 64)
b = torch.rand(4, 3, 64, 604)
c = torch.rand(4, 1, 64, 6004)
d = torch.matmul(a, b)
e = torch.matmul(a, c)  # broadcast机制扩展
print(a.size())
print(b.size())
print(c.size())
print(d.size())
print(e.size())

f = torch.tensor(3.1)
# 向下取整，向上取整，四舍五入，取整数部分，取小数部分。
print(f.floor(), f.ceil(), f.round(), f.trunc(), f.frac())
grad = torch.rand(2, 3) * 20
print(grad)
# print(grad.clamp(5))  # 设置下限（小于5置为5）
# print(grad.clamp(0,10))  # 设置上下限
print(grad.median())

print(grad.norm(1))  # 1范数 绝对值之和

print(grad.norm(2))  # 2范数 平方和开根号

print(grad.norm(2, dim=0))  # 指定维度，求范数

array = torch.arange(0, 9, 1).view(3, 3)
print(array)
print(torch.max(array,dim=1))
print(torch.argmax(array,dim=1,keepdim=True))
print(torch.topk(array,k=1,dim=1,largest=False)) # 最大（小）的k个值
print(torch.kthvalue(array, k=3, dim=1))  # 第k小的数值
print(torch.equal(array,array)) #是否相同

"p62-63-64"
"nn.Module"


# net = nn.Sequential(
#     nn.Linear(2, 3),
#     nn.Linear(5, 4)
# )
#
# print(net)
# print('\n'*2)
#
# print(list(net.parameters()))
# print('\n'*2)
#
# for i in list(net.parameters()):
#     print(i, '\n')
#     print(i.shape, '\n')
# print('\n'*2)
#
# print(
#     dict(net.named_parameters()).items()
# )
#
# optimizer=optim.SGD(net.parameters(),lr=0.01)


class BasicNet(nn.Module):
    def __init__(self):
        super(BasicNet, self).__init__()
        self.net = nn.Linear(4, 3)

    def forward(self, x):
        return self.net(x)


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.net = nn.Sequential(
            BasicNet(),
            nn.ReLU(),
            nn.Linear(3, 2))

    def forward(self, x):
        return self.net(x)


print(BasicNet())
print(Net())
print([list(BasicNet().parameters())[i].shape
       for i in range(len(list(BasicNet().parameters())))])
print([list(Net().parameters())[i].shape
       for i in range(len(list(Net().parameters())))])

x = torch.Tensor([[1, 2, 3, 4],
                  [5, 6, 7, 8]])
print('\n')
print(BasicNet()(x))
print('\n')
print(Net()(x))

print('============================')
# to(device)
device = torch.device('cpu')
net = Net()
print(net.to(device))
# save and load
torch.save(net.state_dict(), 'ckpt.mdl')
p = net.load_state_dict(torch.load('ckpt.mdl'))
print(p)
# train and test
net.train()
net.eval()


# Sequential要求里面的必须是class，如果是函数就不行。因此自定义类Flatten()
class Flatten(nn.Module):
    def __init__(self):
        super(Flatten, self).__init__()

    def forward(self, input):
        return input.view(input.size(0), -1)


class TestNet(nn.Module):
    def __init__(self):
        super(TestNet, self).__init__()
        self.net = nn.Sequential(
            nn.Conv2d(1, 16, stride=1, padding=1),
            nn.MaxPool2d(2, 2),
            nn.Linear(1 * 14 * 14, 10))

    def forward(self, x):
        return self.net(x)


# own linear layer
class MyLinear(nn.Module):
    def __init__(self, inp, outp):
        super(MyLinear, self).__init__()
        self.w = nn.Parameter(torch.randn(outp, inp))
        self.b = nn.Parameter(torch.randn(outp))

    def forward(self, x):
        return x @ self.w.t() + self.b


print('--------------')
x = torch.rand(4, 5)
print(MyLinear(5, 6)(x))

"数据增强 Data argumentation will help ，but not too much." \
"torchvision.transform 提供的图片操作" \
"Reinforcement"
# transforms.Compose(
#     transforms.RandomHorizontalFlip(),
#     transforms.RandomVerticalFlip(),
#     # transforms.RandomRotation(15),
#     transforms.RandomRotation([90, 180, 270]),
#     transforms.Resize([32, 32]),
#     transforms.RandomCrop([28, 28]),
#     # 增加噪声（pytorch不提供）
#     transforms.ToTensor(),
# )

