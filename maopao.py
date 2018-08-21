#!usr/bin/env python
# coding:utf-8

import random

l = [1,5,7,8,2,4,6,0,9,3]

def digui(source,save=[]):
	chang = len(source)
	print save
	if not source:
		return save
	for i in range(chang):
		if i == 0:
			a = i
		if i < chang:
			if a <= source[i]:
				a = source[i]
			else:
				a
	source.remove(a)
	save.insert(0,a)
	return digui(source,save)

# a = digui(l)
# print a

#选择排序
def xuanze(l):
	save = []
	save.append(l.pop())
	print save[len(save)-1]
	while len(l)> 0:
		a = l.pop()
		for n,i in enumerate(save):
			if a < i:
				if n == 0:
					save.insert(0,a)
				else:
					save.insert(n-1,a)
			elif a >= save[len(save)-1]:
				save.append(a)

	return save
print xuanze(l)

