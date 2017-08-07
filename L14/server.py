# --------------------------------------#
#
# Created by Fu4ng on 2017/8/6.
#
# 博文地址:
# --------------------------------------#

import socket

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    s.send('Thank you for connecting!')
    c.close()
