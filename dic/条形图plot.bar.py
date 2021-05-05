# 条形图plot.bar
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('students.csv')
print(len(data))
print('前5行数据：\n', data.head())

data = data.sort_values(by='age')
print(data)
data = data.reset_index()
print(data)

plt.figure(num=1)
groupby_user = data.groupby('age').size()
print(groupby_user)
groupby_user.plot.bar(title='Distribution of ages')

plt.figure(num=2)
groupby_user = data.groupby('gender').size()
groupby_user.plot.bar(title='Distribution of genders')

plt.figure(num=3)
data = data[(data['age'] >= 18) & (data['age'] <= 21)]
groupby_user = data.groupby('gender').size()
groupby_user.plot.bar(title='Distribution of genders2')
plt.show()
