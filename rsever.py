#!usr/bin/env python
# coding:utf-8

import pdb
import time
import socket
from threading import Thread
# from multiprocessing import Process

class Server(object):

	def __init__(self, serverIp = "127.0.0.1", serverPort = 7778):
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind((serverIp,serverPort))
		server.listen(5)
		self.server = server
		self.flag = True
		self.processQ = {}
		self.receveString()

	def receveString(self):
		print "Start server"
		while self.flag:
			sock, addr = self.server.accept()
			if sock:
				pid = Thread(target=self.execComain,args=(sock,addr))
				pid.start()
				print pid.ident
				self.processQ[pid.ident] = None
			print self.processQ.keys()
	def cancelServer(self,receve):
		if receve == 'exit':
			self.flag = False

	def execComain(self,sock,addr):
		print "Sub process accecpt data"
		sock.send('Welcome')
		while True:
			shell = raw_input(">>").strip()
			if shell:
				sock.send(shell)
				data = sock.recv(1024)
				print "{addr}---{data}".format(addr=addr,data=data)
			elif shell == 'exit':
				break
			# pdb.set_trace()
			else:
				time.sleep(1)
		sock.close()


if __name__  == "__main__":
	Server()
