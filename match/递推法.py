#!usr/bin/env python
# coding:utf-8

#斐波那契算法 1 1 2 3 5 8 13

lt = []
for i in range(20):
	if i == 0 or i == 1:
		lt.append(i)
	else:
		lt.append(lt[i-2] + lt[i-1])

print lt