#!usr/bin/env python
# coding:utf-8

#阶乘
#  1 * 2 *3 *4 *5
n = 5

def fun(n):
	if n == 1:
		return n
	print n
	a = n * fun(n-1)
	print a
	return a

fun(n)

resault = 1
for i in range(2,n+1):
	resault = resault*i
	print resault