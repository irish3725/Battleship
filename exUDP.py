#!/usr/bin/python

import socket

#SERVER
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',5000))

#CLIENT
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#ip in next line is my public ip I think
s.sendto(bytes('hello'),('192.168.124.255',5000))

#SERVER
data, addr = s.recvfrom(BUFFER_SIZE)

