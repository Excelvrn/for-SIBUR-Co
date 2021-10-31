# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 10:19:35 2021

@author: KhatuntsevSV
"""
'''
 - основной


'''

global var
var = 3

import os, time, sys, os.path
print(sys.platform)
if sys.platform=='linux':
	print(1)
	homedir = '/home/excelvrn/Pyth'
	sys.path+=[homedir + 'pandas-master']
	sys.path+=[homedir + 'numpy-main']
	import data_module_linux as dm
else:
	
	import data_module as dm
	
import  pandas, numpy


import all_files
all_files.adddir("C:/Users/Khatuntsevsv/Desktop/W/exp")

#all_files.adddir("C:\\Users\\Khatuntsevsv\\Desktop\\W\\pythlibs\\networkx-main")
#import networkx as nx

#import report_1

import datetime




#df = {'datas':pdatas, 'marks':pmarks}
sheets = {'marks':'Marks', 'col41':'col41marks'}
params41 = {'ARKM':'В работе АРКМ', 'ARK':'В работе АРК'}
col41time = {'1':[], '2':[], '3':[], '4':[]}
col41name = {'start':'AL_25_Column_41_', 'end':'_str'}

#AL_25_Battery_004.Model24H_str
colBatname = {'start':'AL_25_Battery_00', 'end':'.Model24H_str'}
marksBatd = {'M1':'АРКМ-27 ПН', 'M2':'АРКМ-15 ПН',\
			'M3':'АРКМ-15', 'M5':'АРК', 'M6':'АРКМ-27 Норман'}
markARKM_Bat = {'M1':'АРКМ-27 ПН', 'M2':'АРКМ-15 ПН',\
			'M3':'АРКМ-15', 'M6':'АРКМ-27 Норман'}
markARK_Bat = {'M5':'АРК'}


def getallvalues(series):
	l = series.to_list()
	setl = set(series.to_list())
	for i in setl:
		print(i)
def getallvaluesind(series):
	print(series.shape)
	for i in range(0, series.shape[0]):
#		print(i, series.iat[i])
		if series.iat[i] == params41['ARKM'] or series.iat[i] == params41['ARK']:
			print(i, series.iat[i])

def bat41w(filedoc=all_files.paek_14, defsheet=sheets['col41'] ):
	df = pandas.read_excel(filedoc, defsheet)
	
	rows, columns = df.shape
	print(rows, columns)
	
	colnames = []
	
	for col in df.columns:
		if col.count('41'):
#			print(col)
			colnames+=[col]
			
	for col in colnames:
		print(col)
#		getallvalues(df[col])
		ge = col.find(col41name['end'])
		gs = len(col41name['start'])
		col41number = col[gs:ge]
		print(col41number)
		for i in range(0, rows):
			if df[col].iat[i] == params41['ARKM']:
#				print(df[col].iat[i], i, sep='\t')
				col41time[col41number]+=[i]
	for k in col41time.keys():
		print(k, len(col41time[k]))
		for i in range(1, len(col41time[k])):
			last = col41time[k][i-1]
			cur = col41time[k][i]
			diff = cur - last
			if diff>1:
				print(k, type(last), type(cur), i-1,i)
#	for col in colnames:
#		print(col)
#		getallvaluesind(df[col])
#	print(col41name.keys())
	


def main(filedoc=all_files.paek_10, defsheet='datas', defsheet2='Marks' ):
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
#							print(ncol, time)
						elif ncol!=k[1]:
#							print(col, ncol, ind, time, pmarks.iat[ind, 0], sep='\t')
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

#
#	end main
#


def getbat41(filedoc=all_files.paek_14, defsheet=sheets['col41']):
	'''
	'''
#	filedoc=all_files.paek_14, defsheet=sheets['col41'] 
	pmarks = pandas.read_excel(filedoc, defsheet)
#	pmarks = pandas.read_excel(filedoc, defsheet2)
	rows, columns = pmarks.shape
	print(f'{rows} x {columns}')
#	print(pmarks.shape)
	marksBat = []
#	for col in pdatas.columns:
#		if 
	
	for col in pmarks.columns:
#		print(col)
#		print(col, col.count(col41name['start']))
#		col.find(colBatname['end'])
		if col.count(col41name['start']) and col.count(col41name['end']):
			cns = len(col41name['start'])
			cne = col.find(col41name['end'])
			colnum = col[cns:cne]
			print(col, colnum, sep='\t')
		else:
			continue
		periods =[]
		periodsm = []
		perdict={'ARKM':[], 'ARK':[]}
		for k in params41.keys():
			last = 0
			nlast = 0
			newparams41 = 0
			lastparams41 = 0
			stp = 0
			endp = 0
			for i in range(1, rows):
				if i==1:
					if params41[k]==pmarks[col].iat[i-1]:
						lastparams41 = 1
					else:
						lastparams41 = -1
				else:
					lastparams41 = newparams41
#				if i!=0:
#					last = i-1
#				d = i - last
#				if d==1:
#					continue
				if params41[k]==pmarks[col].iat[i]:
					newparams41 = 1
				else:
					newparams41 = -1
#				if params41[k]==pmarks[col].iat[i-1]:
#					lastparams41 = 1
#				else:
#					lastparams41 = -1
				
				
#				if lastparams41==1 and newparams41 == 1:
##					print('equ params')
#					pass
				if lastparams41==1 and newparams41 == -1:
#					print('equ stop')
					endp = i
#					print(k, stp, endp)
					periodsm+=[[stp, endp]]
#					print(periodsm)
					
					perdict[k]+=[[stp, endp]]
#					print(k, perdict[k])
				elif lastparams41==-1 and newparams41==1:
#					print('equ start')
					stp = i
#					print(i)
#				lastparams41 = newparams41
#			for ip in perdict:
#				print(ip)
#				for iip in ip:
#					print(iip)
			marksBat+=[perdict]
	print('marksBat')
	w = 0
	for i in marksBat:
		w+=1
		print(w, i)
		
	return marksBat
'''
1 {'ARKM': [[8, 18], [20, 26], [107, 108]], 'ARK': [[18, 20], [32, 34], [35, 53], [95, 104], [106, 107], [108, 132], [231, 235], [237, 277], [343, 377], [391, 392]]}
2 {'ARKM': [[8, 18], [20, 26], [107, 108]], 'ARK': [[18, 20], [32, 34], [35, 53], [95, 104], [106, 107], [108, 132], [231, 235], [237, 277], [343, 377], [391, 392]]}
3 {'ARKM': [], 'ARK': [[51, 95], [105, 106], [170, 190], [215, 231], [281, 310], [335, 336], [380, 381], [390, 397]]}
4 {'ARKM': [], 'ARK': [[51, 95], [105, 106], [170, 190], [215, 231], [281, 310], [335, 336], [380, 381], [390, 397]]}
5 {'ARKM': [[6, 7], [26, 41], [59, 77], [132, 152], [178, 190], [269, 273], [345, 349]], 'ARK': [[41, 51], [55, 59], [120, 132], [152, 162], [190, 204], [210, 215], [273, 285], [334, 335], [336, 345]]}
6 {'ARKM': [[6, 7], [26, 41], [59, 77], [132, 152], [178, 190], [269, 273], [345, 349]], 'ARK': [[41, 51], [55, 59], [120, 132], [152, 162], [190, 204], [210, 215], [273, 285], [334, 335], [336, 345]]}
7 {'ARKM': [[1, 8], [77, 85], [93, 116], [178, 180], [227, 233], [237, 255], [292, 306], [312, 338], [351, 352], [354, 355], [356, 357], [358, 359], [360, 361], [362, 363], [364, 365], [370, 371], [372, 395]], 'ARK': [[0, 1], [85, 93], [116, 120], [233, 237], [285, 286], [287, 292], [306, 312], [371, 372], [395, 397]]}
8 {'ARKM': [[1, 8], [77, 85], [93, 116], [178, 180], [227, 233], [237, 255], [292, 306], [312, 338], [351, 352], [354, 355], [356, 357], [358, 359], [360, 361], [362, 363], [364, 365], [370, 371], [372, 395]], 'ARK': [[0, 1], [85, 93], [116, 120], [233, 237], [285, 286], [287, 292], [306, 312], [371, 372], [395, 397]]}
'''
		
#colBatname = {'start':'AL_25_Battery_00', 'end':'.Model24H_str'}
def getbat(filedoc=all_files.paek_14, defsheet=sheets['marks']):
	'''
	'''
#	filedoc=all_files.paek_14, defsheet=sheets['col41'] 
	pmarks = pandas.read_excel(filedoc, defsheet)
#	pmarks = pandas.read_excel(filedoc, defsheet2)
	rows, columns = pmarks.shape
	
#	print(pmarks.shape)
	marksBat = []
#	for col in pdatas.columns:
#		if 
	l = []
	for col in pmarks.columns:
		if col.count(colBatname['start']) and col.count(colBatname['end']):
			cns = len(colBatname['start'])
			cne = col.find(colBatname['end'])
			colnum = col[cns:cne]
			print(col, colnum, sep='\t')
			print(col)
			l+=pmarks[col].to_list()
			print(set(pmarks[col].to_list()))
	print('l:\n\t',set(l))
	
	
# main2
import dataframe_41_head_1 as dh

def main2(data1=all_files.paek_10, data2=all_files.paek_14):
	if sys.platform!='linux':
#	df11 = pandas.read_excel(data1, dh.df1sh1 )
		print(data1.split(sep='\\'))
		df12 = pandas.read_excel(data1, dh.df1sh2 )
		df12r, df12c = df12.shape
		df21 = pandas.read_excel(data2, dh.df2sh1 )
		df21r, df21c = df21.shape
		df22 = pandas.read_excel(data2, dh.df1sh2 )
	else:
		homedir = '/home/excelvrn/W/PAEK/'
		print(data1.split(sep='\\'))
		g = data1.split('\\')
		g = g[len(g)-1]
		print(f'g:\t{g}')
		print(f'g:\t{homedir + g}')
		
		df12 = pandas.read_excel(homedir+g, dh.df1sh2 )
		df12r, df12c = df12.shape
		print(data1.split(sep='\\'))
		g = data2.split('\\')
		g = g[len(g)-1]
		df21 = pandas.read_excel(homedir+g, dh.df2sh1 )
		df21r, df21c = df21.shape
		df22 = pandas.read_excel(homedir+g, dh.df1sh2 )
		
	
	intel = []
	
#	print(dm.getcolname(df11, ['Bat']))
	#print(dm.getcolname(df12, ['Bat','Model24H_str']))
#	print(dm.getcolname(df21, ['Bat', 'Model24H_str']))
#	print(dm.getcolname(df22, ['Bat', 'Model24H_str']))
	
	#print( len(dm.getindexes(df12, 'AL_25_Battery_002.Model24H_str', 'АРК')) )
	# AL_25_Battery_001.Model24H_str - mark
	# AL_25_Battery_001.Column24H_str - worked column
	main_battery_numer = str(2)
	'AL_25_Battery_002.Model24H_str'
	sl = set(df12[	'AL_25_Battery_00' + \
					main_battery_numer +\
					'.Model24H_str'].to_list())
	print('sl:\t', sl)
	
	#main list consists of mark, #bat, #col-112, #col-41, time-start, time-end
	mainlist = []
	
	#esl is mark
	for esl in sl:
		print(f'***\tMark:\t{esl}')
		if esl == '-':
			continue
		gotlist = dm.getindexes(df12, 'AL_25_Battery_00' + main_battery_numer +'.Model24H_str', esl)
#		print( esl, len(gotlist) )
		gti = dm.gettimeinterval(	 df12,\
							 dm.getcolnamebynumcol(df12, 0),\
							 gotlist)
#		print(df12.iat[0,0], '\n', dm.addtime(df12.iat[0,0], 3600))
		print(f'Mark consitsts at {len(gti)} periods and these are:\n\t{gti}')
#		timeseriesall = []
		for igti in gti:
			print('gti')
			for iigti in igti:
				print(f'\t{iigti}')
		for i in gti:
#			print(i)
			print('\t\t*******')
			timeseries = dm.gettimeseries(i[0], i[1])
			print(i[0], i[1],len(timeseries))
#			timeseriesall+=[timeseries]
		print('\t\t*******')
		curcolnumer = dm.getbeetstr('AL_25_Battery_001.Model24H_str',\
				 'AL_25_Battery_00',\
				 '.Model24H_str')
		
		print('numer:\t', curcolnumer)
		
		#main_battery_numer
		
		#workedbat_columntag = 'AL_25_Battery_00' + str(curcolnumer)+'.Column24H_str'
		workedbat_columntag = 'AL_25_Battery_00' + main_battery_numer+'.Column24H_str'
		
		print('tag is\t', workedbat_columntag, len(df12[workedbat_columntag]))
		
		set_workedbat_col = set(df12[workedbat_columntag].to_list())
		print(f'set_workedbat_col:\t{set_workedbat_col}')
		
		print(len(gti))
		g = []
		for time in gti:
#			for time_el in time:
#				print(type(time_el))
#			for time_el in time:
#			print('workedbat_columntag:\t', workedbat_columntag)
			coll = []
			for ind in range(time[4], time[5]):
				if df12[workedbat_columntag].iat[ind]!='-':
					if type(df12[workedbat_columntag].iat[ind]) == str:
#						print('df12[workedbat_columntag].iat[ind]:\t',\
#							 df12[workedbat_columntag].iat[ind])
						name = df12[workedbat_columntag].iat[ind].split('/')
#						print(len(name))
						if len(name)==2:
#							print(workedbat_columntag, name[1])
							coll+=[name[1]]
#					df12[workedbat_columntag].iat[ind]
#				else:
#					print(' - - -\t', ind)
			set_coll=set(coll)
			# isc is 112-col number
			for isc in set_coll:
				scl=[]
				periods_col_112 = []
				print(f'{isc} in set_coll\t\ttime:\t{time[4]}\t{time[5]}')
				for ind in range(time[4], time[5]):
					if type(df12[workedbat_columntag].iat[ind]) == str:
#						print('df12[workedbat_columntag].iat[ind]:\t',\
#							 df12[workedbat_columntag].iat[ind])
						name = df12[workedbat_columntag].iat[ind].split('/')
#						print(len(name))
						if len(name)==2:
#							print(workedbat_columntag, name[1])
							if name[1] == isc:
#								print('isc', isc, ind)
								scl+=[ind]
								periods_col_112+=[ind]
								if ind < df12r:
									intel+=[[esl,ind, main_battery_numer, curcolnumer, \
				  df12.iat[ind, 0], df12.iat[ind+1, 0]\
				  ]]
#				print(f'***{isc} col-112`s period: {periods_col_112} ')
				print('scl:\t', isc, len(scl))
	# AL_25_Column_41_3_str
	# df21
	mark_work_41col = dm.getcolname(df21, ['AL_25_Column_41', 'str'])
	print('mark_work_41col:\t\n\t',mark_work_41col)
#	mw41coll = []
#	for cols in mark_work_41col:
#		mw41coll+=df21[cols].to_list()
#	print(set(mw41coll))
	col41dtl = []
	for iel in intel:
		cond = 0
#		params41 = {'ARKM':'В работе АРКМ', 'ARK':'В работе АРК'}
		if iel[0] == 'АРК':
			cond = params41['ARK']
		elif iel[0] == 'АРКМ':
			cond = params41['ARKM']
		else:
			continue
#		print(f'\t\t*** {cond} ***')
		for col in mark_work_41col:
			nncol = -1
			for ncol in range(0, df21c):
				if col == df21.columns[ncol]:
					nncol = ncol
			if nncol==-1:
				continue
#			colnum = dm.getcolnamebynumcol()
			for ind in range(0, df21r):
				if cond == df21.iat[ind,nncol] and\
				df21.iat[ind,0].timestamp()>=iel[4].timestamp() and\
				df21.iat[ind,0].timestamp()<=iel[5].timestamp() :
#					print('\tcond', col, '\t', ind)
#					col41dtl+=[[col, iel, ind, df21.iat[ind,0]]]
					col_f1 = len('AL_25_Column_41_')
					col_f2 = col.find('_str')
					col41dtl+=[[iel[2], iel[3],int(col[col_f1:col_f2]),\
						ind,\
						df21.iat[ind,0]\
							]]
					#iel+=[int(col[col_f1:col_f2])]
	
			
	print('---***---***---***---')
#	for i in intel:
#		print('intel:\t',i)
				

#		print('gti:\t', gti)
	print(f'\t\tcol41dtl {len(col41dtl)} element(s)')
	maxl = 0
	dm.flprint(col41dtl)
	for i in intel:
		if i == intel[0] or i == intel[len(intel)-1]:
			print('intel')
			for ii in i:
				print('\t', ii)
	#for el in 	set(col41dtl):
		#if el == col41dtl[0]:
			#maxl = len(el)
		#elif len(el)>maxl:
			#maxl = len(el)
		#if len(el)==maxl:
			#print(el)
		

	
	
	
	
	
#		
work = 5
if work == 1:			
	main()
elif work ==2:
	bat41w()
elif work ==3:
	getbat41()
elif work ==4:
	getbat()
elif work ==5:
	main2()

	

	
