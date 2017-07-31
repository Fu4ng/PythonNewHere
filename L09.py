# --------------------------------------#
#
# Created by Fu4ng on 2017/7/30.
#
# 博文地址:
# --------------------------------------#


# 魔法方法

class Bird:
    def __init__(self):
        self.hungry = 1

    def eat(self):
        if self.hungry:
            print('ahhhh')
        else:
            print('no,thx')
            self.hungry = 0


class songBird(Bird):
    def __init__(self):
        super(songBird, self).__init__()
        self.sound = 'sqqqq'

    def sing(self):
        print(self.sound)


sb = songBird()
sb.sing()
sb.eat()

# 基本的序列和映射规则
#
x = ['a', 'b', 'c', '1', '2']
print(x.__len__())
# x[key]就是调用x.__getitem__(key)
print(x.__getitem__(1))
# x[key]=value 调用 x.__setitem(key,value)
x.__setitem__(1, '2')
print(x.__getitem__(1))
x.__delitem__(1)  # 完全删除掉这个项，让后面的项向前进一位
print(x.__getitem__(1))


# ## 创建一个无穷序列
#
def checkIndex(key):
    """
    所给的键是正确的索引吗？
    key应该是一个非负数的整数
    如果不是整数，引发TypeError
    如果是复数引发IndexError
    :param key:
    :return:
    """
    if not isinstance(key, (int)): raise TypeError  # 判断key是不是int或long类型
    if key < 0: raise IndexError


class ArithmeticSequence:
    def __init__(self, start=0, step=0):
        """

        :param start:序列中第一个数
        :param step: 步长
        changed:被改变的项的字典
        """
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        """
        从序列中获取一个数
        :param item:
        :return:
        """
        checkIndex(key)
        try:
            return self.changed[key]  # 检查这个值是否被修改了
        except KeyError:
            return self.start + key * self.step  # 否则返回正常的数，因为是有序的，所以可以计算出这值

    def __setitem__(self, key, value):
        """
        修改无穷序列中的一个项

        把他存到changed字典中
        :param key:
        :param value:
        :return:
        """
        checkIndex(key)
        self.changed[key] = value


s = ArithmeticSequence(0, 5)
print(s[12])
s[12] = 12
print(s[12])


# 访问器
class Rectangle():
    def __init__(self):
        self.height = 0
        self.width = 0

    def getSize(self):
        return self.height, self.width

    def setSize(self, size):
        self.height, self.width = size

    size = property(getSize, setSize)


r = Rectangle()


class Screen():
    """
    长宽两个属性，还有一个resolution的只读属性
    """

    @property
    def size(self):
        return self.height, self.width

    @size.setter
    def size(self, size):
        self.height, self.width = size

    @property
    # 如果只设置property 没有设置setter那么就是只读属性
    def resolution(self):
        return self.height * self.width


s = Screen()
s.size = (1, 2)
print(s.size)
print(s.resolution)
