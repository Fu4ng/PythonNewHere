# --------------------------------------#
#
# Created by Fu4ng on 2017/7/18.
#
# 博文地址:
# --------------------------------------#



# print('Age:',42)
#
# #序列解包
# x,y,z = 1,2,3
# print(x,y,z)
# cp = {'name': 'Robin', 'grilfriend': 'Ceil'}
# key, value = cp.popitem()
# print(key, value)

# name = input('Your name:')
# if name.lower().startswith('gumb'):
#     print('Hi')

# age =10
# assert 0<age<100
# age = -1
# assert 0<age<100 ,"The age must be realistic"
# x=1
# while x<100:
#     print(x)
#     x+=1

# 循环
# xl = [1,2,5,6]
# for x in xl:
#     print(x)
# for x in range(2,6):
#     print(x,',',end="")#输出不换行且加空格
##一些迭代工具
# name = ['anne','beth','george','damon']
# age = [12,56,33,55]
# 第一种
# for i in range(len(name)):
#     print(name[i],'is',age[i],'years old')
# #第二种,zip可以把来两个序列压缩在一起然后返回一个元组的列表
# for x in zip(name,age):
#     print(x)
#
# a1=[1,3,5]
# a2=[2,4,6]
# print(str(list(zip(a1,a2))).strip('[').strip(']'))

# print([x * x for x in range(10) if x % 3 == 0 ])

# girls = {'alice', 'bernice', 'clarice'}
# boys = {'chris', 'arnold', 'bob'}
# letterGirls = {}
# for girl in girls:
#     letterGirls.setdefault(girl[0], []).append(girl)
# print(list(b + '+' + g for b in boys for g in letterGirls[b[0]]))
# print(letterGirls)

##eval的安全性
# a=1
# x = input('请输入：')
# eval(x)


# def init(data):
#     data['first'] = {}
#     data['middle'] = {}
#     data['last'] = {}
#
#
# def lookup(data, label, name):
#     return data[label].get(name)
#
#
# def store(data, *fullNames):
#     for fullName in fullNames:
#         names = fullName.split()
#         if len(names) == 2: names.insert(1, ' ')
#         labels = 'first', 'middle', 'last'
#         for label, name in zip(labels, names):
#             people = lookup(data, label, name)
#             if people:
#                 people.append(fullName)  ##如果有人名字中有相同片段，就加上去
#             else:
#                 data[label][name] = [fullName]
#
#
# Mynames = {}
# init(Mynames)
# store(Mynames, 'Magus Lie Hetland', 'X Lie Hen')
# print(lookup(Mynames, 'middle', 'Lie'))

# def power(*one,**two):
#     if one and two:print(one,two)
#     else:print('No')
# power(1,2,x=2)
