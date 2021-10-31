# -*- coding: utf-8 -*-

run = 14
"""
run == 1
run == 2
run == 3
run == 4
run == 5
run == 6
run == 7
run == 8
run == 9    Извлечение показателя значения и даты измерения насыпной плотности,
			извлечение времени и показателей значений датчиков с последующим
			формированием единого документа, содержащего перечисленные выше значения.
			Вычисление показателя значения корреляции из сформированного файла
			с последующим формированием отдельного файла
run == 10 Отладка
run == 11 Формирование xlsx-файла, содержащего тег и его описание
run == 12 Формирование xlsx-файла, вытащить первую строку и сравнить по колонкам значения
run == 13 п.9, но без файловаго вывода
run == 14 analysing of SJAP



Это временный скриптовый файл.
Выгрузка данных через интервал времени: 24 х количество дней / количество тегов 

f - рабочий документ
shn - рабочий лист
"""
f="C:/Users/Khatuntsevsv/Desktop/W/Datas/FQR1461.xlsx"
FRCA1411="C:/Users/Khatuntsevsv/Desktop/W/Datas/FRCA1411.xlsx"
MR201A102407="C:/Users/Khatuntsevsv/Desktop/W/Datas/MR201A.1024.07.xlsx"
MR201A101305="C:/Users/Khatuntsevsv/Desktop/W/Datas/MR201A.1013.05.xlsx"
MR201_temperature_txt="C:/Users/Khatuntsevsv/Desktop/W/Datas/MR201.A.txt"
fBuLi="C:/Users/Khatuntsevsv/Desktop/W/Datas/BuLi/BuLi.913.05.21.xlsx"
fBuLi_2="C:/Users/Khatuntsevsv/Desktop/W/Datas/BuLi/BuLi.2021.xlsx"
fBuLi_3="C:/Users/Khatuntsevsv/Desktop/W/Datas/BuLi/BuLi.2021.c.1.xlsx"
fBuLi_4="C:/Users/Khatuntsevsv/Desktop/W/Datas/BuLi/BuLi.2021.c.2.xlsx"
fNP="C:/Users/Khatuntsevsv/Desktop/W/Datas/BuLi/NP.01-05.21.xlsx"
fparties="C:/Users/Khatuntsevsv/Desktop/W/Datas/BuLi/Parties.xlsx"
fKV="C:/Users/Khatuntsevsv/Desktop/W/Datas/BuLi/KV.jan.2021.xlsx"
fKV_full="C:/Users/Khatuntsevsv/Desktop/W/Datas/BuLi/FullCycle.11_12.jan.2021.xlsx"
fKV_full_14="C:/Users/Khatuntsevsv/Desktop/W/Datas/BuLi/FullCycle.13_14.jan.2021.xlsx"
fKV_full_BC14="C:/Users/Khatuntsevsv/Desktop/W/Datas/BuLi/FullCycle.BC.13_14.jan.2021.xlsx"
fKV_full_BC13_27="C:/Users/Khatuntsevsv/Desktop/W/Datas/BuLi/FullCycle.BC.13_27.jan.2021.xlsx"
SJAP="C:/Users/Khatuntsevsv/Desktop/W/Datas/BuLi/SJAP.01_02.2021.xlsx"
#MR201_temperature_txt = "\\tsclient\C\Users\Khatuntsevsv\Desktop\W\Datas\MR201.temperature.txt"
#------------------------------------------------------------
suschka = "C:\\Users\\Khatuntsevsv\\Desktop\\W\\Datas\\Suh\\Pylx.xlsx"
#------------------------------------------------------------
shn=2#sheet_name=2

M_nBuLi = 66
M_DDS = 129
M_SiCl4 = 170

'''
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.values.html
Time - https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html?highlight=timestamp#pandas.Timestamp

Indexing in Numpy:a.to_numpy()[0,0]

'''
import os
import  sys, pandas, numpy, matplotlib, math, statistics
import seaborn as sbrn
import matplotlib.pyplot as mpl
from decimal import *

