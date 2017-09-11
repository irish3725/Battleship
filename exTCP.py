#!/usr/bin/python

import socket

#SERVER
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',80))
s.listen(1)

#CLIENT
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#ip in next line is my public ip I think.
s.connect(('192.168.124.255',80))
data = s.recv((BUFFER_SIZE))
s.close()

#SERVER
conn, addr = s.accept()
data = conn.recv(BUFFER_SIZE)
conn.send(data) # echo
conn.close()


