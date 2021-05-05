# 取余数
y = 0
for i in range(20):
    y += 5 * (10 ** i)
print(y)
print('以下是余数')
print(y % 84)

# #分隔提取字符
# string = 'My moral standing  is: 0.98765'
# moral_str = string.split(":")[1]
# print(moral_str)


# # 提取不含元音字母或者数字的元素
# # https://docs.python.org/2/reference/compound_stmts.html#the-for-statement
# words = ['HELLO', 'PH', 'Hi', 'read', 'tmp123', 'Our', 'vmr']
# for item in words:
#     item_temp = item.lower()
#     for ch in item_temp:
#         if ch in 'aeiou' or ch in '0123456789':
#             break
#     else:
#         print(item)

# # 引用形式输出
# va = 5
# print('Hello %d' % (va))

# # input
# temp = input("please input your name:")
# print("HELLO," + temp + "先生/女士")
