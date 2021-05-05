# import os
# print(os.path.join('demo', 'exercise'))

# import os
# myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
# for filename in myFiles:
#     print(os.path.join('C:\\demo\\exercise', filename))

import os
# print(os.getcwd())
# os.chdir('C:\\Windows\\System32')
# print(os.getcwd())

# 除了经常使用 .\ 表示当前所在目录之外，还会用到 ..\ 表示当前所在目录的父目录。

# 移除已有文件
# os.remove("a.txt")

# # 以某种方式打开文件
# file = open("a.txt",encoding="utf-8",mode='r+')
# print(file)
# print(file.encoding)
# print(file.mode)
# print(file.closed)
# print(file.name)
# # 关闭文件
# file.close()
# # 判断文件是否已关闭
# print(file.closed)

# a.txt 文件内容为：C语言中文网
# f.read()为读取全部内容
# f = open("a.txt", mode='r',encoding="utf-8",buffering=True)
# while True:
#     # 每次读取一个字符
#     ch = f.read(1)
#     # 如果没有读到数据，跳出循环
#     if not ch:
#         break
#     # 输出ch
#     print(ch, end='\n')
# f.close()

# f = open("a.txt", 'r', True)
# while True:
#     # 每次读取一行
#     line = f.readline(3)
#     # 如果没有读到数据，跳出循环
#     if not line: break
#     # 输出line
#     print(line)
# f.close()


# 写文件write

