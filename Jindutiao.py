#!usr/bin/env python
# coding:utf-8

import sys, time


"""
实现原理,sys标准输出到控制器,隔段时间刷新数据
"""

def Jindu(totlenum,sleepTime=0.1):
    if isinstance(totlenum,[int,float]):
        for i in range(totlenum):
            k = i + 1
            str = '>' * (i // 2) + ' ' * ((totlenum - k) // 2)
            sys.stdout.write('\r' + str + '[%s%%]' % (i + 1))
            sys.stdout.flush()
            time.sleep(sleepTime)