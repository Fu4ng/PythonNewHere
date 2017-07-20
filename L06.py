# --------------------------------------#
#
# Created by Fu4ng on 2017/7/20.
#
# 博文地址:
# --------------------------------------#




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
#                 people.append(fullName)               ##如果有人名字中有相同片段，就加上去
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
