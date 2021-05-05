# https://www.bilibili.com/video/BV1Wh411Z7qV
# Keras MNIST 识别

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cv2
from keras import models
from keras.optimizers import Adam, RMSprop
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ReduceLROnPlateau
from keras.layers import Conv2D, Input, LeakyReLU, Dense, Activation, Flatten, Dropout, MaxPool2D
import pickle
from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape([-1, 28, 28, 1]) / 255
y_train = y_train.reshape([-1, 1]) / 255

# X_val=X_train[:int(X_train.shape[0]*0.2),:]
# y_val=y_train[:int(y_train.shape[0]*0.2)]
# print(X_val.shape)
# print(y_val.shape)

# fig=plt.figure(figsize=(16,8))
# fig.add_subplot(121)
# fig.add_subplot(122)
# plt.show()


# np.random.seed(666)
# train_data = pd.read_csv('test2.csv')
# print(train_data.head())
# train_data = train_data.iloc[np.random.permutation(len(train_data))]
# print(train_data.head())
# print(train_data.shape)

'''
arr = np.arange(9).reshape((3, 3))
arr = 34
arr = np.array([3,5,5,69,8,583,8,9])
print(np.random.permutation(arr))'''
