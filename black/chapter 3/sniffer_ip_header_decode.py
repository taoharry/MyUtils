#!usr/bin/env python
# coding:utf-8

import socket
import os
import struct
from ctypes import *

host = "192.168.222.189"

class IP(Structure):
	_fields_ = [
		("ihl",			c_ubyte, 4),  # ip head length:头长度
		("version",		c_ubyte, 4),  # 版本
		("tos", 		c_ubyte),  # 服务类型
		("len", 		c_ushort),  # ip数据包总长度
		("id", 			c_ushort),  # 标识符
		("offset", 		c_ushort),  # 片偏移
		("ttl", 		c_ubyte),  # 生存时间
		("protocol_num",c_ubyte),  # 协议数字,应该是协议类型,这里用数字来代表时哪个协议, 下面构造函数有设置映射表
		("sum", 		c_ushort),  # 头部校验和
		("src", 		c_uint32),  # 源ip地址
		("dst", 		c_uint32) # 目的ip地址

	]

	def __new__(self, socket_buffer=None):
		return self.from_buffer_copy(socket_buffer)

	def __init__(self, socket_buffer=None):
		print dir(self)
		self.protocol_map = {1:"ICMP",6:"TCP",17:"UDP"}
		#可读性更强的ip地址
		self.src_address = socket.inet_ntoa(struct.pack("@I", self.src))
		self.dst_address = socket.inet_ntoa(struct.pack("@I", self.dst))

		try:
			print self.protocol_num
			self.protocol = self.protocol_map[self.protocol_num]
		except:
			self.protocol = str(self.protocol_num)


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

try:
	while True:
		# 读取数据包
		raw_buffer = sniffer.recvfrom(65565)[0]
		print raw_buffer
		# 将缓冲区的前20个字节按IP头进行解析
		ip_header = IP(raw_buffer[0:32])

		# 输出协议和通信双方IP地址
		print "Protocol: %s %s ->  %s" % (ip_header.protocol, ip_header.src_address, ip_header.dst_address)

# 处理CTRL-C
except  KeyboardInterrupt:

	# 如果运行再Windows上,关闭混杂模式
	if os.name == "nt":
		sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)



