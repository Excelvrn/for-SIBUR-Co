global vmain, debug
vmain = 10
debug = 2
'''


5 - из обработанного файла paek_5 получить показатель работы батарей
6 - получить работу 41кл
7 - получить работу батарей, 41кл, 112кл
8 - получить набор данных по-колонно, удалив строки неработающих 41-ых колонн, и корреляцию
9 - получить данные в случае работы бат/112/41
10 - main10()


'''

import os, time
import  sys, pandas, numpy, matplotlib, math, statistics
#import seaborn as sbrn
#import matplotlib.pyplot as mpl
from decimal import *

import all_files
all_files.adddir("C:/Users/Khatuntsevsv/Desktop/W/exp")

#all_files.adddir("C:\\Users\\Khatuntsevsv\\Desktop\\W\\pythlibs\\networkx-main")
import networkx as nx

import report_1

import data_module as dm


import datetime
import pandas
import decimal
#import statsmodels
import numpy

#print(numpy.nan, type(numpy.nan))

def df_getstr(datafr, col):
#	g = datafr.iloc[:, [1]].to_list()
#	g = datafr.iloc[:, [1]]
	datarow, datacol = datafr.shape
#	print(datafr.shape)
#	for i in range(0, datafr.shape[0]):
#		print(i, datafr.iat[i, col])
#	gl = g.iloc[0].to_list()
#	
#	print(f'type(g):{type(g)}\t{g.shape}')
#	ind = -1
	typel = []
	for i in range(0, datarow):
		if type(datafr.iat[i,col])==str:
#			print(i, datafr.iat[i,col])
			typel+=[i]
#			if typel.count(type(i))==0:
#				typel+=[type(i)]
#			print(ind, type(i), i)
#	print(len(typel), typel, sep="\t\n")
	return typel

def df_drop(datafr):
	dfr, dfc = datafr.shape
	l=[]
	dropl=[]
	for i in range(0, dfc):
		g = df_getstr(datafr, i)
		
		if len(g)<dfr:
			l+= g
		print(i+1, '/', dfc, len(g), len(l))
		if len(g)==dfr:
			print("\t\t!!!", i, len(g), datafr.columns[i], len(dropl))
			dropl+=[datafr.columns[i]]
	sl = set(l)
	print("sl:\t", len(sl))
	
	drdf = datafr.drop(dropl,axis=1 )
#	if len(dropl)>0:
#		print(drdf.drop(dropl,axis=1 ).shape)
		
	drdf = drdf.drop(sl)
	if len(sl)>0:
		print("sl:\t",drdf.shape)
	return drdf


def df_drop_v2(datafr):
	dfr, dfc = datafr.shape
#	l=[]
	dropl=[]
	for i in range(0, dfc):
		g = df_getstr(datafr, i)
		
		if len(g)<dfr:
#			l+= g
			print(i+1, '/', dfc, len(g))
		elif len(g)==dfr:
			print("\t\t!!!", i, len(g), datafr.columns[i], len(dropl))
			dropl+=[datafr.columns[i]]
#	sl = set(l)
#	print("sl:\t", len(sl))
	
	try:
		drdf = datafr.drop(dropl,axis=1 )
	except:
		print("***\tdrdf except")
	else:
		print("***\tdf_drop_v2:\t",drdf.shape)
#	if len(dropl)>0:
#		print(drdf.drop(dropl,axis=1 ).shape)
		
#	drdf = drdf.drop(sl)
#	if len(sl)>0:
#		print("sl:\t",drdf.shape)
	return drdf
def df_drop_v3(datafr, delrowlist):
	'''
	execute after df_drop_v3
	'''
	k = 0
#	drdf = datafr
	with pandas.ExcelWriter(all_files.paek_1) as writer:
		for i in delrowlist:
			try:
				drdf = datafr.drop(i)
			except:
				print("***\tdf_drop_v3 except")
			else:
				print("***\tdrdf:\t",drdf.shape)
				namesheet = 'Sheet' + str(k)
				drdf.to_excel(writer, sheet_name=namesheet)
			k+=1
		
		
	
#	if len(dropl)>0:
#		print(drdf.drop(dropl,axis=1 ).shape)
		
#	drdf = drdf.drop(sl)
#	if len(sl)>0:
#		print("sl:\t",drdf.shape)
	return drdf
	
def get_worked(datafr, worked):
	pass
	
#	print(dfr, len(sl))
	

