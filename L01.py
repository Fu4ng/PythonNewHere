# Created by Fu4ng on 2017/7/14





# 我把代码注释了，因为都是一些小代码块，需要改写哪部分代码在把前面的#删掉就可以了。

#博文：http://blog.csdn.net/junloin/article/details/75106797
#     http://blog.csdn.net/junloin/article/details/75119431
# 模板导入

# # 第一种方法:
#
# import math
# a = math.floor(32.9) #floor函数的作用是向下取整数
# print(a)
#
# # 第二种办法：
#
# from math import sqrt
# b = sqrt(9)
# print(b)

# sqrt复数

# import cmath
#
# c = cmath.sqrt(-1)
# print(c)

# #命名冲突
# from cmath import sqrt
#
# d = sqrt(-1)
# e = sqrt(1)
# print(d)
# print(e)

# # 字符串
# x = "hello world"
# y = "let's go "
# print(y + x)
# print('"hello world",she said')
# print(repr("hello world"))
# print(repr(100000))
# print(str("hello world"))
# # 用repr函数会比str多出一个引号
# # str和 int long 一样，是一种类型。而repr仅仅是函数
#
# #input 和 raw_input
#
# name = input("what is your name?")
# print(name)
# number =input("what is your number ")
# print(number)
#
# # 长字符串
# print('111111111111111111111111111'
#       '111111111111111111111111')
# print('''2222222222用三个引号能换行222
#         2222222222222''')

# #原始字符串
# print('C:\nowhere')  #这个是非原始字符串，因为检查到有\n换行符存在，输出时会换行
# print (r'C:\nowHere') #原始字符串以r开头，可以存放\，但是原始字符串最后一个字符不能是\
# # 如果有硬性要求需要最后一个字符必须为\ ,那么我们应该对\进行转义，如下
# print(r'C:Program Files\foo\bar' '\\')

# #Unicode
# print(u"hello world")

##模版字符串
# from  string import Template
# s = Template ("$x,Python $x!")
# print(s.substitute(x = 'wow'))
# #替换字段是单词的一部分，那么参数名就必须用括号扩起来，从而指明结尾
# s = Template("It's ${x}thon")
# print(s.substitute(x = 'Py'))
