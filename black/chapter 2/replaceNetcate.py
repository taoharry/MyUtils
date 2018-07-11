#!usr/bin/env python
# coding:utf-8

import sys
import socket
import getopt
import threading
import subprocess


listen = False
command = False
upload = False
execute = ''
target = ''
upload_destination = ""
port = 0

def usege():
	print "BHP Net Tool\n"
	print "Usage: reolaceNetcate.py  -t target_host -p port"
	print "-l --listen				 - listen on [host]:[port] for " \
		  "incoming connections"
	print "-e --execute=file_to_run  - excute the given file upon" \
		  "receiving a connection"
	print "-c -- command 			 - initialize a command shell"
	print "-u --upload=destination	 - upon receving connection upload a" \
		  "file and write to [destination]"
	print
	print
	print "Examples:"
	print "reolaceNetcate.py -t 192.168.0.1 -p 555 -l -c"
	print "reolaceNetcate.py -t 192.168.0.1 -p 555 -l -u=c:\\target.exe"
	print "reolaceNetcate.py -t 192.168.0.1 -p 555 -l -e='cat /etc/passwd'"
	print "echo 'ABCDEFGHI'| ./reolaceNetcate.py -t 192.168.0.1 -p 555"
	sys.exit(0)

def main():
	global listen
	global port
	global execute
	global command
	global upload_destination
	global target
	if not target or port == 0:
		usege()
	if listen:
		server_loop()
	if not listen and len(target) and port >0:
		buffer = sys.stdin.read()
		client_sender(buffer)

def client_sender(buffer):
	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		client.connect((target,port))
		if len(buffer):
			client.send(buffer)
		while True:
			recv_len = 1
			response = ''
			while recv_len:
				data = client.recv(4096)
				recv_len = len(data)
				response +=data
				if recv_len < 4096:
					break
			print response
			buffer = raw_input("")
			buffer +="\n"
			client.send(buffer)
	except:
		print  "[*] Exception! exiting."

	client.close()

def server_loop():
	global target
	if not len(target):
		target = "0.0.0.0"
		server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		server.bind((target,port))
		server.listen(5)
		while True:
			client_socket,addr = server.accept()
			client_thread = threading.Thread(target=client_handler,args=(client_socket,))
			client_thread.start()

def run_command(command):
	command = command.rstrip()
	try:
		output = subprocess.check_output(command,stderr=subprocess.STDOUT,shell=True)
	except:
		output = "Failed to execute command,\n"
	return output

def client_handler(client_socket):
	global upload
	global execute
	global command
	if len(upload_destination):
		file_buffer = ""
		while True:
			data = client_socket.recv(1024)
			if not data:
				break
			else:
				file_buffer +=data

	try:
		file_description = open(upload_destination,"wb")
		file_description.write(file_buffer)
		file_description.close()
		client_socket.send("successfully saved file to %s \n"%upload_destination)
	except:
		client_socket.send("Failed to saved file to %s \n"%upload_destination)

	if len(execute):
		output = run_command(execute)
		client_socket.send(output)

	if command:

		while True:
			client_socket.send('<BHP:#> ')
			cmd_buffer = ""
			while "\n" not in cmd_buffer:
				cmd_buffer +=client_socket.recv(1024)
			response = run_command(cmd_buffer)
			client_socket.send(response)