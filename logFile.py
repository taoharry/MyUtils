#!usr/bin/env python
# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import logging

confPath = './'

class LogUtils(object):

    def __init__(self):
        conf = os.path.join(confPath,'logger.conf')
        logging.config.fileConfig(conf)
        self.logger = logging.getLogger("root")

    def debug(self,arg):
        self.logger.debug(arg)

    def info(self,arg):
        self.logger.info(arg)

    def warn(self,arg):
        self.logger.warn(arg)

    def error(self,arg):
        self.logger.error(arg)


