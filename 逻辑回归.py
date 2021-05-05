import torch

x = torch.Tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).view(-1, 1)
y = torch.Tensor([-1, 1, 3, 5, 7, 9, 11, 13, 15, 17]).view(-1, 1)


class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linears = torch.nn.Linear(1, 1)

    def forward(self, x):
        return self.linears(x)


net = Model()
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(net.parameters(), lr=0.01)
print('训练前')
print(net.linears.weight.item())
print(net.linears.bias.item())

for i in range(500):
    optimizer.zero_grad()
    ml = net(x)
    loss = criterion(ml, y)
    # losslist.append(loss.data)
    loss.backward()
    optimizer.step()

print('训练后')
print(net.linears.weight.item())
print(net.linears.bias.item())

# x_test = torch.Tensor([[58.0]])
# y_test = net(x_test)
# print('y_pred=', y_test.data)

# import matplotlib.pyplot as plt
# plt.plot(losslist)
# plt.show()

# 保存模型
net = Model()
torch.save(net, 'model.pth')

# 加载模型
net = torch.load('model.pth')

# 保存模型参数
net = Model()
torch.save(net.state_dict(), 'modelstate_dict.pth')

# 加载模型参数
net = Model()
net.load_state_dict(torch.load('modelstate_dict.pth'))
