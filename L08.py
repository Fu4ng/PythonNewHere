# --------------------------------------#
#
# Created by Fu4ng on 2017/7/25.
#
# 博文地址:
# --------------------------------------#




# try:
#     x = input("first number:")
#     y = input('second number:')
#     print(int(x)/int(y))
# except ZeroDivisionError:
#     print('No zero')


# # 屏蔽机制的开关
# class MuffledCalcular:
#     muffled = False
#     def calu(self,expr):
#         try:
#             return eval(expr)
#         except ZeroDivisionError:
#             if self.muffled:
#                 print('No zero')
#             else :
#                 raise
#
#
#
# #屏蔽关！
# calcu = MuffledCalcular()
# print(calcu.calu('10/0'))
#
# #屏蔽开！
# calcu.muffled = True
# print(calcu.calu('10/0'))

# 应用
one = {
    'name': 'kile',
    'age': 12,

}


# def out_info(one)
#     print('name:%s' %one['name'])
#     print('age:%s' %one['age'])
#     if occupation in one:
#         print('occupation:%s' %one['occupation'])
#     else :
#         pass
def out_info(one):
    print('name:%s' % one['name'])
    print('age:%s' % one['age'])
    try:
        print('occupation:%s' % one['occupation'])
    except:
        pass


out_info(one)

# one字典中没有occupation的Key,如果使用if去判断的话，效率不高，因为ifelse语句先判断一次，取值一次。而tryexcept直接假设有occupation这个Key，没有的话直接跳过。
