#!usr/bin/env python
# coding:utf-8

"""
	探测微博服务质量
"""

import os,sys
import time
import sys
import pycurl



class PYCurl(object):

	def __init__(self,url=''):
		if url:
			self.url = url
		else:
			self.url = "https://www.baidu.com"
		self.indexFile  = self.creatFile()
		self.c = pycurl.Curl()
		self.c.setopt(pycurl.URL, self.url)
		self.request()
		self.getResault()

	def setOpt(self):
		self.c.setopt(pycurl.CONNECTTIMEOUT,5)
		self.c.setopt(pycurl.TIMEOUT,5)
		self.c.setopt(pycurl.NOPROGRESS,1)  #屏蔽进度条
		self.c.setopt(pycurl.FORBID_REUSE,1) #完成交互后断开
		self.c.setopt(pycurl.MAXREDIRS,1) #指定http最大重定向数量
		self.c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)
		self.c.setopt(pycurl.WRITEHEADER,self.indexFile)
		self.setOpt(pycurl.WRITEDATA,self.indexFile)

	def creatFile(self):
		indexFile = open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"cintent.txt"),'wb')
		return indexFile

	def request(self):
		try:
			self.c.perform()
		except Exception as e:
			print "connect error:" + str(e)
			self.indexFile.close()
			self.c.close()
			sys.exit()

	def getResault(self):
		nameLookUpTime = self.c.getinfo(pycurl.NAMELOOKUP_TIME) #获取dns解析时间
		connectTime = self.c.getinfo(pycurl.CONNECT_TIME)  #获取建立链接时间
		pretransferTime = self.c.getinfo(pycurl.PRETRANSFER_TIME) #获取从建立链接到准备传输所消耗掉时间
		startTransferTime = self.c.getinfo(pycurl.STARTTRANSFER_TIME) #获取从建立链接到传输开始消耗的时间
		totalTime = self.c.getinfo(pycurl.TOTAL_TIME)
		httpCode = self.c.getinfo(pycurl.HTTP_CODE)
		sizeDownload = self.c.getinfo(pycurl.SIZE_DOWNLOAD)
		headerSize = self.c.getinfo(pycurl.HEADER_SIZE)
		speedDownload = self.c.getinfo(pycurl.SPEED_DOWNLOAD) #平均下载时间

		print "HTTP 状态码: %s" %httpCode
		print "DNS 解析时间: %.2f ms"%(nameLookUpTime * 1000)
		print "建立链接时间: %.2f ms"%(connectTime * 1000)
		print "准备传输时间: %.2f ms"%(pretransferTime * 1000)
		print "传输开始时间: %.2f ms"%(startTransferTime * 1000)
		print "传输结束总时间: %.2f ms"%(totalTime * 1000)
		print "下载数据包大小: %d bytes/s"%sizeDownload
		print "HTTP 头部大小: %d byte"%headerSize
		print "平均下载速度: %s bytes/s"%speedDownload
		self.indexFile.close()
		self.c.close()

if __name__ == "__main__":
	url = raw_input("要测试的url:")
	PYCurl(url)


