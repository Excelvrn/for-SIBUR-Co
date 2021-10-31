# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 10:01:53 2021

@author: KhatuntsevSV
"""

import pandas, datetime


SAP_REPORT="C:\\Users\\Khatuntsevsv\\Desktop\\W\\SAP.Report.xlsx"
SJAP="C:/Users/Khatuntsevsv/Desktop/W/Datas/BuLi/SJAP.01_02.2021.xlsx"

types_col_0 = ["ПЛАНP", "ППР", "ПРОГНОЗ", "ФАКТ" ]
types_rows=["СКД", "ДССК", "СКС", "ДСТ", "СБС"]


def run5(filename, sh):
	g=pandas.read_excel(filename, sh)
	print(g.columns)
	
	l=[]
	
	row0=g.columns
	for i in types_rows:
		#print("Series:\t", row0.str.count(i))
		Ser = row0.str.count(i)
		print("Ser")
		ll=[]
		for i2 in range(0, len(Ser)):
			if Ser[i2]==1:
				print(i2)
				ll+=[i2]
		l+=[ll]
	print(l)
			
	
	col_names = g.iloc[:, 0]
	print(type(col_names))
	for i in types_col_0:
		k=0
		for i2 in col_names.str.count(i):
			if i2==1:
				k+=1
		print(k)
	print(col_names[0])
		

#	print(statistics.mean(Output_list))