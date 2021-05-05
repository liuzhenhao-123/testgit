import numpy as np
from sklearn.model_selection import KFold,RepeatedKFold
from sklearn.model_selection import cross_val_score,train_test_split,ShuffleSplit,KFold,RepeatedKFold

X = ["a", "b", "c", "d","d","e","h","er","erer","342"]
kf = RepeatedKFold(n_splits=4,n_repeats=3)

for train, test in kf.split(X):
    print("%s %s" % (train, test))

y=np.random.random(10)
train_test_split(X,y,stratify=y,test_size=0.3,shuffle=True)

