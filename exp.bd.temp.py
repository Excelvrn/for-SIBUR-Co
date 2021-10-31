# -*- coding: utf-8 -*-
"""
Редактор Spyder

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
#MR201_temperature_txt = "\\tsclient\C\Users\Khatuntsevsv\Desktop\W\Datas\MR201.temperature.txt"
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
import  sys, pandas, numpy, matplotlib, math
import matplotlib.pyplot as mpl


#import 

print("sys. dirs:")
for i in range(0, len(sys.path)):
	print(sys.path[i])
	#sys.path+=['C:\asdfsadf']
def readfile(readfile,separ):
	'''
	#print(sys.argv,  "\n\n\n")
	#print(sys.version, sys.version_info, sep='\n')
	#a=pandas.read_excel(f, sheet_name)
	'''
	a=pandas.read_csv(f,delimiter = separ )
#	numpy_a = a.to_numpy()
#	print(a.columns)
#	print(a.shape)
	return a
def main():
	a = pandas.read_csv(MR201_temperature_txt)
#	a = open(MR201_temperature_txt)
#	a = open(MR201_temperature_txt)
	print(a.iloc[1])
#	print(a.shape)
#	print(a.iat[3,3])
#	print(a.iloc[2])
#	print("len:\t", len(a.iloc[2]))
#	for i in range(0, len(a.iloc[2])):
#		print(i, type(a.iloc[2][i]), sep="\t")
#	
#	allel_list=[]
#	streamsum=0
#	count=0
#	datemass=[]
#	for i in range(0, a.shape[0]):
#		if i>0:
#			tdelta = a.iloc[i][0].timestamp()-a.iloc[i-1][0].timestamp()
#			stream = a.iloc[i-1][1]
#			allel = tdelta * stream
#			streamsum+=allel
##			if allel<1:
##				streamsum = 0
##			print(i, tdelta, stream, allel, streamsum, sep="\t")
#			if allel<1 and tdelta>100:
#				count+=1
#				print(count, a.iloc[i-1][0], streamsum, sep="\t")
#				datemass+=[a.iloc[i-1][0], streamsum]
#				streamsum = 0
'''
SELECT COUNT(*) as count FROM 
'''
	
def main2():
#	a = readfile(MR201A102407, 7)
	a=pandas.read_excel(MR201A102407, 6)
	print(a.shape)
	print(a.columns)
	print(a.iloc[0])
	'''
	min-max temperature
	'''
#	print(a.iloc[:,0])
	g=a.iloc[:,4]
	updown=0
	iterprocess = 0
	uplist=[]
	downlist=[]
	for i in range(0, len(g)):
		if g[i]>50:
			if updown == 0:
				iterprocess+=1
#				print(iterprocess, i, g[i])
				uplist+=[i]
			updown = 1
#			print(i, g[i], sep="\t")
		else:
			if updown == 1:
				downlist+=[i]
			updown = 0
	full=uplist + downlist
	print(len(uplist), len(downlist), len(full))
	sortedfull=sorted(full)
#	print(full)
#	print(sortedfull)
	'''
	periods
	'''
	modifiedfull=[]
	timelist=a.iloc[:,0]

#	for i in range(0, len(sortedfull)):
#		print(timelist[sortedfull[i]])
	if full[0]==uplist[0]:
		print("uplist")
		for i in range(0, len(full),2):
#			print(i)
			if i>0:
				modifiedfull+=[[full[i-2], full[i-1]]]
#		print("modifiedfull:", modifiedfull)
		prep1461=a.iloc[:,1]
		prep1471=a.iloc[:,2]
		prep1411=a.iloc[:,3]
		
		for i in range(0, len(modifiedfull)):
			sprep1461=0
			sprep1471=0
			sprep1411=0
			for i2 in range(modifiedfull[i][0], modifiedfull[i][1]):
				if i2>0:
					timedelta1=timelist[i2].timestamp()
					timedelta2=timelist[i2-1].timestamp()
					timedelta3=timedelta1-timedelta2
#					print(timedelta1, timedelta2)
					sprep1461+=(prep1461[i2]*timedelta3)
					sprep1471+=(prep1471[i2]*timedelta3)
					sprep1411+=(prep1411[i2]*timedelta3)
					
			if sprep1461<0.01:
				sprep1461=0
			else:
				sprep1461=sprep1461/3600
			if sprep1471<0.01:
				sprep1471=0
			else:
				sprep1471=sprep1471/3600
			if sprep1411<0.01:
				sprep1411=0
			else:
				sprep1411=sprep1411/3600
			
			modifiedfull[i].append(sprep1461)
			modifiedfull[i].append(sprep1471)
			modifiedfull[i].append(sprep1411)
#		print("Start", "End", "1461", "1471", "1411")
#		for i in range(0, len(modifiedfull)):
#			print(modifiedfull[i])
		steps=range(0, len(modifiedfull))
		print("len modified full:\t", len(modifiedfull))
		for i in range(0, len(modifiedfull)):
			print(modifiedfull[i][0], modifiedfull[i][2])
		data1=[]
		data2=[]
		data3=[]
		for i in range(0, len(modifiedfull)):
			data1+=[modifiedfull[i][2]]
			data2+=[modifiedfull[i][3]]
			data3+=[modifiedfull[i][4]]

#		fig, ax1 = mpl.subplots()
		steps = range(0, len(modifiedfull))
		
#		color = 'tab:red'
#		ax1.set_xlabel('Synteze number, #')
#		ax1.set_ylabel('sprep1461', color=color)
#		ax1.plot(steps, data1, color=color)
#		ax1.tick_params(axis='y', labelcolor=color)
#		
#		ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
#		
#		color = 'tab:blue'
#		ax2.set_ylabel('sprep1471', color=color)  # we already handled the x-label with ax1
#		ax2.plot(steps, data2, color=color)
#		ax2.tick_params(axis='y', labelcolor=color)
#		
#		fig.tight_layout()  # otherwise the right y-label is slightly clipped
#		mpl.grid()
		
		# red dashes, blue squares and green triangles
		mpl.plot(steps, data1, 'r--', steps, data2, 'bs', steps, data3, 'g^')
		mpl.show()
#		print(modifiedfull[2])
#		print(modifiedfull)
#	else:

def main3(readfile, sheet):
#	a = readfile(MR201A102407, 7)
	a=pandas.read_csv(readfile, sheet)
	print(a.shape)
	print(a.columns)
	print(a.iloc[0])
	'''
	min-max temperature
	'''
#	print(a.iloc[:,0])
	g=a.iloc[:,4]
	updown=0
	iterprocess = 0
	uplist=[]
	downlist=[]
	for i in range(0, len(g)):
		if g[i]>50:
			if updown == 0:
				iterprocess+=1
#				print(iterprocess, i, g[i])
				uplist+=[i]
			updown = 1
#			print(i, g[i], sep="\t")
		else:
			if updown == 1:
				uplist+=[i]
			updown = 0
#	full=uplist + downlist
#	print(len(uplist), len(downlist), len(full))
#	sortedfull=sorted(full)
#	print(full)
#	print(sortedfull)
	'''
	periods
	'''
	modifiedfull=[]
	timelist=a.iloc[:,0]


#	print(uplist)
	for i in range(0, len(uplist), 2):
		if i>0:
			modifiedfull+=[[uplist[i-2], uplist[i-1]]]
#	print(modifiedfull)

#	for i in range(0, len(sortedfull)):
#		print(timelist[sortedfull[i]])
#	if full[0]==uplist[0]:
#		print("uplist")
#		for i in range(0, len(uplist), 2):
##			print(i)
#			if i>0:
#				modifiedfull+=[[uplist[i-2], uplist[i-1]]]
#		print("modifiedfull:", modifiedfull)
	prep1461=a.iloc[:,1]
	prep1471=a.iloc[:,2]
	prep1411=a.iloc[:,3]
		
	for i in range(0, len(modifiedfull)):
		sprep1461=0
		sprep1471=0
		sprep1411=0
		for i2 in range(modifiedfull[i][0], modifiedfull[i][1]):
			if i2>0:
				timedelta1=timelist[i2].timestamp()
				timedelta2=timelist[i2-1].timestamp()
				timedelta3=timedelta1-timedelta2
#					print(timedelta1, timedelta2)
				sprep1461+=(prep1461[i2]*timedelta3)
				sprep1471+=(prep1471[i2]*timedelta3)
				sprep1411+=(prep1411[i2]*timedelta3)
					
		if sprep1461<0.01:
			sprep1461=0
		else:
			sprep1461=sprep1461/3600
		if sprep1471<0.01:
			sprep1471=0
		else:
			sprep1471=sprep1471/3600
		if sprep1411<0.01:
			sprep1411=0
		else:
			sprep1411=sprep1411/3600
			
		modifiedfull[i].append(sprep1461)
		modifiedfull[i].append(sprep1471)
		modifiedfull[i].append(sprep1411)
#		print("Start", "End", "1461", "1471", "1411")
#		for i in range(0, len(modifiedfull)):
#			print(modifiedfull[i])
	steps=range(0, len(modifiedfull))
	print("len modified full:\t", len(modifiedfull))
	for i in range(0, len(modifiedfull)):
		print("Syntheze #", i, ":\t", timelist[modifiedfull[i][0]], modifiedfull[i][2])
	'''
	Data4 - Синтезы
	'''
	data1=[]
	data2=[]
	data3=[]
	data4 = []
	for i in range(0, len(modifiedfull)):
		data1+=[modifiedfull[i][2]]
		data2+=[modifiedfull[i][3]]
		data3+=[modifiedfull[i][4]]
#		data1+=[modifiedfull[i][2]/M_DDS]
#		data2+=[modifiedfull[i][3]/M_SiCl4]
#		data3+=[modifiedfull[i][4] / M_nBuLi/10]
	for i in range(0, len(modifiedfull)):
		if i!=5 and i!=18 and i!=21 and i!=22:
#		if i!=6 and i!=10 and i!=13 and i!=15 and i!=21 and i!=22:
			data4+=[0.32]
		else:
			data4+=[0.26]
		
#		mpl.plot(steps, data1, 'r--', steps, data2, 'bs', steps, data3, 'g^')

#		fig, ax1 = mpl.subplots()
	steps = range(0, len(modifiedfull))
		
#		color = 'tab:red'
#		ax1.set_xlabel('Synteze number, #')
#		ax1.set_ylabel('sprep1461', color=color)
#		ax1.plot(steps, data1, color=color)
#		ax1.tick_params(axis='y', labelcolor=color)
#		
#		ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
#		
#		color = 'tab:blue'
#		ax2.set_ylabel('sprep1471', color=color)  # we already handled the x-label with ax1
#		ax2.plot(steps, data2, color=color)
#		ax2.tick_params(axis='y', labelcolor=color)
#		
#		fig.tight_layout()  # otherwise the right y-label is slightly clipped
#		mpl.grid()
		
		# red dashes, blue squares and green triangles
	mpl.plot(steps, data1, 'r--', steps, data2, 'bs-', steps, data3, 'g^-', steps, data4, 'c^-')
	mpl.show()
#		mpl.savefig('myfig.png')
#		print(modifiedfull[2])
#		print(modifiedfull)
#		writingfile = open("newfile.txt", os.O_WRONLY)
##		print("asdfasdf", file=writingfile)
#		os.close(writingfile)
	def correl(text, d1, d2):
		g1=numpy.corrcoef(d1, d2)
		g2 = numpy.cov(d1, d2)
#		g2 = numpy.corrcoef(d2, d1)
		print(text, g1,g2, sep="\n")
	print("The Correlation:\n----> forward\tbackward")
	print("1\tn-BuLi X 0.1, mol")
	print("2\tSA-1, mol")
	print("3\tSA-2, mol")
	print("np\tNasypnaja Plotnostx")
	correl("1-2", data1, data2)
	correl("1-3", data1, data3)
	correl("1-np", data1, data4)
	correl("2-3", data2, data3)
	correl("2-np", data2, data4)
	correl("3-np", data3, data4)
	l1=[1,2,3]
	l2=[math.sin(1), math.sin(8), math.sin(27)]
	correl("l1-l2", l1, l2)
	return [modifiedfull, data1, data2, data3]

#sys.path+=['C:\\Users\Khatuntsevsv\Desktop\W\pythlibs\catboost-master\catboost\python-package']
#sys.path+=['C:\\Users\Khatuntsevsv\Desktop\W\pythlibs\catboost-master\catboost\python-package\catboost']
#C:\Users\Khatuntsevsv\Desktop\W\pythlibs\catboost-master\catboost\python-package
#sys.path+=['C:\\Users\Khatuntsevsv\Desktop\W\pythlibs\catboost-master\catboost\python-package']
#sys.path+=['C:\\Users\Khatuntsevsv\Desktop\W\pythlibs\catboost-master\catboost\python-package']
#from catboost import Pool, CatBoostRegressor
#from catboost import CatBoostRegressor
#from catboost import CatBoostRegressor
#import catboost
#import _catboost
#from catboost import CatBoostRegressor
def BuLi(f, vkv):
	'''
	vkv - столбец крана с н-БуЛи
	'''
	a=pandas.read_excel(f, "BuLi")
	print(a.shape)
	
	time=a.iloc[:, 0]
	raschod=a.iloc[:, 1]
	kv1=a.iloc[:, vkv]
	kv1time=[]
	kv1time_ar=[]
	
	sumrasch=0
	last = 0
	
	for i in range(0, a.shape[0]):
#		print(kv1[i])
		if last==0 and kv1[i]==1:
#			print(i, time[i], "Opened")
			last=1
			kv1time+=[i]
		elif last==1 and kv1[i]==0:
#			print(i, time[i] )
			last=0
			kv1time+=[i]
		
	for i in range(0, len(kv1time), 2):
		if i>0:
			kv1time_ar+=[[kv1time[i-2], kv1time[i-1]]]
#	print(len(kv1time_ar),kv1time_ar)
	
	print("step", "start_time","sum, gr","sum, mol" ,"input_all_time", "stream, gr/s",  sep="\t" )
	for i in range(0, len(kv1time_ar)):
		sumrasch = 0
		for i2 in range(kv1time_ar[i][0], (kv1time_ar[i][1]+1)):
			if i2!=kv1time_ar[i][1]:
				vtime=time[i2+1].timestamp() - time[i2].timestamp()
				sumrasch+=(vtime*raschod[i2+1])
		sumtime=time[kv1time_ar[i][1]].timestamp() - time[kv1time_ar[i][0]].timestamp()
		print(i, time[kv1time_ar[i][0]],sumrasch/3.6,sumrasch/(3.6*66) ,sumtime, sumrasch/(3.6*sumtime),  sep="\t" )
def BuLi2(f, vkv):
	'''
	vkv - столбец крана с н-БуЛи
	'''
	a=pandas.read_excel(f, "BuLi.0121")
	print(a.shape)
	
	time=a.iloc[:, 0]
	raschod=a.iloc[:, 1]
	kv1=a.iloc[:, vkv]
	kv1time=[]
	kv1time_ar=[]
	
	sumrasch=0
	last = 0
	
	for i in range(0, a.shape[0]):
#		print(kv1[i])
		if last==0 and kv1[i]==1:
#			print(i, time[i], "Opened")
			last=1
			kv1time+=[i]
		elif last==1 and kv1[i]==0:
#			print(i, time[i] )
			last=0
			kv1time+=[i]
		
	for i in range(0, len(kv1time), 2):
		if i>0:
			kv1time_ar+=[[kv1time[i-2], kv1time[i-1]]]
#	print(len(kv1time_ar),kv1time_ar)
	
	print("step", "start_time","sum, gr","sum, mol" ,"input_all_time", "stream, gr/s",  sep="\t" )
	for i in range(0, len(kv1time_ar)):
		sumrasch = 0
		for i2 in range(kv1time_ar[i][0], (kv1time_ar[i][1]+1)):
			if i2!=kv1time_ar[i][1]:
				vtime=time[i2+1].timestamp() - time[i2].timestamp()
				sumrasch+=(vtime*raschod[i2+1])
		sumtime=time[kv1time_ar[i][1]].timestamp() - time[kv1time_ar[i][0]].timestamp()
		print(i, time[kv1time_ar[i][0]],sumrasch/3.6,sumrasch/(3.6*66) ,sumtime, sumrasch/(3.6*sumtime),  sep="\t" )
def BuLi3(f, vkv, sh):
	'''
	vkv - столбец крана с н-БуЛи
	'''
	a=pandas.read_excel(f, sh)
	print(a.shape)
	
	time=a.iloc[:, 0]
	raschod=a.iloc[:, 1]
	kv1=a.iloc[:, vkv]
	kv1time=[]
	kv1time_ar=[]
	
	sumrasch=0
	last = 0
	
	for i in range(0, a.shape[0]):
#		print(kv1[i])
		if last==0 and kv1[i]==1:
#			print(i, time[i], "Opened")
			last=1
			kv1time+=[i]
		elif last==1 and kv1[i]==0:
#			print(i, time[i] )
			last=0
			kv1time+=[i]
		
	for i in range(0, len(kv1time), 2):
		if i>0:
			kv1time_ar+=[[kv1time[i-2], kv1time[i-1]]]
#	print(len(kv1time_ar),kv1time_ar)
	
	print("step", "start_time","sum, gr","sum, mol" ,"input_all_time", "stream, gr/s",  sep="\t" )
	for i in range(0, len(kv1time_ar)):
		sumrasch = 0
		for i2 in range(kv1time_ar[i][0], (kv1time_ar[i][1]+1)):
			if i2!=kv1time_ar[i][1]:
				vtime=time[i2+1].timestamp() - time[i2].timestamp()
				sumrasch+=(vtime*raschod[i2+1])
		sumtime=time[kv1time_ar[i][1]].timestamp() - time[kv1time_ar[i][0]].timestamp()
		print(i, time[kv1time_ar[i][0]],sumrasch/3.6,sumrasch/(3.6*66) ,sumtime, sumrasch/(3.6*sumtime),  sep="\t" )
		
def NP(f):
	'''
	vkv - столбец крана с н-БуЛи
	'''
	a=pandas.read_excel(f, 0)
	np_list=a.iloc[:, 15]
	time_list=a.iloc[:,0]
	print(a.shape)
	for i in range(0, a.shape[0]):
		if (i%10000)==0:
			print("\t\t\t", i)
		if np_list[i]<0.3:
			print(i+2, time_list[i], np_list[i], sep="\t\t")
	

def main4():
	print(103%50)

def BuLi_Parties(filename):
	'''
	Read file contained
	'''
	a=pandas.read_excel(f, 0)
	np_list=a.iloc[:, 15]
	time_list=a.iloc[:,0]
	

	
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
	g = []
	Styrol = a.iloc[:, 1]
	for i in range(0, len(Styrol)):
		if Styrol[i]=="Null":
			g+=[2]
		else:
			g+=[Styrol[i]]
			
	def get012list(l):
		g=[]
		for i in range(0, len(Styrol)):
			if Styrol[i]=="Null":
				g+=[2]
			else:
				g+=[Styrol[i]]
		return g
	
		
	
	BuLi = a.iloc[:, 4]
	gBuli = get012list(BuLi)
#	for i in range(0, len(BuLi)):
#		if BuLi[i]=="Null":
#			BuLi[i]=2
#	
	SA1 = a.iloc[:, 7]
	gSA1 = get012list(SA1)
#	for i in range(0, len(SA1)):
#		if SA1[i]=="Null":
#			SA1[i]=2
#	
	Buta = a.iloc[:, 10]
	gButa = get012list(Buta)
#	for i in range(0, len(Buta)):
#		if Buta[i]=="Null":
#			Buta[i]=2
#	



	print("Lists are loaded")
	
	def detect(aStyrol, aBuLi, aSA1, aButa, aTP):
		trig = -1
		styrol_cycle=[]
		def detect_01_10(alist):
			time_alist=[]
			alist_cycle=[]
			trig=-1
			for i in range(1, len(alist)):
				if alist[i-1]==1 and alist[i]==0:
					alist_cycle=[i]
					time_alist+=[[i-1,i, (aTP[i].timestamp()-aTP[i-1].timestamp())/60]]
			return time_alist
		def detect_01_10_ver1(alist):
			time_alist=[]
			alist_cycle=[]
			time_cycle=[]
			trig=-1
			sum1=0
			for i in range(1, len(alist)):
				if trig==-1:
					if alist[i-1]==0 and alist[i]==1:
#						print("Up", i)
						trig = 2
						alist_cycle+=[i]
						sum1+=1
				else:
					if trig==2 and alist[i]==0 and alist[1]==1:
#						print("Down", i)
						alist_cycle+=[i]
						time_alist+=[alist_cycle]
						alist_cycle=[]
						trig=-1
			for i in range(1, len(time_alist)):
				time_cycle+=[[time_alist[i-1][0], time_alist[i][0]]]
			print(sum1, time_cycle)
			return time_cycle
		
		print("\n\ndetect_01_10_ver1")
#		print(detect_01_10_ver1(aStyrol))
		
		time_Styrol = detect_01_10(aStyrol)
#		time_Styrol = detect_01_10_ver1(aStyrol)
#		print(time_Styrol)
		time_BuLi = detect_01_10_ver1(aBuLi)
		time_SA1 = detect_01_10(aSA1)
		time_Buta = detect_01_10(aButa)
		
		print("\n\ndetect_01_10_ver1")
		print("Styrol:\n", time_Styrol)
		print("SA1:\n", time_SA1)
		print("BuLi:\n", time_BuLi)
		print("C4H10:\n", time_Buta)
		
#	detect(Styrol, BuLi, SA1, Buta, time_process)
#	detect(a.iloc[:, 2], a.iloc[:, 5], a.iloc[:, 8], a.iloc[:, 11], a.iloc[:, 0])
#	indexcol=3
#	detect(a.iloc[:, indexcol], a.iloc[:, indexcol+3*1], a.iloc[:, indexcol+3*2], a.iloc[:, indexcol+3*3], a.iloc[:, 0])
	

def runprogram():
	run = 11
	if run ==1:
		main()
	elif run ==2:
		main2()
	elif run ==3:
		k = main3(MR201A101305, "1013_05")
	elif run ==4:
		main4()
	elif run ==5:
		BuLi(fBuLi, 3)
		BuLi(fBuLi, 7)
		BuLi(fBuLi, 9)
	elif run==6:
		NP(fNP)
	elif run ==7:
		BuLi2(fBuLi_2, 3)
		BuLi2(fBuLi_2, 5)
		BuLi2(fBuLi_2, 7)
	elif run==8:
		BuLi3(fBuLi_3, 3, "BuLi.0321")
		BuLi3(fBuLi_3, 5, "BuLi.0321")
		BuLi3(fBuLi_3, 7, "BuLi.0321")
	elif run==9:
		readfile = fBuLi_4
		BuLi3(readfile, 3, "BuLi.0221")
		BuLi3(readfile, 5, "BuLi.0221")
		BuLi3(readfile, 7, "BuLi.0221")
	elif run==10:
		readfile = fparties
		BuLi_Parties(readfile)
	elif run==11:
		readfile = fKV
		KV(readfile, 10)

	
		

#getmin2(temp1)
#datas()
runprogram()