def main():
	print("run")
	#!!! elect recordsdatas_file
	# рабочий main_deb_1 = 4
	main_deb_1 = 4
	TEP_L_R = 1
	#3 лист - рабочий
	if main_deb_1==1:
		recordsdatas = pandas.read_excel(all_files.record_1, 3)
	elif main_deb_1==2:
		recordsdatas = pandas.read_excel(all_files.np_datas, 1)
	elif main_deb_1==3:
		recordsdatas = pandas.read_excel(all_files.exp_5)
	elif main_deb_1==4:
		recordsdatas = pandas.read_excel(all_files.exp_6)
		
	print("\tOpen recordsdatas 1")
	
# ***		
	if TEP_L_R == 1:
		naspldatas = dm.getnaspl_1_0(all_files.np_tep_l,1, 0, 15)
	elif TEP_L_R==2:
		naspldatas = dm.getnaspl_1_0(all_files.np_tep_r,1, 0, 15)
	print("naspl.shape:\t", naspldatas.shape)
	print("\tOpen recordsdatas 2")
	naspldatas.to_excel(all_files.exp_1)
	print("\tBe read naspldatas")
	dm.getnasplins3(naspldatas, recordsdatas, all_files.exp_2, all_files.exp_3)

def main_2(namecol='RAB', defsheet='Y2'):
	print("run")

#	pdatas = pandas.read_excel(all_files.paek_2, 3)
	pdatas = pandas.read_excel(all_files.paek_3, defsheet)
	
	pdatasr, pdatasc = pdatas.shape
	
	print(f'\t***\tpdatas:\t{pdatas.shape}')
	RAB_l = []

	for i in pdatas.columns:
		if i.count("Bat") and i.count(namecol):
			print(f'columns:\t{i}')
			RAB_l+=[i]
#			print(f'aset:\t{aset}\t{len(aset)}')

	print('***\tset:\t', RAB_l)
	


	
	st_l_main = []
	for i in RAB_l:
		st_l=[]
		print(i, pdatas[i].size,pdatas[i].ndim, sep='\t')
		for i2 in range(0, pdatas[i].size):
			if type(pdatas[i].iat[i2])!=str and pdatas[i].iat[i2]==1:
				st_l+=[i2]
		st_l_main+=[st_l]
	for i in st_l_main:
		print("st_l_main:\t", len(i))
		
	k= set([])
	for i in st_l_main:
		k= k.union(set(i))
	
	print("***\tK:", len(k))
	
	g = range(0, pdatasr)
	g = set(g)
	g = g.difference(k)
	print(len(g))
	
	print(pdatas.shape)
	
	dropg = list(g)
	pdatas_drop= pdatas.drop(dropg)
	
	print(pdatas_drop.shape)
	
#	pdatas_drop.to_excel(all_files.paek_4)
	corr_matrix = pdatas_drop.corr()
	with pandas.ExcelWriter(all_files.paek_4) as writer:
		corr_matrix.to_excel(writer, sheet_name="Cor")
		pdatas_drop.to_excel(writer, sheet_name="Sh11")
	
#	print('pandas.read_excel(all_files.paek_0, 3)', pdatas.iat[0,1], type(pdatas.iat[0,1]), pdatas.iloc[1])
	
#	g = df_drop_v3(df_drop_v2(pdatas), st_l_main)
#	print("after drop:\t", type(g), g.shape)
	
	
#	corr_matrix = g.corr()
#	print("\tCR:\n", type(corr_matrix), len(corr_matrix))
	
#	try:                                                                              
#		k = pandas.DataFrame(corr_matrix, index=g.columns, columns=g.columns)
#		k.dropna(axis=1, how='all')
#		k.dropna(axis=0, how='all')
#	except:
#		print("Except")
#	else:
##		k.dropna()
	
#	with pandas.ExcelWriter(all_files.paek_1) as writer:
#		corr_matrix.to_excel(writer, sheet_name="Cor")
#		g.to_excel(writer, sheet_name="Sh11")
	
#		print(pdatas.columns, pdatas.iloc[0],corr_matrix, sep="\n")
def main_3(defsheet='Y2'):
	print("run")

#	pdatas = pandas.read_excel(all_files.paek_2, 3)
	pdatas = pandas.read_excel(all_files.paek_4, defsheet)
	
	pdatasr, pdatasc = pdatas.shape
	
	print(f'\t***\tpdatas:\t{pdatas.shape}')
	
	RAB_l = []
	dropl = []
	
	for el in pdatas.columns:
		k = 0
		els = 0
		ll=[]
		for i in range(0, pdatasr):
			if type(pdatas[el].iat[i])==str:
				els+=1
				ll+=[i]
