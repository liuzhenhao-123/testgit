# 《Python光速入门》09.文件处理_哔哩哔哩 (゜-゜)つロ 干杯~-bilibili https://www.bilibili.com/video/BV1MT4y1G7pD
# # 自己处理异常Exception，不要让python处理异常
# try:
#     x = float(input('Please input a number:'))
# except Exception as e:
#     print('Error:',e.args[0])
# finally:
#     x = 333334
# print(x)

# # 避免报错的方式打开一个文本文件：try
# try:
#     f = open('23.txt', 'r')
#     lines = f.readlines()
#     print(lines)
#     f.close()
# except:
#     print('ERROR')

# # 免于增加close的语法:with as
# with open('2.txt', 'r') as f:
#     f = open('2.txt', 'r')
#     lines = f.readlines()
#
# lis = []
# for line in lines:
#     line = line.strip()  # 开头和空行
#     tokens = line.split('。')
#     for token in tokens:
#         if len(token) > 0:
#             lis.append(token)
# print(lis)

# lamda,filter,extend,append
import re

with open('2.txt', 'r') as f:
    lines = f.readlines()

sents = []
for line in lines:
    line = line.strip()  # 开头和空行
    tokens = line.split('。')
    sents.extend(list(filter(lambda x: len(x) > 0, tokens)))
print(sents)

# lens=[]
# for token in sents:
#     lens.append(len(token))

lens = [len(token) for token in sents]
print(lens)

# 正则表达式
regex = 'student'
regex = '8.'  # .是任意字符的意思
regex = '[一新]'  # 有任何一个字都会返回
regex = '[0-9]'  # 0-9数字通配符
regex = '2[0-9]{3}'  # 2之后至少跟3个数字
for sent in sents:
    if re.search(regex, sent) is not None:
        print(sent)
