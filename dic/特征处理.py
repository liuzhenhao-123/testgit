import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_extraction import DictVectorizer

'''
fruits = pd.DataFrame({'数值特征': [5, 6, 7, 8, 9],
                       '类型特征': ['watermelon', 'banana', 'orange', 'apple', 'grapes']})
print(fruits)
fruits_dum = pd.get_dummies(fruits)
print(fruits_dum)
# 先把数值型转化为字符型，然后再get_dummies
fruits['数值特征'] = fruits['数值特征'].astype(str)
fruits_dum2 = pd.get_dummies(fruits, columns=['数值特征'])
print(fruits_dum2)
'''
# 特征化向量
data = [{'price': 850000, 'rooms': 4, 'neighborhood': 'Queen Anne'},
        {'price': 700000, 'rooms': 3, 'neighborhood': 'Fremont'},
        {'price': 650000, 'rooms': 3, 'neighborhood': 'Wallingford'},
        {'price': 600000, 'rooms': 2, 'neighborhood': 'Fremont'}, ]
vec = DictVectorizer(sparse=False, dtype=int)
vec.fit_transform(data)
print(vec.get_feature_names())