import all_files
all_files.adddir("C:/Users/Khatuntsevsv/Desktop/W/exp")

#all_files.adddir("C:\\Users\\Khatuntsevsv\\Desktop\\W\\pythlibs\\networkx-main")
import networkx as nx

import report_1

import data_module as dm
dm.PR()


#import 

print("sys. dirs:")
for i in range(0, len(sys.path)):
	print(sys.path[i])
	#sys.path+=['C:\asdfsadf']
			
def get012list(l):
	g=[]
	for i in range(0, len(l)):
		if l[i]=="Null":
			g+=[0]
		else:
			g+=[l[i]]
	return g

def get_timelist(timel, datal):
	trig=-1
	mainlist = []
	advlist=[]
	for i in range(1, len(datal)):
		if trig==-1 and datal[i-1]==0 and datal[i]==1:
			advlist+=[timel[i].timestamp()]
			trig = 1
		elif trig == 1 and datal[i]==0 and datal[i-1]==1:
			trig = -1
			advlist+=[timel[i].timestamp()]
			mainlist+=[advlist]
			advlist=[]
	return mainlist
def minusmin(tlist, min_time):
	g=[]
	gg = []
	for i in range(0, len(tlist)):
		for i2 in range(0, len(tlist[i])):
			gg+= [int(tlist[i][i2]- min_time)]
		g+=[gg]
		gg=[]
	return g


def KV(filename, sheetname):
	'''
	Read file contained
	'''
	a=pandas.read_excel(filename,sheetname)
	print(a.shape)
	"""
	0 - закрыт 
	1 - открыт
	Стирол - 
	"""
	time_process=a.iloc[:, 0]
	
	Styrol = a.iloc[:, 1]
	gStyrol = get012list(Styrol)
	tStyrol = get_timelist(time_process, gStyrol)

	BuLi = a.iloc[:, 4]
	gBuLi = get012list(BuLi)
	tBuLi = get_timelist(time_process, gBuLi)
#	for i in range(0, len(BuLi)):
#		if BuLi[i]=="Null":
#			BuLi[i]=2
#	
	SA1 = a.iloc[:, 7]
	gSA1 = get012list(SA1)
	tSA1 = get_timelist(time_process, gSA1)
#	for i in range(0, len(SA1)):
#		if SA1[i]=="Null":
#			SA1[i]=2
#	
	Buta = a.iloc[:, 10]
	gButa = get012list(Buta)
	tButa = get_timelist(time_process, gButa)

	print("Lists are loaded")
	listcompare=[]
	if len(tStyrol):
		listcompare+=[tStyrol[0][0]]
	if len(tBuLi):
		listcompare+=[tBuLi[0][0]]
	if len(tSA1):
		listcompare+=[tSA1[0][0]]
	if len(tButa):
		listcompare+=[tButa[0][0]]
	mintime = min(listcompare)
	print("MT:\t", mintime)
	
	normStyrol = minusmin(tStyrol, mintime)
	normBuLi = minusmin(tBuLi, mintime)
	normSA1 = minusmin(tSA1, mintime)
	normButa = minusmin(tButa, mintime)
	print("NormStyrol:\t", normStyrol)
	
	styroldata = []
	BuLidata = []
	SA1data = []
	Butadata=[]
	for i in range(0, 600000):
		styroldata+=[0]
		BuLidata+=[0]
		SA1data+=[0]
		Butadata+=[0]
		
	for i in range(0, len(normStyrol)):
		for i2 in range(normStyrol[i][0], normStyrol[i][1]):
			styroldata[i2] = 1
	for i in range(0, len(normBuLi)):
		for i2 in range(normBuLi[i][0], normBuLi[i][1]):
			BuLidata[i2] = 2
	for i in range(0, len(normSA1)):
		for i2 in range(normSA1[i][0], normSA1[i][1]):
			SA1data[i2] = 3
	for i in range(0, len(normButa)):
		for i2 in range(normButa[i][0], normButa[i][1]):
			Butadata[i2] = 4
	lims=3600*24*4 + 0
	lime = lims + 3600*24
	x = range(lims, lime)
	mpl.plot(x,styroldata[lims:lime], 'r-',x,BuLidata[lims:lime], 'b-',x,SA1data[lims:lime], 'k-',x,Butadata[lims:lime], 'c-')
	mpl.show()
	
