#!usr/bin/env python
# coding:utf-8

import Queue
import threading
import os
import urllib2

threads = 10
target = "http://www.blackhatpython.com"
directory = "/opt/app"
filters = [".jpg",".git","png",".css"]

os.chdir(directory)

web_paths = Queue.Queue()

for r,d,f in os.walk('.'):
	for files in f:
		remote_path = "{}/{}".format(r,files)
		if remote_path.startswith('.'):
			remote_path = remote_path[1:]
		if os.path.splitext(files)[1] not in filters:
			web_paths.put(remote_path)

def test_remote():
	while not web_paths.empty():
		path = web_paths.get()
		url = "{}{}".format(target,path)
		try:
			response = urllib2.urlopen(url)
			content = response.read()
		except urllib2.HTTPError as e:
			print e

for i in range(threads):
	t = threading.Thread(target=test_remote)
	t.start()

