from ipython_genutils.py3compat import execfile


class C(object):
    @staticmethod
    def f():
        print('runoob')


C.f()  # 静态方法无需实例化
cobj = C()
cobj.f()
ss=all(['a', 0, 'c', 'd'])
print(ss)

seq = ['one', 'two', 'three', 'four', 'five']
for i, element in enumerate(seq):
    print(i, element)

print(ord('A'))

dict = {'runoob': 'runoob.com', 'google': 'google.com'}

print(str(dict))


execfile('hello.py')
