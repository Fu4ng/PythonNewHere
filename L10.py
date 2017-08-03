# --------------------------------------#
#
# Created by Fu4ng on 2017/8/2.
#
# 博文地址:
# --------------------------------------#

import time
import re

###time
# t = (2008, 1, 21, 12, 2, 56, 0, 21, 0)  # 2008.1.21 12：2：56，星期一，第21天，无夏令时
# t_str = "Mon Jan 21 12:02:56 2008"
# # 时间元组转字符串
# print(time.asctime(t))
# # 字符串转时间元组
# print(time.strftime(t_str))
# # 时间元组转换成秒数
# print(time.mktime(t))
# # 不做任何事几秒
# time.sleep(1)
# print("————————1秒过去了——————")
# # 当前时间,秒数
# print(time.time())
# # 秒数转成日期元组
# t_now = time.time()
# print(time.localtime(t_now))
#
# # 打印出当前时间
# now = time.localtime(t_now)
# print('%d年%d月%d日 %d:%d:%d' %now[0:6])



###re

s = "http://www.python.org"
p = "w*\.python\.org"
pc = re.compile(p)
# compile将字符串形式书写的正则表达式转成pattern模式，下面两个表达式等值
if re.search(p, s):
    print('Y')
if pc.search(s):
    print('Y')
# match函数从字符串开始处匹配
if re.match(r"ht.*://", s):
    print('Y')

# split 分割字符串
# text = "A...B,,C D"
# p = "[., ]*"
# f = re.split(p,text)
# print(" ".join(f))

# findall 返回所有符合的匹配项
pat = '[a-zA-Z]+'
text = "as?/a as???.???fa,sl.mFAS%.,?SAF asf"
f = re.findall(pat, text)
print(f)
# 查找标点符号
pat = "[?/.,]+"
f = re.findall(pat, text)
print(f)

# sub
pat = '{name}'
text = 'Dear{name}...{name}..{name}!'
f = re.sub(pat, 'Mr.Lol', text, count=2)  # count参数是对前面几个进行代换
print(f)
