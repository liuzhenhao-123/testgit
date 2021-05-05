#特征化向量，跟pandas中的get dummies相似。
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline # 特征管道5.4.6

'''
# 5.4.4衍生特征，多元线性回归，提高预测精度
x = np.array(np.arange(1, 6))
y = np.array([4, 2, 1, 3, 7])
plt.scatter(x, y,color='y')

X = x[:, np.newaxis]
model = LinearRegression().fit(X, y)
yfit = model.predict(X)
plt.plot(x, yfit,color='g')

poly = PolynomialFeatures(degree=3, include_bias=False)
X2 = poly.fit_transform(X)
# print(X2)
model = LinearRegression().fit(X2, y)
yfit = model.predict(X2)
plt.plot(x, yfit,color='r')

plt.show()

print(model.coef_)
'''
'''
# 5.4.5缺失值补充,再线性回归预测
X = np.array([[np.nan, 0, 3],
              [3, 7, 9],
              [3, 5, 2],
              [4, np.nan, 6],
              [8, 8, 1]])
y = np.array([14, 16, -1, 8, -5])

imp = SimpleImputer(strategy='mean')
X2 = imp.fit_transform(X)
print(X2)

model=LinearRegression().fit(X2,y)
print(model.predict(X2))

# 综合缺失值补充、衍生特征的线性回归预测
X = np.array([[np.nan, 0, 3],
              [3, 7, 9],
              [3, 5, 2],
              [4, np.nan, 6],
              [8, 8, 1]])
y = np.array([14, 16, -1, 8, -5])
model = make_pipeline(SimpleImputer(strategy='mean'),
                      PolynomialFeatures(degree=2),
                      LinearRegression())
model.fit(X, y)
print(y)
print(model.predict(X))
'''

'''
# 线性回归预测正弦曲线。
poly_model = make_pipeline(PolynomialFeatures(12), LinearRegression())
rng = np.random.RandomState(1)
x = 20 * rng.rand(400)
y = np.sin(x) + 0.02 * rng.randn(400)
poly_model.fit(x[:, np.newaxis], y)
xfit = np.linspace(0, 20, 100)
yfit = poly_model.predict(xfit[:, np.newaxis])
y1 = np.sin(xfit)
plt.plot(xfit, y1)
plt.scatter(x, y, s=20)
plt.scatter(xfit, yfit, s=15, edgecolors='black')
plt.show()
'''