from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
import numpy as np

# X_train = np.array([[1., -1., 2.],
#                     [2., 0., 0.],
#                     [0., 1., -1.]])
#
# scaler = preprocessing.StandardScaler().fit(X_train)
# print(scaler)
#
# print(scaler.mean_)
#
# print(scaler.scale_)
#
# X_scaled = scaler.transform(X_train)
# print(X_scaled)

"""X, y = make_classification(random_state=42)
print(X.shape)
print(y.shape)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=105)
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
# pipe = make_pipeline(StandardScaler(), LogisticRegression())
# pipe.fit(X_train, y_train)  # apply scaling on training data
# print(pipe)
# print(pipe.score(X_test, y_test))  # apply scaling on testing data, without leaking training data.

scale = StandardScaler().fit(X_train)
X_scaled = scale.transform(X_train)

logi = LogisticRegression().fit(X_scaled, y_train)

model_y=logi.predict(scale.transform(X_test))
print(model_y)

print(y_test)
print(logi.score(scale.transform(X_test), y_test))  # apply scaling on testing data, without leaking training data.
"""

X_train = np.array([[ 1., -1.,  2.],
                    [ 2.,  0.,  10.],
                    [ 0.,  1., -15.]])

max_abs_scaler = preprocessing.MaxAbsScaler()
X_train_maxabs = max_abs_scaler.fit_transform(X_train)
print(X_train_maxabs)



X_test = np.array([[ -3., -1.,  4.]])
X_test_maxabs = max_abs_scaler.transform(X_test)
print(X_test_maxabs)

print(max_abs_scaler.scale_)