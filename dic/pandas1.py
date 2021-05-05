print("==========================================")
print("B站莫烦pandas")
print("==========================================")

import numpy as np
import pandas1 as pd

'''
# 构造序列或表数据
a = pd.Series([3, 2, 56, np.nan, 1, "big", "matab", "cat"])
print(a)
b = pd.date_range('20200103', periods=6)
print(b)
c = pd.DataFrame(np.random.randn(6, 4), index=b, columns=['a', 'b', 'c', 'd'])
print(c)
print("=======================================")
d = pd.DataFrame(np.arange(36).reshape(4, 9))
print(d)
print("=======================================")
e = pd.DataFrame(np.random.randn(6, 4), columns=['A', 'B', 'C', 'D'])
print(e)
print("=======================================")
print(e['A'])
print(e.A)
print(e[2:5])
print("=======================================")
# 建立行列索引,axis=0,行,axis=1,列
f = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("ABCD"))
print(f)
print("=======================================")
'''
'''
# df2 = pd.DataFrame({'A': 1.,
#                     'B': pd.Timestamp('20180310'),
#                     'C': pd.Series(1, index=list(range(4)), dtype='float32'),
#                     'D': np.array([3] * 4, dtype='int32'),
#                     'E': pd.Categorical(["test", "train", "test", "train"]),
#                     'F': 'foo'
#                     })
# print(df2)
# print(df2.index)  # 行标签
# print(df2.columns)  # 列标签
# print(df2.values)  # 每行的值
# print(df2.describe())  # 对于数值型数据计算均值、标准差等
# print(df2.T)  # 转置矩阵
# print(df2.sort_index(axis=1, ascending=False))  # 按照倒序型排列序（列）
# print(df2.sort_values(by='E'))  # 按照E列值进行排序
'''
'''
dates = pd.date_range('20180310', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)
# 选择
# select by label
print(df.loc['20180312']) #打印对应行
print(df.loc[:,['A','B']]) #打印AB两列
# select by location
print(df.iloc[1:3, [1, 3]])
print(df[df.A > 8])
# 修改值
df.iloc[2, 2] = np.nan
print(df)
df.loc['20180312','B']=2222
print(df)
df.A[df.A>4]=0
print(df)
df.A = np.nan
print(df)
# 添加一列E（必须对应到行标）
df['E']=pd.Series([1,3,5,4,2,6],index=pd.date_range('20180310',periods=6))
print(df)
print(df.dropna(axis=0, how='any'))  # 0对行进行操作 1对列进行操作 any:只要存在NaN即可drop掉; all:必须全部是NaN才可drop
print(df.fillna(value=0))  # 将NaN值替换为0
print(pd.isnull(df))  # 矩阵用布尔来进行表示 是nan为ture 不是nan为false
print(np.any(df.isnull()))  # 判断数据中是否会存在NaN值
'''

# 拼接数据表
# df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
# df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
# df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['c', 'd', 'e', 'f'], index=[3, 4, 5])
# print(df1)
# print(df2)
# print(df3)
# res = pd.concat([df1, df2], axis=1, join='outer', join_axes=[df1.reindex])  # 默认为outer,不会丢掉任何一组数据
# print(res)
# res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)  # 忽略原有序号，重新编号
# print(res)

'''
# 保存文件
# students = pd.read_csv("./students.csv")
# print(students)
# students.to_pickle('student.pickle')
'''
# # 打印行
# with open(“C:\Users\Admin\PycharmProjects\first chapter\test.csv”) as f:
#     for line in f:
#         print(line)


# 【python教程】数据分析——numpy、pandas、matplotlib_哔哩哔哩 (゜-゜)つロ 干杯~-bilibili  https://www.bilibili.com/video/av57023791?p=26

# d1 = {"name": ["xiaoming", "xiaogang", "xiaozhu"],
#       "age": [16, 18, 20],
#       "city": ["BJ", "SZ", "NJ"]}
# print(pd.DataFrame(d1))


# d2 = [{"name": "xiaoming", "age": 16, "city": "BJ"},
#       {"name": "xiaogang", "age": 18, "city": "SZ"},
#       {"name": "xiaozhu", "age": 20, "city": "NJ"}]
# y2 = pd.DataFrame(d2)
# print(y2)
# print(y2.head(2)) #打印前n行
# print(y2.values)#打印每一行的内容
# print(y2.index)#打印行标
# print(y2.columns)#打印列标
# print(y2.shape)#打印维度
# print(y2.ndim)
# print(y2.info)

'''
data = pd.Series([0.25, 0.5, 0.75, 1], index=[2, 3, 5, 8])
print(data.values)
print(data.index)
print(data[2])
'''