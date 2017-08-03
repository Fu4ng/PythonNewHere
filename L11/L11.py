# --------------------------------------#
#
# Created by Fu4ng on 2017/8/3.
#
# 博文地址:
# --------------------------------------#


# 文件操作
import time

# with open("test.txt",'wb',buffering=0) as f:
#     f.write(b"hello!")
# #无缓冲写入文件 http://blog.csdn.net/junloin/article/details/76626156

# with open('test.txt','r+b',buffering=0) as f:
#     f.write(b'01234567890123456789')
#     f.seek(5)
#     f.write(b'hello world!')
#     f.seek(0)
#     fr = f.read()
#     print(fr)

# 文件迭代
f = open('test.txt', 'r+')
for line in f.read():
    print(line.strip('\n'))
f.close()
