# --------------------------------------#
#
# Created by Fu4ng on 2017/7/17.
#
# 博文地址:
# --------------------------------------#

# 一个简单的数据库
# 字典使用人名作为键，每个人用另一个字典表示，其键‘Phone’'addr'分别表示它们的电话号码和地址

people = {
    'alice': {
        'phone': '9102',
        'addr': '363100'
    },
    'beth': {
        'phone': '5641',
        'addr': '25641'
    },
    'cecil': {
        'phone': '3547',
        'addr': '53545'
    }
}
# # 针对电话号码和地址使用的描述性表情，会在打印输出的时候用到
# labers = {
#     'phone': 'phone number',
#     'addr': 'address'
# }
# name = input('Name:').lower().strip()
# # 查找电话号码还是地址
# request = input("Phone number(p) or addr(a）:")
# key = request
# if request == 'p': key = 'phone'
# if request == 'a': key = 'addr'
# person = people.get(name, "NonePeople")
# label = labers.get(key, key)
# request = person.get(key, 'not available')
# if name in people: print("%s's %s is %s" % (name, label, request))


# # clear
# x = {}
# y = x
# x['key'] = 'value'
# print(y)
# x.clear()
# print(y)

# # copy 字典与字符串类型互转的方法
# x = {
#     'username': 'admin',
#     'machines': ['foo', 'bar', 'baz']
# }
# y = x.copy()
# y['username'] = 'ccc'
# y['machines'].remove('baz')
# print('x=%s' % str(x).strip('{').strip('}'))
# print(y)
#
# z = "{'a':1,'b':2}"
# zd = eval(z)
# print(zd)

# #setdefault
# d={}
# d.setdefault('name','N/A')
# print(d)
# d['name'] = 'Gumby'
# print(d)
