# https://www.bilibili.com/video/BV1CX4y1374d?p=21&spm_id_from=pageDriver

from urllib.request import urlopen
import requests

'''
url = "http://www.baidu.com"
res = urlopen(url)
# print(res.read().decode("utf-8"))
with open("m.html", mode="w") as f:
    f.write(res.read().decode("utf-8"))
'''

'''header={
    'User-Agent':"Windows Android "
}
query=input("输入关键词")
url = f"http://www.sogou.com/web?query={query}"
resp = requests.get(url,headers=header)
print(resp.text)'''

'''url = "https://fanyi.baidu.com/sug"
s = input("请输入待翻译的词语")
dat = {
    "kw": s
}
resp = requests.post(url, data=dat)
print(resp.json())
'''
import re
str="hu233.22nan.u n8.5iv2 3.3ers.ity"

# 返回列表
res=re.findall("\d+\.[0-9]",str)

# 返回迭代器
it=re.finditer(r"[0-9]+",str)
for i in it:
    print(i)

# 找到一个结果就返回
ss=re.search(r"[0-9]+",str)
print(ss.group())

# 从头匹配
ss=re.match(r".",str)
print(ss.group())

# 预加载正则
obj=re.compile("\d+\.[0-9]")
res=obj.findall(str)
print(res)