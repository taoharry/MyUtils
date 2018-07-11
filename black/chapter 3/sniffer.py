#!usr/bin/env python
# coding:utf-8

import socket
import os


#解icmp数据包
host = "192.168.222.189"

#IPPROTO 协议中有ip,tcp,udp协议,可以理解为tcp/ip协议
if os.name == "nt":
	socket_protocol = socket.IPPROTO_IP
else:
	socket_protocol = socket.IPPROTO_ICMP

#sock_raw 调用sock核心层,即原始处理协议内容
sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW,socket_protocol)

sniffer.bind((host,0))

sniffer.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)

if os.name == "nt":
	sniffer.ioctl(socket.SIO_RECVALL,socket.RCVALL_ON)

print sniffer.recvfrom(65565)

if os.name == "nt":
	sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)