def KVV(filename, sheetname, col, lday):
	'''
	Read file contained
	'''
	a=pandas.read_excel(filename,sheetname)
	print(a.shape)
	"""
	0 - закрыт 
	1 - открыт
	Стирол - 
	"""

	
	time_process=a.iloc[:, 0]
	
	Styrol = a.iloc[:, col]
	gStyrol = get012list(Styrol)
	tStyrol = get_timelist(time_process, gStyrol)

	BuLi = a.iloc[:, col+3]
	gBuLi = get012list(BuLi)
	tBuLi = get_timelist(time_process, gBuLi)
#	for i in range(0, len(BuLi)):
#		if BuLi[i]=="Null":
#			BuLi[i]=2
#	
	SA1 = a.iloc[:, col+3*2]
	gSA1 = get012list(SA1)
	tSA1 = get_timelist(time_process, gSA1)
#	for i in range(0, len(SA1)):
#		if SA1[i]=="Null":
#			SA1[i]=2
#	
	Buta = a.iloc[:, col+3*3]
	gButa = get012list(Buta)
	tButa = get_timelist(time_process, gButa)

	print("Lists are loaded")
	listcompare=[]
	if len(tStyrol):
		listcompare+=[tStyrol[0][0]]
	if len(tBuLi):
		listcompare+=[tBuLi[0][0]]
	if len(tSA1):
		listcompare+=[tSA1[0][0]]
	if len(tButa):
		listcompare+=[tButa[0][0]]
	mintime = min(listcompare)
	print("MT:\t", mintime)
	
	normStyrol = minusmin(tStyrol, mintime)
	normBuLi = minusmin(tBuLi, mintime)
	normSA1 = minusmin(tSA1, mintime)
	normButa = minusmin(tButa, mintime)
	print("NormStyrol:\t", normStyrol)
	
	styroldata = []
	BuLidata = []
	SA1data = []
	Butadata=[]
	for i in range(0, 600000):
		styroldata+=[0]
		BuLidata+=[0]
		SA1data+=[0]
		Butadata+=[0]
		
	for i in range(0, len(normStyrol)):
		for i2 in range(normStyrol[i][0], normStyrol[i][1]):
			styroldata[i2] = 1
	for i in range(0, len(normBuLi)):
		for i2 in range(normBuLi[i][0], normBuLi[i][1]):
			BuLidata[i2] = 2
	for i in range(0, len(normSA1)):
		for i2 in range(normSA1[i][0], normSA1[i][1]):
			SA1data[i2] = 3
	for i in range(0, len(normButa)):
		for i2 in range(normButa[i][0], normButa[i][1]):
			Butadata[i2] = 4
#	lims=3600*24*lday + 01
#	lime = lims + 3600*24
#	x = range(lims, lime)
#	mpl.plot(x,styroldata[lims:lime], 'r-',x,BuLidata[lims:lime], 'b-',x,SA1data[lims:lime], 'k-',x,Butadata[lims:lime], 'c-')
#	mpl.show()

	
	
#	minStyrol = minusmin(tStyrol, mintime)
#	print(minStyrol)
#	
	
	
	
	
	
#	print("Min:\t", mintime)