#		print(el, els*100/pdatasr, sep='\t')
		if (els == pdatasr):
			RAB_l+=[el]
		else:
			dropl+=ll
			print('***',el, els*100/pdatasr, sep='\t')
	print('string columns:',RAB_l)
	print(len(set(dropl)))
	drdf = pdatas.drop(RAB_l,axis=1 )
	print('drdf shape:\t', drdf.shape)
	drdf.to_excel(all_files.paek_5, sheet_name='Cut')
	
def main_4(defsheet='Y2'):
	print("run")

#	pdatas = pandas.read_excel(all_files.paek_2, 3)
	pdatas = pandas.read_excel(all_files.paek_5, defsheet)
	
	pdatasr, pdatasc = pdatas.shape
	
	print(f'\t***\tpdatas:\t{pdatas.shape}')
	
	lcol = []
	for i in pdatas.columns:
		if i.count('Bat') and i.count('RWork') and (i.count('001') or i.count('002') or\
			 i.count('004') or i.count('008')):
			lcol+=[i]
	print('RABs:\t', lcol)
	
	bat_rab=[]
	
	for i in lcol:
		rab=[]
		for i2 in range(0, pdatasr):
			if type(pdatas[i].iat[i2])!=int and type(pdatas[i].iat[i2])!=float:
				rab+=[i2]
				print(i, i2, type(pdatas[i].iat[i2]))
#			else:
#				print(i, i2, type(pdatas[i].iat[i2]))
		bat_rab+=[rab]
	for i in bat_rab:
		print('bat_rab:\t', len(i))
		
	pdatasr_set = []
	for i in range(0, pdatasr):
		pdatasr_set+=[i]
	
#	print(type(x), len(x))
#	
#	res = pdatas.drop(x)
#	print('res.shape:\t', res.shape)
#	print('pdatas.shape:\t', pdatas.shape)
	
#	for i in bat_rab:
#		xset = set(i)
#		xset = xset.difference(pdatasr_set)
#		g = pdatas.drop(xset)
#		corr = g.corr()
#		with pandas.ExcelWriter(all_files.paek_6) as writer:
#			g.to_excel(writer, sheet_name=i)
#			corr.to_excel(writer, sheet_name=i+'_cor')

#for i in range(0, len(bat_rab)):
#	xset = set(bat_rab[0])
#	xset = xset.difference(pdatasr_set)
#	print('len(xset):\t', len(xset))
#	xset = list(xset)
	g = pdatas.drop(bat_rab[0])
	corr = g.corr()
	with pandas.ExcelWriter(all_files.paek_6) as writer:
		g.to_excel(writer, sheet_name='main')
		corr.to_excel(writer, sheet_name='_cor')
#	
#	
#	RAB_l = []
#	dropl = []
#	
#	for el in pdatas.columns:
#		k = 0
#		els = 0
#		ll=[]
#		for i in range(0, pdatasr):
#			if type(pdatas[el].iat[i])==str:
#				els+=1
#				ll+=[i]
##		print(el, els*100/pdatasr, sep='\t')
#		if (els == pdatasr):
#			RAB_l+=[el]
#		else:
#			dropl+=ll
#			print('***',el, els*100/pdatasr, sep='\t')
#	print('string columns:',RAB_l)
#	print(len(set(dropl)))
#	drdf = pdatas.drop(RAB_l,axis=1 )
#	print('drdf shape:\t', drdf.shape)
#	drdf.to_excel(all_files.paek_5)
def main_5(defsheet='main', column_name='41'):
	print("run")

#	pdatas = pandas.read_excel(all_files.paek_2, 3)
	pdatas = pandas.read_excel(all_files.paek_6, defsheet)
	
	pdatasr, pdatasc = pdatas.shape
	
	print(f'\t***\tpdatas:\t{pdatas.shape}')
	
	lcol = []
	for i in pdatas.columns:
		if i.count(column_name) or i.count('OS') or i.count('SO'):
			lcol+=[i]
	print('RABs:\t', lcol)
	
	
	
#	print(type(x), len(x))
#	
#	res = pdatas.drop(x)
#	print('res.shape:\t', res.shape)
#	print('pdatas.shape:\t', pdatas.shape)
	
