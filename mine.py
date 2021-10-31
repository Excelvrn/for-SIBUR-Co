# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 11:32:46 2021

@author: KhatuntsevSV
"""

def fib(a,b, times):
	sum = 0
	s1 = 0
	s2 = 0
	l = []
	for i in range(0, times):
		if i == 0:
			sum = a + b
			s1 = a
			s2 = b
			l+=[s1, s2, sum]
		else:
			s2 = l[i]
			sum = sum + s2
			l+=[sum]
	for i in range(1, len(l)):
		print(i, l[i], l[i]/l[i-1], sep="\t\t")

fib(1,33, 100)
			
			