'''
P l o t
	lims=300
	lime = 100 + lims
	
	x = range(lims, lime)
	mpl.plot(x, gStyrol[lims:lime], "r--", x, gBuLi[lims:lime], "g-", x, gButa[lims:lime], "c-", x, gSA1[lims:lime], "m-")
	mpl.show()
'''
def run4(filename, sh):
	g=pandas.read_excel(filename, sh)
	'''
	*********************************************************
	
	********************* R A S C H O D *********************
	
	*********************************************************
	'''
	try:
		time_time, temp_time, press_time = dm.time_temp_pressure(g, 0, 6, 8)
		
		styrol = dm.raschod(g, 0, 1, 9)
		print("dm\tstyrol:\n", styrol)
		
		BuLi_list = dm.raschod(g, 0, 2, 10)
		print("dm\tBuLi:\n", BuLi_list)
		
		SiCl = dm.raschod(g, 0, 3, 11)
		print("dm\tSiCl:\n", SiCl)
		
		DDS = dm.raschod(g, 0, 4, 12)
		print("dm\tDDS:\n", DDS)
		
		Butadien  = dm.raschod(g, 0, 5, 13)
		print("dm\tButadien:\n", Butadien)
		
		time_react = dm.getraschodintocycle(BuLi_list)
		print("time_react:\n", time_react)
		#tm, tmpl = dm.lin_temp(g, 0, 6)
		
		tm, pressl = dm.lin_temp(g, 0, 8)
		tеm, temp= dm.lin_temp(g, 0, 6)
	
		for i in range(0, len(pressl)) :
	#		print("\t", i)
			pressl[i] = pressl[i]*1000
	#		print("\t\t", i)
		for i in range(0, len(temp)) :
	#		print("\t", i)
			temp[i] = temp[i]+dm.Kelvin
	except TypeError:
		print("Null")
		print("\tNull")
		print("\t\tNull")
	else:
	#		print("\t\t", i)
		Synthez_styrol = dm.GetReagentsOfSyntheze2(time_react, styrol, time_time)
		print("GetReagentsOfSyntheze Styrol:")
		for i in Synthez_styrol:
			print(i[0], i[1], i[2], sep="\t\t")
			
		Synthez_Butadien = dm.GetReagentsOfSyntheze2(time_react, Butadien, time_time)
		print("GetReagentsOfSyntheze Butadien:")
		for i in Synthez_Butadien:
			print(i[0], i[1], i[2], sep="\t\t")
		
		Syntheze_SiCl =  dm.GetReagentsOfSyntheze2(time_react, SiCl, time_time)
		print("GetReagentsOfSyntheze SiCl:")
		for i in Syntheze_SiCl:
			print(i[0], i[1], i[2], sep="\t\t")
		
		Syntheze_DDS = dm.GetReagentsOfSyntheze2(time_react, DDS, time_time)
		print("GetReagentsOfSyntheze DDS")
		for i in Syntheze_DDS:
			print(i[0], i[1], i[2], sep="\t\t")
			
		
		Syntheze_BuLi = dm.GetReagentsOfSyntheze2(time_react, BuLi_list, time_time)
		print("GetReagentsOfSyntheze BuLi")
		for i in Syntheze_BuLi:
			print(i[0], i[1], i[2], sep="\t\t")
		
		print("start,s", "end,s", "Styrol", "Butadien", "SiCl", "DDS", "n-BuLi", sep="\t")
		for i in range(0, len(Synthez_Butadien)):
			print(Synthez_Butadien[i][0], Synthez_Butadien[i][1],\
				 Synthez_styrol[i][2],\
				 Synthez_Butadien[i][2], \
				 Syntheze_SiCl[i][2],\
				 Syntheze_DDS[i][2], \
				 Syntheze_BuLi[i][2], sep="\t")
		
	#	dm.GetReagentsOfSyntheze2(time_react, BuLi_list, time_time)
#		
#		mpl.grid()
#		l1, l2 = mpl.plot(tm,pressl, 'r-', tm,temp, 'b-')
#		mpl.legend((l1, l2), ('Pressure, kPa', 'Temperature, K'), loc='upper right', shadow=True)
#		mpl.show()


