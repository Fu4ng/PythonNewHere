# --------------------------------------#
#
# Created by Fu4ng on 2017/7/15.
#
# --------------------------------------#

# #--- P28--日期转换
# months = ['January',
#           'February',
#           'March',
#           'April',
#           'May',
#           'June',
#           'July',
#           'August',
#           'September',
#           'October',
#           'November',
#           'December']
# # 以1-31为结尾的日期列表
# ending = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']
# year = input('Year:')
# month = input('month:')
# day = input('day:')
#
# month_num = int(month)
# day_num = int(day)
#
# print(months[month_num - 1] + ',' + day + ending[day_num - 1] + ',' + year)

# # ---P32---随句子变换而变换大小的盒子
# sentence = input('Sentence is:')
# screen_width = 80
# text_width = len(sentence)
# box_width = text_width +6
# left_margin = (screen_width - box_width)//2
# print(' '*left_margin + '+' + '_'*(box_width-5)+'+')
# print(' '*(left_margin)+ '|'+' '*text_width + '|')
# print(' '*(left_margin)+'|'+sentence + '|')
# print(' '*(left_margin)+ '|'+' '*text_width + '|')
# print(' '*left_margin + '+' + '_'*(box_width-5)+'+')

# # ---P33---检查用户名和PIN码
# database = [
#     ['bob', '1234'],
#     ['rose', '4567'],
#     ['loli', '6789']
# ]
# username = input('name:')
# pin = input('pin:')
# if [username, pin] in database: print('Access granted')

# # --用分片赋值删除元素
# x = [1, 3, 3, 3, 2]
# x[1:4] = []
# print(x)

# # # count函数
# x = [[1, 2], 1, [1, 2]]
# print(x.count([1, 2]))
# print(x.count(1))

# # append 与 extend
# a = [1, 2]
# b = [4, 5]
# a.append(3)
# print(a)
# a.extend(b)
# print(a)

# # insert
# x=[1,2,3,5]
# x.insert(3,"four")
# print(x)

# # pop 与 remove
# #pop返回被剔除的值，remove是一个没有返回值的原位置改变方法
# x = [1, 2, 5, 3, 4]
# print(x.pop(2))
# print(x.remove(3))
# print(x)
