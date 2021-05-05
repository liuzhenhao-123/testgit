import numpy as np
from sklearn.datasets import load_iris
from sklearn import preprocessing
from sklearn.model_selection import train_test_split


# iris = load_iris()
# X, y = iris.data, iris.target
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
#
# quantile_transformer = preprocessing.QuantileTransformer(random_state=0)
# X_train_trans = quantile_transformer.fit_transform(X_train)
# X_test_trans = quantile_transformer.transform(X_test)
#
# np.percentile(X_train[:, 0], [0, 25, 50, 75, 100])

X = [[1., -1., 2.],
     [2., 0., 0.],
     [0., 1., -1.]]
X_normalized = preprocessing.normalize(X, norm='l2')
normalizer = preprocessing.Normalizer().fit(X)  # fit does nothing

print(X_normalized)
print(normalizer)

normalizer.transform(X)

normalizer.transform([[-1., 1., 0.]])
