# 画子图
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2, figsize=(12, 6), sharex=False, sharey=True, subplot_kw={})
ax[0].scatter(np.arange(20), np.arange(20))
ax[1].plot(np.arange(20), np.arange(20))
plt.show()

# fig = plt.figure()
#
# # 支持的图像格式
# for item in fig.canvas.get_supported_filetypes():
#     print(item)
#
# plt.subplot(2,1,1)
# x = np.linspace(0, 10, 100)
# y = np.sin(x)
# plt.plot(x, y)
# fig.savefig('p.png')
# plt.show()


# # 后半部分：ax[1]或者plt效果是相同的，因为默认是在最后一张图上画图。
# fig, ax = plt.subplots(2)
# x = np.linspace(0, 10, 100)
# y = np.sin(x)
# z = np.cos(x)
# ax[0].plot(x, y + z)
#
# ax[1].plot(x, y, label='sinx')
# ax[1].plot(x, z, label='cosx')
# ax[1].legend(['tt', 'zz'])
# plt.show()

# import matplotlib
#
# matplotlib.rcParams['legend.numpoints'] = 5  # 更改默认值 - matplotlib.rcParams
#
# rng = np.random.RandomState(0)
# for marker in ['o', '.', ',', '+']:
#     plt.plot(rng.rand(5), rng.rand(5), marker, label="marker='{0}'".format(marker))
# plt.legend()
# plt.legend(numpoints=3)
# plt.show()

'''
# errorbar图
x = np.linspace(0, 10, 50)
dy = 0.2
y = np.sin(x) + dy * np.random.rand(50)
# plt.errorbar(x, y,yerr=dy,fmt='.k')
plt.errorbar(x, y, yerr=dy, fmt='o', color='black', ecolor='lightgray', elinewidth=3, capsize=0)
# plt.scatter(x, y, facecolor='y', edgecolors='r', s=80)
plt.plot(x, np.sin(x), color='y')
plt.show()
'''
# fig = plt.figure()
# ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4], xticklabels=[], ylim=(-1.2, 1.2))
# ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4], ylim=(-1.2, 1.2))
# x = np.linspace(0, 10)
# ax1.plot(np.sin(x))
# ax2.plot(np.cos(x))
# plt.show()
