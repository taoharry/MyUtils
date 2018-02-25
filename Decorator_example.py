#!usr/bin/env python
# coding:utf-8


from functools import wraps



#不带参数覆盖原函数属性装饰器
def Warpfun(fun):
    def fun_w(*args,**kwargs):
        """func doce"""
        #函数处理前逻辑
        print "不带参数覆盖原函数属性装饰器"
        return fun()
        #函数处理后逻辑
    return fun_w

#不带参数"不"覆盖原函数属性装饰器
def WarpfunN(fun):
    """func doce"""
    @wraps(fun)
    def fun_w(*args,**kwargs):
        #函数处理前逻辑
        return fun()
        #函数处理后逻辑
    return fun_w

#带参数覆盖原函数属性装饰器
def Warp_fun(fun,a,b=1):
    #必须传进参数a
    """func doce"""
    def fun_w(*args,**kwargs):
        #函数处理前逻辑
        return fun()
        #函数处理后逻辑
    return fun_w

@Warpfun
def test():
    """
    test
    """
    pass

if __name__ == "__main__":
    a = test()

    print a