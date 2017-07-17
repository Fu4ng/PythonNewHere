# --------------------------------------#
#
# Created by Fu4ng on 2017/7/16.
#
# 博文地址：http://write.blog.csdn.net/mdeditor#!postId=75119431
# --------------------------------------#


# format1 = 'hello,%s,%s nough for ya?'
# values = ('world','hot')
# print(format1 % values)

# from math import pi
# print('%10f' % pi)
# print('%10.2f' % pi)
# print('%010.2f' % pi)
# print('%-10.2f' % pi)
# x = 'abcde'
# print('%.2s' %x)
# #关于字符串对齐的方法：http://jingyan.baidu.com/article/77b8dc7fe1371b6174eab691.html

# # 字符串方法
# #find
# x='deacddef'
# y = x.find('de')
# print(y)
# z = x.find('de',2,5)  #设置起始点和结束点参数
# print(z)

# #join和split
#
# s = ['1','2','3']
# q ='+'
# print(q.join(s))
# m =(' ','usr','bin','env')
# print('C:'+'/'.join(m))
# print(q.join(s).split('+'))
# print(('C:'+'/'.join(m)).split('/'))

# #replace
# x = 'This is a test'
# print(x.replace('is','eez'))

# #strip
# x = '         去除两侧空格             '
# print(x.strip())
# x= 5*'+'+x+5*'+'
# print(x)
# print((x.strip('+')).strip())

# translate
x = '123456'
tab = x.maketrans('1235', 'abce', '6')
print(x.translate(tab))


# translate
