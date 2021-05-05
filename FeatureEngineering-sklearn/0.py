from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn.feature_selection import RFE
import matplotlib.pyplot as plt

" 递归特征消除法 Wrapper法 feature_selection 非统计学方法"
# Load the digits dataset
digits = load_digits()
X = digits.images.reshape((len(digits.images), -1))
y = digits.target
print(digits.images.shape)

a = 968
plt.matshow(digits.images[a].reshape(8, 8), cmap=plt.cm.Blues)
plt.title(y[a])
plt.show()


# Create the RFE object and rank each pixel
# 基估计器SVC
svc = SVC(kernel="linear", C=1)
#  feature_selection 方法RFE
rfe = RFE(estimator=svc, n_features_to_select=1, step=1)
rfe.fit(X, y)
ranking = rfe.ranking_.reshape(digits.images[0].shape)
print(ranking.shape)

# Plot pixel ranking
plt.matshow(ranking, cmap=plt.cm.Blues)
plt.colorbar()
plt.title("Ranking of pixels with RFE")
plt.show()