#	for i in bat_rab:
#		xset = set(i)
#		xset = xset.difference(pdatasr_set)
#		g = pdatas.drop(xset)
#		corr = g.corr()
#		with pandas.ExcelWriter(all_files.paek_6) as writer:
#			g.to_excel(writer, sheet_name=i)
#			corr.to_excel(writer, sheet_name=i+'_cor')

#for i in range(0, len(bat_rab)):
#	xset = set(bat_rab[0])
#	xset = xset.difference(pdatasr_set)
#	print('len(xset):\t', len(xset))
#	xset = list(xset)
	cut = 2
	if cut==1:
		g = pdatas.drop(bat_rab[0])
		corr = g.corr()
		with pandas.ExcelWriter(all_files.paek_6) as writer:
			g.to_excel(writer, sheet_name='main')
			corr.to_excel(writer, sheet_name='_cor')
def main_6(defsheet='Y2'):
	print("run")

#	pdatas = pandas.read_excel(all_files.paek_2, 3)
	pdatas = pandas.read_excel(all_files.paek_3, defsheet)
	
	pdatasr, pdatasc = pdatas.shape
	
	print(f'\t***\tpdatas:\t{pdatas.shape}')
	
	lcol = []
	for i in pdatas.columns:
		if i.count('RAB') or i.count('RWork'):
			lcol+=[i]
	print('RABs:\t', lcol)	
	
	index_proces = 0
	ldata=[]
	ldata3=[]
	for i in range(0, pdatasr):
		retx = 0
		for el in lcol:
			if type(pdatas[el].iat[i])!=str:
				if pdatas[el].iat[i]==1 or pdatas[el].iat[i]==1.0:
					retx+=1
					ldata+=[i]
		if retx>2:
			index_proces+=1
#			print(index_proces, i)
			ldata3+=[i]
	print("ldata:\t", len(set(ldata)))
	print("ldata3:\t", len(set(ldata3)))
	
#			for el in lcol:
#				print('***\t', pdatas[el].iat[i])
#	
	cut = 2
	if cut==1:
		g = pdatas.drop(bat_rab[0])
		corr = g.corr()
		with pandas.ExcelWriter(all_files.paek_6) as writer:
			g.to_excel(writer, sheet_name='main')
			corr.to_excel(writer, sheet_name='_cor')


	retBat = dm.getnamedcol_1(pdatas, ['RWork'])
	print('Bat:\t', len(retBat))

	ret112 = dm.getnamedcol_1(pdatas, ['112', 'RAB'])
	print('***\t112:\t', len(ret112))
	
	ret41=dm.getnamedcol_1(pdatas, ['41', 'RAB'])
	print('41:\t', len(set(ret41)))
	
	
	
	kkk = set(retBat)
	kkk = kkk.intersection(set(ret112), set(ret41))
	print(len(kkk))
	kkk = kkk.intersection(set(ret41))
	print(len(kkk))
	
	gg = set(range(0, pdatasr))
	print(f'gg:\t{len(gg)}')
	gg2 = gg.difference(kkk)
	print(f'gg:\t{len(gg2)}')
	
	drdatas = pdatas.drop(gg2)
	
	'''
	delete Battery 003, 005
	'''
	main_tag_name = 'Battery'
	adv_tag_name_1 = '003'
	adv_tag_name_2 = '005'
	dropcol_main_tag_name=[]
	
	for el in pdatas.columns:
		if el.count(main_tag_name) and ( el.count(adv_tag_name_1) or el.count(adv_tag_name_2) ):
			dropcol_main_tag_name+=[el]
	for i in dropcol_main_tag_name:
		print('*** dropcol_main_tag_name:\t', i)
		
		
	print(drdatas.shape, drdatas.columns)
	drdatas.drop(dropcol_main_tag_name, axis=1, inplace=True)
	print(drdatas.shape, drdatas.columns)
#	drdatas1 = dm.dropnull(drdatas)
	corr = drdatas.corr()
	print('drdatas after droping:\t', drdatas.shape)
	
	print()
	
	
#	print('type:\t', type(drdatas.columns.to_list()))
#	sdrdatas = drdatas.columns.to_list()
#	print('***\tSorted:\n',sorted(drdatas.columns.to_list()))
#	
	with pandas.ExcelWriter(all_files.paek_7) as writer:
		dm.dropnullcol(drdatas).to_excel(writer, sheet_name='delcol')
		corr.to_excel(writer, sheet_name='cor')
#	sorted('***\tSorted:\n', drdatas.columns)
def main_7(filedoc=all_files.paek_8, defsheet='delcol'):
	'''
	cut columns 41 (4)
	'''
	print("run")