def runprogram():
	if run==10:
		print("\n\t*** debug!")
		print("\t\t*** debug!")
		print("\t\t\t*** debug!\n")
	else:
		print("\n\t*** run!", run)
	
	readfile = fKV
	if run == 1:
		KV(readfile, 10)
	elif run == 2:
		KVV(readfile, 10, 2, 5)
	elif run == 3:
		import math
		for i in range(273, 400, 10):
			print(i, math.e**((i+5)/i))
	elif run == 4:
		#dm.dates(datetime.date(2021, 8, 18))
#		run4(fKV_full, "A.jan.11_12.2021")
#		print("-------   -------")
		#run4(fKV_full_14, "A.jan.13_14.2021")
#		run4(fKV_full_BC14, "C140121")
		for i in range(2, 5):
			print("------------------------------------")
			print("------------------------------------")
			print("------------------------------------")
			print(i, "/25")
			print("------------------------------------")
			print("------------------------------------")
			print("------------------------------------")
			run4(fKV_full_BC13_27, i)
	elif run == 5:
		print(run)
		report_1.run5(report_1.SAP_REPORT, 2)
	elif run == 6:
		
		print("Cur.dir:\t", os.getcwd())
#		gpd = pandas.DataFrame([['a', 'b'], ['c', 'd']], columns=["Col1", "col2"], index=["ind1", "ind2"])
#		gpd.to_excel(all_files.writedatas, sheet_name='startsheet')
		sh=2
		'''
		Suschka
		'''
		dm.covar_excel(all_files.Pylx_1, 6, all_files.writedatas)
#		g=pandas.read_excel(suschka, sh)
#		t1 = g.iloc[:, 7]
#		t2 = g.iloc[:, 8]
#		t3 = g.iloc[:, 9]
#		t4 = g.iloc[:, 4]
#		for i in range(0, len(t1)):
#			if t1[i]=='Null':
#				t1[i]=0
#		for i in range(0, len(t2)):
#			if t2[i]=='Null':
#				t2[i]=0
#		for i in range(0, len(t3)):
#			if t3[i]=='Null':
#				t3[i]=0
#		for i in range(0, len(t3)):
#			if t4[i]=='Null':
#				t4[i]=0
##		xt2=range(0, len(t2))
##		print(pandas.isna(t1))
##		for i in range(0, len(t1)):
#
#		x = range(0, len(t1))
##		mpl.plot(x,t1, 'r-',x,t2, 'b-',x,t3, 'k-')
##		mpl.plot(x,t1, 'r-', x,t2, 'b-', x,t3, 'm-', x,t4, 'c-')
#		mpl.plot(x,t1, 'r-', x,t2, 'b-', x,t3, 'm-')
#		mpl.show()
	elif run == 7:
		nodes = dm.open_txt(all_files.tops)
		
#		DG = nx.read_edgelist(all_files.graph3, delimiter="\t",nodetype=str)
		DG = nx.read_weighted_edgelist(all_files.graph4,\
							 delimiter="\t",\
							 nodetype=str, create_using=nx.DiGraph)
		
		print(nx.nodes(DG))
		
		for i in nx.nodes(DG):
			print(DG.neighbors(i).__iter__())
#		DG.add_nodes_from(nodes)
#		DG.add_edge(nodes[0], nodes[1])
		
#		print(type(DG))
#		G = nx.petersen_graph()
#		print(G)
		po1s = nx.random_layout(DG)
		nx.draw(DG,pos = po1s, with_labels=True, arrowsize=14, edge_color='r')
#		nx.draw_networkx_edges(DG, pos=None,arrows=True,with_labels=True, font_weight='bold')
	elif run == 8:
		
		print("Cur.dir:\t", os.getcwd())
