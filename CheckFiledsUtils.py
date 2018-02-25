#!usr/bin/env python
# coding:utf-8


import inspect


class CheckFileds(object):


    def __init__(self):
        pass



    def __setattr__(self, key, value):
        try:
            arg = inspect.getargspec(self.__init__) #获得函数__init__的属性
            args = arg.args  #获得传进来参数,
            defaults = arg.defaults #参数设置默认值
            if 'self' in args:
                args.remove('self')
            kwargs = dict(zip(args, defaults))
            if key in kwargs:
                defType = type(kwargs[key])
                if isinstance(kwargs[key], (str, unicode)):
                    defType = (str, unicode)
                elif isinstance(kwargs[key], (int, long)):
                    defType = (int, long)
                elif isinstance(kwargs[key], (list, tuple)):
                    defType = (list, tuple)
                if not isinstance(value, defType):
                    raise TypeError, "Need %s input %s" % (defType, type(key))
        except:
            #可以写入到日志文件
            raise TypeError, "Need %s input %s" % (defType, type(key))
        super(CheckFileds,self).__setattr__(key,value)



class ClassExplain(object):

    def __new__(cls, *args, **kwargs):
        #new 是在类生成之间自动调用的
        # return checkFileds() 这么使用是不走自己的构造方法的
        pass

    def __init__(self):
        #负责将类实例化
        pass

    def __call__(self, *args, **kwargs):
        # self.__call__() == classExplain() 主要作用是可以像函数一样调用类
        pass

    def __del__(self):
        #折构函数,负责类使用完了处理一些事务
        pass

    def __enter__(self):
        #上下文管理器相当于with as
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        #退出
        pass

    def __set__(self, instance, value):
        #调用实例本身拥有属性使用,是实例创建后被动使用,instance 是拥有者对象的一个实例.创建对象的描述器
        print instance,value

    def __setattr__(self, key, value):
        #创建实例时候自动调用,控制属性访问
        print key,value

    def __getattr__(self, item):
        #对象访问一个不存属性时候使用,控制属性访问
        pass

    def __get__(self, instance, owner):
        #定义当描述器的值被取得的时候的行为(证明对象中有这个类)， instance 是拥有者对象的一个实例。 owner 是拥有者类本身
        pass

