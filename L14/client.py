# --------------------------------------#
#
# Created by Fu4ng on 2017/8/6.
#
# 博文地址:
# --------------------------------------#


import socket

s = socket.socket

host = socket.gethostname()
port = 1234

s.connect((host, port))
print(s.recv(1024))
