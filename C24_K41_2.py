# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 16:33:55 2021

@author: KhatuntsevSV



"""

global dv_1
dv_1 = 1

import os
import all_files

all_files.adddir("C:/Users/Khatuntsevsv/Desktop/W/exp")


writtenfile = os.getcwd()+'\\wrt.txt'

def openfile(fn):
#	with open(fn, 'r', encoding='utf-8')  as g:
#	with open(all_files.c25_k41_2,'r', encoding='ansi')  as g:
	with open(all_files.c25_k41_2,'r', encoding='ansi')  as g:
		readdata = g.read()
		print(len(readdata), type(readdata))
#		print(os.getcwd())
#		print(readdata)
		
		
#		for i in range(0, 256):
#			print(i, readdata.count(chr(i)))
		str1 = ''
		
		for i in range(0, len(readdata)):
#		for i in range(0, 10):
			if ord(readdata[i])!=0\
			and ord(readdata[i])!=1\
			and ord(readdata[i])!=2\
			and ord(readdata[i])!=6\
			and ord(readdata[i])!=7\
			 and ord(readdata[i])!=17\
			and ord(readdata[i])!=22\
			and ord(readdata[i])!=12\
			and ord(readdata[i])!=30\
			and ord(readdata[i])!=127\
			and ord(readdata[i])!=19\
			and ord(readdata[i])!=3\
			and ord(readdata[i])!=31\
			and ord(readdata[i])!=18\
			and ord(readdata[i])!=20\
			and ord(readdata[i])!=14\
			and ord(readdata[i])!=16\
			and ord(readdata[i])!=27\
			and ord(readdata[i])<144 :
#				print(f'readdata:{readdata[i]},{ord(readdata[i])}')
				str1+=readdata[i]
#				print(i, readdata[i])
		
		print(f'\tlen(str1):\t{len(str1)}')
		
		with open(writtenfile, 'w',encoding="utf-8") as wf:
#			print(str1, file=wf)
			wf.write(str1)
			wf.close()
		
	
#openfile(all_files.c25_k41_2)

def count(l,k):
	if type(l)==list and type(k)!=list:
		print(f'count:\t{l.count(k)}')
#count([1,2,3,'a'], 10)


import numpy
X = []
Y=[]
R = 0
for i in range(0, 5):
	X+=[i]
for i1 in range(0,10):
	for i2 in range(0,10):
		for i3 in range(0,10):
			for i4 in range(0,10):
				for i5 in range(0,10):
					Y=[i1,i2,i3,i4,i5]
					cov = numpy.corrcoef(X,Y)[1][0]
					if abs(cov)>=0.5:
						R+=1
						print(R, Y, cov, sep = '\t')
print(X)
