# 05-2 Pytorch RNN LSTM MNIST实战案例_哔哩哔哩 (゜-゜)つロ 干杯~-bilibili
# https://www.bilibili.com/video/BV19a4y1j77Y/?spm_id_from=autoNext
# from tensorflow import nn
import torch


class RNN_model(nn.Module):
    def __init__(self, input_dim, hidden_dim, layer_dim, output_dim):
        super(RNN_model, self).__init()
        self.hidden_dim = hidden_dim
        self.layer_dim = layer_dim
        self.rnn = nn.RNN(input_dim,
                          hidden_dim,
                          batch_first=True,
                          nonlinearity='relu')
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        h0 = torch.zeros(self.layer_dim, x.size(0), self.hidden_dim).requires_grad_().to(device)
        out, hn = self.rnn(x, h0.detach())
        out = self.fc(out[:, -1, :])
        return out


input_dim = 20
hidden_dim = 100
layer_dim = 2
output_dim = 10

model = RNN_model(input_dim, hidden_dim, layer_dim, output_dim)

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

criterion=nn.CrossEntropyLoss()

learning_rate=0.1
optimizer=torch.optim.SGD(model.parameter(),lr=learning_rate)

print(list(model.parameters()))

for i in range(len(length)):
    print('参数：%d '%(i+1))
    print(list(model.parameters()[i]).size())

