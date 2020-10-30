# -*- codeing = utf-8 -*-
# @Time : 2020/10/30 15:44
# @Author : yexiaozhu
# @File : gopherclient.py
# @Software : PyCharm

import socket
import sys

port = 70
host = sys.argv[1]
filename = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

s.sendall((filename + "\r\n").encode(encoding='UTF-8'))

while 1:
    buf = s.recv(2048).decode()
    if not len(buf):
        break
    sys.stdout.write(buf)