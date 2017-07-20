# #repr和str
# x='avbc'
# print(x)
# print(str(x))
# print(repr(x))  #带引号 给python看的
# print(type(repr(x)))


# 创建类
class Person:
    __age = 15

    def getAge(self):
        print(self.__age)

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print('Hi,i am %s' % self.name)


# 继承
class studen(Person):
    def getNumber(self, number):
        number = number
        print(number)


foo = Person()
foo.setName('hel')
foo.getName()
foo.greet()
foo.getAge()
foo2 = studen()
foo2.setName('Genji')
foo2.getNumber('0011')

# 从非空序列中随机抽元素
import random

print(random.choice(range(100)))