#	pdatas = pandas.read_excel(all_files.paek_2, 3)
	pdatas = pandas.read_excel(filedoc, defsheet)
	
	pdatasr, pdatasc = pdatas.shape
	
	print(f'\t***\tpdatas:\t{pdatas.shape}')
	
	cutlist=[]
	for el in pdatas.columns:
		if el.count('41') and el.count('RAB'):
			cutlist+=[el]
			
	rab_main=[]
	for el in cutlist:
		print('cut - \t', el)
		rab0=[]
		for i in range(0, pdatasr):
			if type(pdatas[el].iat[i])==str or pdatas[el].iat[i]==0:
				rab0+=[i]
		rab_main+=[rab0]
		
	for i in rab_main:
		print(len(i))
		
	with pandas.ExcelWriter(all_files.paek_8) as writer:
		for i in range(0, len(rab_main)):
			sn='doc' + str(i)
			g = pdatas.drop(rab_main[i])
			g.to_excel(writer, sheet_name=sn)
			sn='cor' + str(i)
			g = g.corr()
			g.to_excel(writer, sheet_name=sn)
	
	cutlist=[]
	for el in pdatas.columns:
		if el.count('41') and el.count('RAB'):
			cutlist+=[el]
	
	
	
		
		
#	print(drdatas.shape, drdatas.columns)
#	drdatas.drop(dropcol_main_tag_name, axis=1, inplace=True)
#	print(drdatas.shape, drdatas.columns)
##	drdatas1 = dm.dropnull(drdatas)
#	corr = drdatas.corr()
#	print('drdatas after droping:\t', drdatas.shape)
#	
#	print()
#	
#	
##	print('type:\t', type(drdatas.columns.to_list()))
##	sdrdatas = drdatas.columns.to_list()
##	print('***\tSorted:\n',sorted(drdatas.columns.to_list()))
##	
#	with pandas.ExcelWriter(all_files.paek_7) as writer:
#		dm.dropnullcol(drdatas).to_excel(writer, sheet_name='delcol')
#		corr.to_excel(writer, sheet_name='cor')
def main_8(filedoc=all_files.paek_7, defsheet='delcol'):
	'''
	cut columns 41 (4)
	'''
	print("run")

#	pdatas = pandas.read_excel(all_files.paek_2, 3)
	pdatas = pandas.read_excel(filedoc, defsheet)
	
	pdatasr, pdatasc = pdatas.shape
	
	print(f'\t***\tpdatas:\t{pdatas.shape}')
	
	dm.getstatdf(pdatas)
	
	
	cutlist_rwork=[]
	for el in pdatas.columns:
		if el.count('RWork'):
			cutlist_rwork+=[el]

	cutlist_41=[]
	for el in pdatas.columns:
		if el.count('41') and el.count('RAB'):
			cutlist_41+=[el]

	cutlist_112=[]
	for el in pdatas.columns:
		if el.count('112') and el.count('RAB'):
			cutlist_112+=[el]
	
	
	
	all_columns=[cutlist_rwork, cutlist_41, cutlist_112]
	print('ac:\t', len(all_columns))
	
	
	index=0
	
	elements =[]
#	elementsi=[]
# el_1 - bat
# el_2 - 112
# el_3 - 41
#
# [el_1, 
#	el_2,
#		el_3, 
#	         elementsii - rows
# elements=[[el_1, el_2, el_3,elementsii]]
#
	for el_1 in cutlist_rwork:
		for el_2 in cutlist_112:
			for el_3 in cutlist_41:
				el0=[]
				elementsii=[]
				iel0=0
				for i in range(0, pdatasr):
					if type(pdatas[el_1].iat[i])!=str and  type(pdatas[el_2].iat[i])!=str\
					and  type(pdatas[el_3].iat[i])!=str and pdatas[el_1].iat[i]==1 \
					and pdatas[el_2].iat[i]==1 and pdatas[el_3].iat[i]==1\
					and pdatas[el_1].iat[i]!='Null' \
					and pdatas[el_2].iat[i]!='Null' and pdatas[el_3].iat[i]!='Null':
						index+=1
						iel0+=1
						elementsii+=[i]
#						print('***', index, el_1, el_2, el_3, i, sep='\t')
				if iel0:
					el0=[el_1, el_2, el_3,elementsii]
					elements+=[el0]
	
