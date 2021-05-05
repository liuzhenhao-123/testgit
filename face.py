import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('challenges-in-representation-learning-facial-expression-recognition-challenge/train.csv')

fig = plt.figure()

for j in range(81):
    ax = fig.add_subplot(9, 9, j + 1)

    pixel_str = map(int, data.iloc[j+1000, 1].split(' '))

    imgelist = np.zeros((48, 48))

    for i, val in enumerate(pixel_str):
        imgelist[int(i / 48), int(i % 48)] = val

    ax.imshow(imgelist)
    ax.axis('off')

plt.show()
