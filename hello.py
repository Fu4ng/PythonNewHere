# --------------------------------------#
#
# Created by Fu4ng on 2017/7/14.
#
# --------------------------------------#


# 如何导入自己创建的模块。
# 　第一版
# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a+b
#         n = n +1

# 第二版
# def fab(max):
#     n, a, b = 0, 0, 1
#     list = []
#     while n < max:
#         list[n] = b
#         a, b = b, a+b
#         n = n +1


# 第三版
# class Fab(object):
#     def __init__(self,max):
#         self.max =max
#         self.n, self.a, self.b = 0, 0, 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#        if self.n < self.max:
#             r = self.b
#             self.a, self.b = self.b,self.a + self.b
#             self.n +=1
#             return r
#        raise StopIteration() #迭代器没有更多的值了，异常处理

# 第四版
# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a+b
#         n = n +1