#	for i in elements:
#		if i==elements[0]:
#			print()
#		print('comb:\t',len(elements), i[0].split('.')[0], i[1].split('.')[0], i[2].split('.')[0], len(i[3]), sep='\t')
#		for i2 in pdatas.columns:
#			if i2.count(i[0].split('.')[0]) or i2.count(i[1].split('.')[0]) or i2.count(i[2].split('.')[0]):
#				print('***\t', i2)
	print(len(elements[0][3]), type(elements[0][3]))
			
	rwork1=[]
	for el in cutlist_rwork:
		rworkl = []
		print(el)
		for i in range(0, pdatasr):
			if type(pdatas[el].iat[i])!=str and pdatas[el].iat[i]==1:
				rworkl+=[i]
		rwork1+=[rworkl]
	for i in rwork1:
		print('rwork:\t*\t', len(i))
		
	rwork41=[]
	for el in cutlist_41:
		print(el)
		rworkl = []
		for i in range(0, pdatasr):
			if type(pdatas[el].iat[i])!=str and pdatas[el].iat[i]==1:
				rworkl+=[i]
		rwork41+=[rworkl]
	for i in rwork41:
		print('rwork41:\t*\t', len(i))
		
	rwork112=[]
	for el in cutlist_112:
		print(el)
		rworkl = []
		for i in range(0, pdatasr):
			if type(pdatas[el].iat[i])!=str and pdatas[el].iat[i]==1:
				rworkl+=[i]
		rwork112+=[rworkl]
	for i in rwork112:
		print('rwork112:\t*\t', len(i))
		
#	with pandas.ExcelWriter(all_files.paek_8) as writer:
#		for i in range(0, len(rab_main)):
#			sn='doc' + str(i)
#			g = pdatas.drop(rab_main[i])
#			g.to_excel(writer, sheet_name=sn)
#			sn='cor' + str(i)
#			g = g.corr()
#			g.to_excel(writer, sheet_name=sn)
	
	
	need_columns=[]
	
	if debug==1:
		k = 5
	else:
		k=len(elements)

	for i in range(0, k):
		ncl = [pdatas.columns[0]]
		for el in pdatas.columns:
			if el.count(elements[i][0].split('.')[0]) or el.count(elements[i][1].split('.')[0]) or el.count(elements[i][2].split('.')[0]) or el.count('OS') or el.count('SO_S') or el.count('LAT'):
				ncl+=[el]
		ncl+=[elements[i][3]]
		need_columns+=[ncl]
		print('ncl - ', i, '/k')
#
# [el_1, 
#	el_2,
#		el_3, 
#	         elementsii - rows
# elements=[[el_1, el_2, el_3,elementsii]]
#		print(len(need_columns), len(ncl), ncl)
#		dm.getlen(need_columns)
	
	ind = 0
#	for i in need_columns[0][:len(need_columns[0])-1]:
#		print('need_columns:\t', ind, i)
#		ind+=1
	gs = set(need_columns[1][len(need_columns[1])-1])
#	print('len(gs):\t', len(gs))
	
	k = set(list(range(0, pdatasr)))
	print('k-type:\t', type(k), len(k))
	
	diff = gs.difference(k)
	print('diff:\n', len(diff), pdatasr)
	
	
#	gs = k.difference(gs)
#	print(gs)
#	print('k:\t', kx)
#	print('k-type:\t', type(kx))
	try:
		print(pdatas[need_columns[0][:(len(need_columns[0])-1)]].drop(gs).shape)
	except:
		print('zopa')
	else:
		print('Das Gut!')
	
#	dfr = pdatas[need_columns[1][:(len(need_columns[1])-1)]].drop(gs)
#	dfr = pdatas[need_columns[1][:(len(need_columns[1])-1)]].loc[need_columns[1][len(need_columns[1])-1]]
	with pandas.ExcelWriter(all_files.paek_9) as writer:
		ind = 0
		for el in need_columns:
			dfr = pdatas[el[:(len(el)-1)]].loc[el[len(el)-1]]
			print('step\t', ind)	
			corr_matrix = dfr.corr()
			corr_matrix.to_excel(writer, sheet_name="Cor_"+str(ind))
			dfr.to_excel(writer, sheet_name="Sh_"+str(ind))
			ind+=1
	
#
#	datas, Marks
#
def main_10(filedoc=all_files.paek_10, defsheet='datas', defsheet2='Marks' ):
	'''
	cut columns 41 (4)
	'''
	print("run")

#	pdatas = pandas.read_excel(all_files.paek_2, 3)
	pdatas = pandas.read_excel(filedoc, defsheet)
	pmarks = pandas.read_excel(filedoc, defsheet2)