#		gpd = pandas.DataFrame([['a', 'b'], ['c', 'd']], columns=["Col1", "col2"], index=["ind1", "ind2"])
#		gpd.to_excel(all_files.writedatas, sheet_name='startsheet')
		'''
		Suschka
		'''
		dm.covar_excel3(all_files.Pylx_1, 2, all_files.Pylx_2, 2, all_files.writedatas)
		
		
	elif run == 9:
		'''
		get nas.pl from report http://s103as-mes-rs.sibur.local/SSRSServer/Pages/ReportViewer.aspx?%2fLIMS+Reports%2f%d0%9f%d1%80%d0%be%d0%b8%d0%b7%d0%b2%d0%be%d0%b4%d1%81%d1%82%d0%b2%d0%be+%d1%82%d0%b5%d1%80%d0%bc%d0%be%d1%8d%d0%bb%d0%b0%d1%81%d1%82%d0%be%d0%bf%d0%bb%d0%b0%d1%81%d1%82%d0%be%d0%b2%2f%d0%93%d0%be%d1%82%d0%be%d0%b2%d0%b0%d1%8f+%d0%bf%d1%80%d0%be%d0%b4%d1%83%d0%ba%d1%86%d0%b8%d1%8f+%d0%a2%d0%ad%d0%9f+(%d0%b4%d0%bb%d1%8f+%d0%bf%d1%80%d0%be%d0%b8%d0%b7%d0%b2%d0%be%d0%b4%d1%81%d1%82%d0%b2%d0%b0)&rs:Command=Render
		'''
#		dm.getnasplins(all_files.record_1)
		recordsdatas = pandas.read_excel(all_files.record_1, 4)
# ***		
		naspldatas = dm.getnaspl(all_files.record_2, 1, 0, 15)
		
		dm.getnasplins2(naspldatas, recordsdatas, all_files.record_2_0_saved, all_files.record_2_1_saved)
# ***
	elif run == 10:
		dm.getnasplins_debug( )
	elif run == 11:
		dm.getcolumnsnames(all_files.record_1,\
							 3				,\
							 all_files.record_1_tags)
	elif run == 12:
		g3 = pandas.read_excel(all_files.record_1,\
							 3)
		g4 = pandas.read_excel(all_files.record_1,\
							 4)
		g31 = g3.iloc[0, :]
		g41 = g4.iloc[0, :]
		
		g3col = g3.columns
		
		gl = []
		for i in range(0, len(g31)):
			for i2 in range(0, len(g41)):
				if g31[i] == g41[i2]:
					print(g3col[i],i, i2)
					gl+=[[g3col[i],i, i2]]
		gldf = pandas.DataFrame(gl)
		gldf.to_excel(all_files.record_2_3_saved)
	elif run == 13:
		'''
		get nas.pl from report http://s103as-mes-rs.sibur.local/SSRSServer/Pages/ReportViewer.aspx?%2fLIMS+Reports%2f%d0%9f%d1%80%d0%be%d0%b8%d0%b7%d0%b2%d0%be%d0%b4%d1%81%d1%82%d0%b2%d0%be+%d1%82%d0%b5%d1%80%d0%bc%d0%be%d1%8d%d0%bb%d0%b0%d1%81%d1%82%d0%be%d0%bf%d0%bb%d0%b0%d1%81%d1%82%d0%be%d0%b2%2f%d0%93%d0%be%d1%82%d0%be%d0%b2%d0%b0%d1%8f+%d0%bf%d1%80%d0%be%d0%b4%d1%83%d0%ba%d1%86%d0%b8%d1%8f+%d0%a2%d0%ad%d0%9f+(%d0%b4%d0%bb%d1%8f+%d0%bf%d1%80%d0%be%d0%b8%d0%b7%d0%b2%d0%be%d0%b4%d1%81%d1%82%d0%b2%d0%b0)&rs:Command=Render
		'''
#		dm.getnasplins(all_files.record_1)
		recordsdatas = pandas.read_excel(all_files.record_1, 2)
		print("\tOpen recordsdatas")
# ***		
		naspldatas = dm.getnaspl_1_0(all_files.record_2, 1, 0, 15)
		naspldatas.to_excel(all_files.exp_1)
		dm.getnasplins3(naspldatas, recordsdatas, all_files.exp_2, all_files.exp_3)
# ***
	elif run == 14:
		dm.getmaxmin(all_files.SJAP,1 )

#getmin2(temp1)
#datas()
runprogram()


