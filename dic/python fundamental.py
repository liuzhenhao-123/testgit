'''
# list，有序，可增加可删除元素
classmates=['Mike','Jhon','Marry']
print(classmates)
# 要附加元素在list末尾
classmates.append('LZH')
print(classmates)
print(classmates[-2])
# 要附加元素在list的指定位置
classmates.insert(1,'LOUs')
print(classmates)
# 要删除list末尾的元素
classmates.pop()
print(classmates)
# 要删除list指定位置的元素
classmates.pop(1)
print(classmates)
# 直接替换元素
classmates[1] = 'Sarah'
print(classmates)
# 打印长度
print(len(classmates))

# tuple与list类似，但是他用的是圆括号；不能增删改他的元素；
# 单个元素的话，要加一个逗号，否则会有歧义
a=(2,)
print(a)
'''

L = [['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']]
print(L[1][3])

# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name)
#
# sum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#    sum = sum + x
# print(sum)
#
# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)


# L = ['Bart', 'Lisa', 'Adam']
# for es in L:
#     print('Hello,'+es)


# break和continue
# break是彻底退出循环
# continue是跳出此次循环

# names = ['Michael', 'Bob', 'Tracy']
# scores = [95, 75, 85]
# print(scores[names.index('Michael')])


# dict优点是查询速度快
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d['Michael'] = 99
print(d['Michael'])
print('Bob' in d)
print(d.get('Thomas'))

# set是无序集合，不带重复的，没有value值，只有key，可以做交集并集等运算