#	df = pandas.read_excel(all_files.paek_13, 'df')
	
	pdatasr, pdatasc = pdatas.shape
	pmarksr, pmarksc = pmarks.shape
	
	print(f'\t***\tpdatas:\t{pdatas.shape},{pmarks.shape}')

#	dm.getstatdf(pdatas)
	g1 = []
	print('get common .*')
	for i in pdatas.columns:
#		print(i)
		if i.find('.'):
			k = i.split('.')
		if len(k)>1:
			g1+=[k[len(k)-1]]

	setg1 = set(g1)
	setg1l = []
	print('get common ***.')
	for el in setg1:
#		print(el)
		l = []
		for col in pdatas.columns:
			g = col.split('.')
			if len(g)>1 and g[1] == el:
				l+=[col]
		setg1l+=[l]

	print('len:\t',len(setg1l))
	for i in setg1l:
		if len(i):
			print()
#			for i2 in i:
#				if i2!=i[0]:
#					print(i[0], i2)
#					dm.equstr(i2, i[0])
#				print(i2)
#	dm.equstr('asdf', 'as')
###	
###	
###	
	SKN_112 = ['F1', 'F2', 'P1', 'RAB', 'T1', 'T2']
	Col_112 = {'1':'001', '2':'002', '3':'003', '4':'004', '5':'005'}
###
	SKN_41 = [\
#25_SKN_Column_41_*.F1
			'F1',\
#25_SKN_Column_41_*.F2
			'F2',\
#25_SKN_Column_41_*.F3
			'F3', \
#25_SKN_Column_41_*.F3.T_sat
			'F3.T_sat', \
#25_SKN_Column_41_*.L1_1
			'L1_1', \
#25_SKN_Column_41_*.L1_2
			'L1_2', \
#25_SKN_Column_41_*.P1
			'P1', \
#25_SKN_Column_41_*.P2
			'P2', \
#25_SKN_Column_41_*.P3
			'P3', \
#25_SKN_Column_41_*.P4
			'P4', \
#25_SKN_Column_41_*.RAB
			'RAB', \
#25_SKN_Column_41_*.T4
			'T4', \
#25_SKN_Column_41_*.T5
			'T5', \
#25_SKN_Column_41_*.T6
			'T6', \
#25_SKN_Column_41_*.T7
			'T7', \
#25_SKN_Column_41_*.T8
			'T8'\
	]
	apps = {'112':'25_SKN_Column_112_', '41':'25_SKN_Column_41_', 'bat':'25_SKS_Battery_'}
	battery = {'1':'001', '2':'002', '4':'004', '8':'008'}
	
	
	
	var = 2
	if var == 1:
		for col in pmarks.columns:
			if col.find('Bat')>0 and col.find('Col')>0:
	#			print(col)
				ncol = 0
				for ind in pmarks[col]:
					k = ind.split('/')
					if len(k)>1:
						print(f'{col}:\t{k[1]}')
# var 2
	elif var == 2:
		varframe = 0
		for col in pmarks.columns:
			if col.find('Bat')>0 and col.find('Col')>0:
	#			print(col)
				ncol = 0
				time = 0
				dictdatetime = {'1':[], '2':[], '3':[], '4':[], '5':[]}
				battery_number = col[len('AL_25_Battery_'):col.find('.')]
				print(battery_number)
				for ind in range(0, pmarksr):
					k = pmarks[col].iat[ind].split('/')
					if len(k)>1:
#						print(f'{col}:\t{k[1]}')
						if ncol == 0:
							ncol = k[1]
							time = pmarks.iat[ind, 0]
							print(ncol, time)
						elif ncol!=k[1]:
							print(col, ncol, ind, time, pmarks.iat[ind, 0], sep='\t')
							if ncol=='1' or ncol=='2' or ncol=='3' or ncol=='4' or ncol=='5':
								dictdatetime[ncol]+=[[time, pmarks.iat[ind, 0]]]
							ncol = k[1]
							time = pmarks.iat[ind, 0]
				headdf = []
				for el in dictdatetime:
					pdatas_start = 0
					pdatas_end = 0
					pdatas_datetimes = []
					print('el in dictdatetime:\t', el, len(dictdatetime[el]))
					if len(dictdatetime[el]):
						for elddt in dictdatetime[el]:
