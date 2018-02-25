#!usr/bin/env python
# coding:utf-8

import time
import threading
from threading import Thread



class ThreadUtils(Thread):

    def __init__(self):
        super(ThreadUtils,self).__init__()
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True


    def run(self):
        while self.__running.isSet():
            self.__flag.wait()  # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            print time.time()
            time.sleep(1)


    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞


    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞


    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False


if __name__ == "__main__":
    a = ThreadUtils()
    a.start()
    time.sleep(3)
    a.pause()
    time.sleep(3)
    a.resume()
    time.sleep(3)
    a.pause()
    time.sleep(2)
    a.stop()