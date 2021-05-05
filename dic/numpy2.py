import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])
# print(a)
# print(a.shape)
# print(a.size) #size=元素总个数
# print(a.ndim)

# b=np.arange(12).reshape(3,4)
# print(b)

# c=np.linspace(1,18,18)
# print(c)

# d=np.array([[2,5,3],
#             [9,3,4]])
# print(d)
# print(a+d)

# e=np.random.random((2,3))
# print(e)
# print(np.sum(e))
# print(np.min(e))
# print(np.max(e))
# print(np.sum(e,axis=1))

# f = np.array([[6, 2, 5],
#               [2, 5, 9],
#               [6, 80, 2]])
# print(f)
# print(np.argmax(f)) #矩阵中最大的数值对应的序号
# print(f.transpose())
# print(f.T)

# 设置一个范围，超过范围的大数或者小数都被替换为最大设置值或者最小设置值
# g=np.array([[26,3,12],
#             [3,5,8],
#             [-31,6,-2]])
# print(g)
# print(np.clip(g,1,12))
#
# h=np.arange(3,15).reshape(3,4)
# print(h)
# print(h.flatten())
# for item in h.flat:
#     print(item)

# 组合叠加的方法
# i = np.array([[1, 2, 3],
#               [4, 5, 6]])
# j = np.array([[2, 5, 3],
#               [9, 3, 4]])
# # k=np.hstack((i,j))
# print(k)
# l=np.vstack((i,j))
# print(l)
# # # # # # # # 1为行，0为列 # # # # # # # # #
# m=np.concatenate((i,j,j),axis=1)
# print(m)

# n=np.arange(12).reshape(3,4)
# print(n)
# print(np.split(n,3,axis=0))
# print(np.hsplit(n,4))
# print(np.vsplit(n,3))

'''
o=np.arange(12,dtype=np.float).reshape(3,4)
print(o)
# 只是复制下来了，不会在后续跟着变动
p=o.copy()
# 会同步变动的
q=o
r=p

o[1][3]=0.6
print(o)
print(r)
'''

X = np.array([1, 5, 63, 6, 2, 3, 5, 8, 3, 4, 6, 2, 1, 7])
print(X)
print(np.unique(X))
'''

X=np.array([[1,5,6],
           [3,8,4]])
print(X)
print(X.sum(axis=0))
print(X.sum(axis=1))
'''
