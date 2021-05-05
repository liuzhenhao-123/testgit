# coding=utf-8
import matplotlib
import matplotlib.pyplot as plt
import random
import numpy as np

# font = {'family': 'MicroSoft YaHei',
#         'weight': 'bold',
#         'size': 'larger'}
# matplotlib.rc("font", **font)
# matplotlib.rc("font", family='MicroSoft YaHei', weight='bold')


x = range(120)
y = [random.randint(20, 35) for i in range(120)]
plt.figure(num=6, figsize=(16, 8), dpi=80)
plt.plot(x, y, linewidth=1, color='red', linestyle='--')
plt.xlim([0, 120])

# 将坐标轴上的刻度换为序列x或者自定义列表
_xtick_labels = ["10点{}分".format(i) for i in range(120)]
_xtick_labels += ["11点{}分".format(i) for i in range(120)]
plt.xticks(list(x)[::3], _xtick_labels[::3], rotation=45)
plt.yticks(range(min(y), max(y) + 2, 1))

# 66666666666666666666666666666666666666666666666666666666666666666666666
# 设置绘图样式
plt.style.use('classic')
x = np.linspace(-4, 4, 100)
y = np.sin(x)
fig = plt.figure()
plt.scatter(x, y)
plt.title('x-sin(x)')
plt.legend('sinx')
fig.savefig('save')

from IPython.display import Image

print(Image('save.png'))
# 查看系统支持的文件格式
print(fig.canvas.get_supported_filetypes())

# 666666666666666666666666666666666666666666666666666666666666
# 设置绘图样式
plt.style.use('seaborn-whitegrid')
fig = plt.figure()
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), color='g', linestyle='dashed', label='sinx')
plt.plot(x, x + 3, color='blue', linestyle='dashed', label='x+3')

# ax = plt.axes()
plt.xlim(0.5, 3)
plt.ylim(0, 5)
plt.axis([-1, 10, -2, 8])
plt.axis('equal')
plt.axis('tight')
plt.title('x-sin(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('sin(x)')

plt.show()


x = np.linspace(0, 10, 100)
fig, ax = plt.subplots(2)
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))

plt.show()
