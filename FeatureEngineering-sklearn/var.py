# https://scikit-learn.org/stable/modules/feature_selection.html
from sklearn.datasets import load_iris
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest, SelectPercentile
from sklearn.feature_selection import chi2, f_classif, mutual_info_classif
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier
from sklearn.model_selection import cross_val_score,train_test_split,ShuffleSplit,KFold,RepeatedKFold
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.signal as signal
import seaborn as sns

sns.set()

"去除低方差特征，统计学方法"
# np.random.seed(10)
# arr = np.random.random((5, 6))
# var = 0.4
# arrnew = VarianceThreshold(0.4 * var * (1 - var)).fit(arr).transform(arr)
# print(arr)
# print(arrnew)

"单变量特征选择，统计学方法"
X, y = load_iris(return_X_y=True)
print(X.shape, y.shape)

"SelectFromModel 只包含两种方法"
clf = ExtraTreeClassifier()
clf.fit(X, y)
print(clf.feature_importances_)

model = SelectFromModel(clf, prefit=True)
X_new = model.transform(X)
print(X_new.shape)


# "基于原始数据"
# DTC = RandomForestClassifier(n_estimators=20)
# DTC.fit(X, y)
# score1 = cross_val_score(DTC, X, y, cv=5)
# print(np.mean(score1))
#
# "单变量特征选择，统计学方法"
# Xnew = SelectKBest(chi2, k=2).fit_transform(X, y)  # 保留特征的个数
# DTC2 = RandomForestClassifier(n_estimators=20)
# DTC2.fit(X, y)
# score2 = cross_val_score(DTC2, Xnew, y, cv=5)
# print(Xnew.shape, y.shape)
# print(np.mean(score2))
#
# "单变量特征选择，统计学方法 保留特征的比率"
# Xnew3 = SelectPercentile(mutual_info_classif, percentile=80).fit_transform(X, y)
# DTC3 = RandomForestClassifier(n_estimators=20)
# DTC3.fit(Xnew3, y)
# score3 = cross_val_score(DTC3, Xnew3, y, cv=5)
# print(Xnew3.shape, y.shape)
# print(np.mean(score3))
#
# "保存数据到CSV"
# # path = './1.csv'
# # pd.read_csv(path)
# pd.concat((pd.DataFrame(X), pd.DataFrame(y)), axis=1).to_csv('./1.csv', index=False)
# pd.concat((pd.DataFrame(X), pd.DataFrame(y)), axis=1).to_csv('./2.csv', index=True)