#							print('elddt:\t',elddt[0], elddt[1])
							for ipdatasdt in range(0, pdatasr):
								if pdatas.iat[ipdatasdt, 0] == elddt[0]:
									print('equ time:\t', ipdatasdt)
									pdatas_start = ipdatasdt
								if pdatas.iat[ipdatasdt, 0] == elddt[1]:
									print('equ time:\t', ipdatasdt)
									pdatas_end = ipdatasdt
							if pdatas_start<pdatas_end:
								pdatas_datetimes+=[[pdatas_start, pdatas_end]]
						print(pdatas_datetimes)
					
					batteryl = []
					col112 = []
					for pdcol in pdatas.columns:
						if pdcol.count('Bat') and pdcol.count(battery_number):
							batteryl+=[pdcol]
						
						if pdcol.count('112') and pdcol.count(Col_112[el]):
							col112+=[pdcol]
					
					print(sorted(batteryl))
					print(sorted(col112))
					l1 = dm.getcolname(pdatas, ['SO_'])
					print(l1)
					l1 = dm.getcolname(pdatas, ['OS'])
					print(l1)
					macrolist = sorted(batteryl)+sorted(col112)+dm.getcolname(pdatas, ['LAT'])+dm.getcolname(pdatas, ['SO_'])+dm.getcolname(pdatas, ['OS_'])
#					for gcn in dm.getcolname(pdatas, 'SO'):
#						macrolist+=
					print(len(macrolist), macrolist)
					for id1 in pdatas_datetimes:
						if id1==pdatas_datetimes[0]:
							frame = pdatas[macrolist].iloc[id1[0]:id1[1]]
						else:
							frame = pandas.concat([frame, pdatas[macrolist].iloc[id1[0]:id1[1]]])
						print(f'micro:\t{pdatas[macrolist].iloc[id1[0]:id1[1]].shape}')
						print(f'frame:\t{frame.shape}')
					fl = []
					if varframe==0:
						mframe = frame
						varframe+=1
					else:
						mframe = frame.append(frame,ignore_index=False)
					fl+=[frame]
					headdf+=[mframe]
#					kframe = pandas.concat(fl,ignore_index=False)
#					print('mframe.shape', mframe.shape)
				print(mframe.shape)
				for ih in headdf:
					print('hdf:\t', ih.shape)
#				for ih in range(0, len(headdf)):
#					if ih==0:
#						mframe = headdf[ih]
#					else:
#						mframe = mframe.append(headdf[ih],ignore_index=True)
#					mframe = frame.append(frame,ignore_index=False)
				hheaddf = pandas.concat(headdf)
				print('hheaddf.shape:\t', mframe.shape)
#				hheaddf.to_excel(all_files.paek_13)
		with pandas.ExcelWriter(all_files.paek_13) as writer:
			ind = 0
			for el in headdf:
				el.to_excel(writer, sheet_name="Sh_"+str(ind))
				ind+=1
#	for el in dictdatetime:
#		print(el)
#		for i in dictdatetime[el]:
#			print('dt:\t', i)

#		print(col)
#	for col in df.columns:
#		print(col)
#	gcol = sorted(df.columns.to_list())
#	for i in gcol:
#		print(i)
#	print(SKN_112, SKN_41, Col_112, apps)
	
#	dm.getstatdf(pmarks)
	
	
	
	
	
#	dict1 = {'l':[1,2,3], 'b':1}
#	dict1['l']+=['asdf']
#	print(dict1['l'])
	


#
#	end main_10
#
	
				

	

	
def seab():
	import numpy as np
	import pandas as pd
	import matplotlib.pyplot as plt
	import seaborn as sns
	df = pd.DataFrame(dict(time=np.arange(500),
                       value=np.random.randn(500).cumsum()))
	g = sns.relplot(x="time", y="value", kind="line", data=df)
	g.fig.autofmt_xdate()



if vmain==1:
	main()
elif vmain==2:
	main_2(namecol='RWork')
elif vmain==3:
	seab()
elif vmain==4:
	main_3(defsheet=1)
elif vmain==5:
	main_4(defsheet='Cut')
elif vmain==6:
	main_5()
elif vmain==7:
	main_6()
elif vmain==8:
	main_7(all_files.paek_7)
elif vmain==9:
	main_8(all_files.paek_3, defsheet='Y2')
elif vmain==10:
	main_10()


#pd = pandas.read_excel(all_files.paek_10, sheet_name='datas')
#pd = pandas.read_excel(all_files.paek_dir+'c.41.xlsx', sheet_name='datas')
#dm.getstatdf(pd)
#main_8(all_files.paek_dir+'c.41.xlsx', 'datas')
