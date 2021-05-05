# python是面向对象(object)的编程，以宏观、总体目标、任务为导向，
# 不像面向过程的编程拘泥于每一个子任务复用性较低。
# 我们目前所学习的都是python内置的object-盒子
# 为满足需求我们需要自定义一些对象-class-容器
# object是class的instance
# 自定义的class使用大写字母开头，大驼峰/帕斯卡命名法


# a = int(10)
# print(a, type(a))
#
#
# class Person:
#     name = 'swk'
#
#     def __init__(self):  # 自动调用执行
#         print("你好啊湖大")
#         pass
#
#     def say_hello(self):
#         print('Good morning! Boys and Girls!')
#         print('nihao', self.name)
#
#
# print(Person)
#
# p1 = Person()  # mc就是通过MyClass创建的对象，mc是MyClass的实例
# p2 = Person()  # mc就是通过MyClass创建的对象，mc是MyClass的实例
# p1.name = 'zbj'  # 先找自己（object）再找class（父亲）
# p2.name = 'fgh'  # 先找自己（object）再找class（父亲）
# print(p1.say_hello())
# print(p2.say_hello())

# # 使用class来创建对象object,class就是一个大家庭，object都是class的实例instance
# class MyClass:
#     age = 10
#
#     def say_hello(self):
#         print('hello,i come from %s Univ.' % self.name)
#
#
# print(MyClass)
#
# # 可以向object中添加属性变量
# p1 = MyClass()
# p1.name = 'Hunan'
# # del p1.name
# print(p1.name)
# print(p1.age)
# # 方法就是类中的函数，函数参数个数很明显，方法默认至少会传一个参数
# print(p1.say_hello())


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def say_hello(self):
#         print('大家好，我是%s' % self.name)
#
#
# p1 = Person('孙悟空')
# p2 = Person('猪八戒')
# print(p1)
# print(p1.say_hello())

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def names(self):
        print('get方法执行了~~~')
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


p = Person('猪八戒', 18)

print(p.names, p.age)
