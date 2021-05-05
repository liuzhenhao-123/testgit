import matplotlib.pyplot as plt
import numpy as np

plt.figure(num=1)
x = np.linspace(-2, 1, 100)
y1 = (2 * x + 1)
y2 = (2 * x + 1) ** 2
l1, = plt.plot(x, y1)
l2, = plt.plot(x, y2)
plt.legend(handles=[l1, l2], labels=['This is legend1', 'This is legend2'])
plt.text(-0.7, 1.3, r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_i$')
plt.show()

plt.figure(num=2)
plt.plot([1, 2, 3, 4, 5, 6], [19, 5, 3, 25, 6, 9])
plt.text(3, 15, r'$\mu=100$', fontsize=15)
plt.title('郑玄波$y=cos(2\pi x)$', fontproperties='SimHei', fontsize=14)
plt.annotate(r'$\mu=100$', xy=(3, 20), xytext=(2, 15),
             arrowprops=dict(facecolor='black', shrink=0.1, width=1))
plt.grid(True)
plt.show()

#相关系数，Pearson系数等等数据分析
plt.figure(num=3)
x = np.arange(1.895, 1.896, 0.0001)
y = np.sin(x) - x / 2
plt.plot(x, y)
plt.xticks(np.arange(1.895, 1.896, 0.0001))
plt.grid(True)
plt.show()


print(np.log2(50*np.pi)-1)
print(np.log(0.34/100000)/np.log(0.66))