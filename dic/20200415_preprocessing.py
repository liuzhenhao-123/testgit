# https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing
# 5.3.1节
from sklearn import preprocessing
import numpy as np

'''
X_train = np.array([[ 1., -1.,  2.],
                    [ 2.,  0.,  0.],
                    [ 0.,  1., -1.]])
#矩阵列标准化
X_scaled = preprocessing.scale(X_train)
print(X_scaled)
print(X_scaled.mean(axis=0))#矩阵列标准化的均值（0）
print(X_scaled.std(axis=0))#矩阵列标准化的标准差（1）

######################
#with_mean=True/False 列向量要不要均值归零化
#with_std=True/False 列向量要不要标准差值归1化
scaler = preprocessing.StandardScaler(with_mean=True, with_std=True).fit(X_train)
print(scaler)
print(scaler.mean_)                                      
print(scaler.scale_)
#这步才开始实际操作X_train矩阵
print(scaler.transform(X_train))

#给了一个新的X_test，按照之前的规则转化
X_test = [[-1., 1., 0.]]
print(scaler.transform(X_test))

'''
'''
X_train = np.array([[ 1., -1.,  2.],
                    [ 2.,  0.,  0.],
                    [ 0.,  1., -1.]])
#最小值化为0,最大值化为1,formula=(x-min)/(max-min)
min_max_scaler = preprocessing.MinMaxScaler()
X_train_minmax = min_max_scaler.fit_transform(X_train)
print(X_train_minmax)

X_test = np.array([[-3., -1.,  4.]])
X_test_minmax = min_max_scaler.transform(X_test)
print(X_test_minmax)
'''
X_train = np.array([[1., -1., 2.],
                    [2., 0., 0.],
                    [0., 1., -1.]])

max_abs_scaler = preprocessing.MaxAbsScaler()
X_train_maxabs = max_abs_scaler.fit_transform(X_train)
print(X_train_maxabs)

X_test = np.array([[-3., -1., 4.]])
X_test_maxabs = max_abs_scaler.transform(X_test)
print(X_test_maxabs)
print(max_abs_scaler.scale_)
