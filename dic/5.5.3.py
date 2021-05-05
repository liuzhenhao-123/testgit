from sklearn.datasets import fetch_20newsgroups

data = fetch_20newsgroups()
print(data.target_names)

categories = ['talk.religion.misc', 'soc.religion.christian', 'sci.space', 'comp.graphics']
train = fetch_20newsgroups(subset='train', categories=categories)
test = fetch_20newsgroups(subset='test', categories=categories)

print(train.data[5])

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

model = make_pipeline(TfidfVectorizer(), MultinomialNB())

model.fit(train.data, train.target)
labels = model.predict(test.data)

from sklearn.metrics import confusion_matrix

mat = confusion_matrix(test.target, labels)
import seaborn as sns

sns.set()

sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=train.target_names, yticklabels=train.target_names)
import matplotlib.pyplot as plt

plt.xlabel('true label')
plt.ylabel('predicted label')

plt.show()


def predict_category(s, train=train, model=model):
    pred = model.predict([s])
    return train.target_names[pred[0]]


print('预测：{}'.format(predict_category('sending a playload to the ISS')))
print('预测：{}'.format(predict_category('discussing Islam atheism')))
print('预测：{}'.format(predict_category('determining the screen resolution')))