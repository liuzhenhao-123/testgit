# LSTM实现股价预测 https://www.bilibili.com/video/BV137411d75x
# https://www.bilibili.com/video/BV1Rp4y1Y7Rn/?spm_id_from=autoNext
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import quandl
from keras.layers import Dense, LSTM, Dropout
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler


# 4.1 加载数据

start = date(2000, 10, 12)
end = date.today()
google_stock = pd.DataFrame(quandl.get("WIKI/GOOGL", start_date=start, end_date=end))

print(google_stock.shape)
print(google_stock.tail())
print(google_stock.head())
print(google_stock.columns.values)

# 4.2 绘制历史收盘价趋势图
google_stock['Close'].plot(figsize=(16, 8))
# plt.figure(figsize=(16, 8))
# plt.plot(google_stock['Close'])
plt.show()

# 4.3 构造训练集与验证集
# 时间点长度
time_stamp = 50

# 划分训练集与验证集
google_stock = google_stock[['Open', 'High', 'Low', 'Close', 'Volume']]
train = google_stock[0:2800 + time_stamp]
valid = google_stock[2800 - time_stamp:]

# 归一化
scaler = MinMaxScaler(feature_range=(0, 1))

# 训练集
scaled_data = scaler.fit_transform(train)
x_train, y_train = [], []
print(scaled_data.shape)
print(scaled_data[1, 3])
for i in range(time_stamp, len(train)):
    x_train.append(scaled_data[i - time_stamp:i])
    y_train.append(scaled_data[i, 3])
x_train, y_train = np.array(x_train), np.array(y_train)

# 验证集
scaled_data = scaler.fit_transform(valid)
x_valid, y_valid = [], []
print(scaled_data.shape)
print(scaled_data[1, 3])
for i in range(time_stamp, len(valid)):
    x_valid.append(scaled_data[i - time_stamp:i])
    y_valid.append(scaled_data[i, 3])
x_valid, y_valid = np.array(x_valid), np.array(y_valid)

print(x_train.shape)  # (2800,50,5)
print(x_valid.shape)  # (624,50,5)

# 4.4 创建并训练LSTM模型
# 超参数
epochs = 20  # Epoch 1/20
batch_size = 32  # 88/88 [==============================] - 15s 176ms/step - loss: 0.0063
verbose = 1  # verbose=1  为输出进度条记录

# LSTM 参数: return_sequences=True LSTM输出为一个序列。默认为False，输出一个值。
# input_dim：输入单个样本特征值的维度
# input_length：输入的时间点长度
# keras 中的 verbose 详解 - 简书 https://www.jianshu.com/p/159a9ac413fa
model = Sequential()
model.add(LSTM(units=128, return_sequences=True, input_dim=x_train.shape[-1], input_length=x_train.shape[1]))
model.add(Dropout(0.2))
model.add(LSTM(units=128, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=128))
model.add(Dropout(0.2))
model.add(Dense(units=1))
model.compile(loss='mse', optimizer='rmsprop')
model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, verbose=verbose)


# # 4.4 创建并训练LSTM模型
# epochs = 3
# batch_size = 16
# verbose = 1
# model = Sequential()
# model.add(LSTM(units=100, return_sequences=True, input_dim=x_train.shape[-1], input_length=x_train.shape[1]))
# model.add(LSTM(units=50))
# model.add(Dense(1))
# model.compile(loss='mean_squared_error', optimizer='adam')
# model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, verbose=verbose)


# 4.5预测stock价格
closing_price = model.predict(x_valid)
scaler.fit_transform(pd.DataFrame(valid['Close'].values))
# 反归一化
closing_price = scaler.inverse_transform(closing_price)
y_valid = scaler.inverse_transform([y_valid])
# print(closing_price)
# print(y_valid)
rms = np.sqrt(np.mean(np.power((y_valid - closing_price), 2)))
print('均方根rms:', rms)
print(closing_price.shape)
print(y_valid.shape)

# 拟合stock trend
plt.figure(figsize=(16, 8))
dict_data = {
    'Predictions': closing_price.reshape(1, -1)[0],
    'Close': y_valid[0]
}
data_pd = pd.DataFrame(dict_data)
plt.plot(data_pd[['Close', 'Predictions']])
plt.show()
