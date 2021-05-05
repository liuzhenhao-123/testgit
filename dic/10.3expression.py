import pandas as pd
stock=pd.read_csv('000777.csv',encoding='GBK')
print(stock.head())
# print(stock.shape)
# y=stock['涨跌幅']
# print(y.shape)
# print(y[0])
features=stock.loc[:,'股票代码':'流通市值']
X=features.values
print(X.shape)
print(X[0])

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# mlpr=ML
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=62)

scaler=StandardScaler()
scaler.fit(X_train)
X_train_scaled=scaler.transform(X_train)
X_test_scaled=scaler.transform(X_test)
mlpr.fit(X_train_scaled,y_train)
print(mlpr.score(X_test_scaled,y_test))
