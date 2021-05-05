import torch
import numpy as np
import torch.nn as nn


class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(in_features=28 * 28, out_features=512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
            nn.ReLU()
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits


model = NeuralNetwork()

X = torch.rand(11, 28, 28)
print(X.shape)

logits = model(X)
print(logits.shape)
# print(logits)

pred_probab = nn.Softmax(dim=1)(logits)
print(pred_probab.shape)
# print(pred_probab)

y_pred = pred_probab.argmax(dim=1)
print(f"Predicted class: {y_pred}")

for i in model.parameters():
    print(i.shape)

for i, j in model.named_parameters():
    print(i, j.size())

learning_rate = 1e-3
batch_size = 64
epochs = 5

# Initialize the loss function
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
