# 课时7
stus = ['孙悟空', '猪八戒', '沙和尚']
# stus.append('唐长老') # 添加到最后
# stus.insert(1,'唐朝长老') # 插入到指定位置
# stus.extend('唐朝长老')
stus.extend(['唐朝长老', '白骨精'])  # 可添加多个
# stus += (['唐朝长老', '白骨精'])
# stus.clear() # 清空
res = stus.pop(2)  # 删除指定位置元素或最后一个
print(res)  # 返回删除值
print(stus)
stus.remove('猪八戒')  # 删除指定元素(有多个相同值只返回第一个)
print(stus)
stus.reverse()  # 颠倒顺序
print(stus)

stus2 = list('zxetsdrcytfuvgyhunijmko.l;,kmjnhb')
# stus2=list([4,1,6849,684981,38,47,3,7])
stus2.sort(reverse=True)  # 默认是升序排列(False)
print(stus2)
