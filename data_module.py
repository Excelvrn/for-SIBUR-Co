# python module
# analyse

import datetime
import pandas
import decimal
import statsmodels
import numpy
import all_files
import os


# del Null columns
v_dropna = 1
Kelvin = 273.16
kg_per_h_to_g_per_s = 3.6
kg = 1000.0
reactionstimelimit = 7200.0
reactionstimelimitn = 12
#includes time interval
reactionshightimelimit = 5400.0
reactionslowtimelimit = 0

def get_null(dataframe):
	ncols = dataframe.shape[1]
	if ncols>1:
		for i in range(0, ncols):
			c = dataframe.iloc[:,i]
			print("type of returned", type(c))

def printd(text, l):
	if len(l)>=1:
		print(text, type(l[0]), l[0], sep="\t")
	else:
		print(text, type(l), "length equ 0")

'''
def dates():
	d = datetime.date(2021, 8, 18)
	d-= datetime.timedelta(days=7)
	if d.isoweekday()>1:
		d-= datetime.timedelta(days=d.weekday())
	print("date:\t", d, d.isoweekday())
	
	return first day of one week ago
'''
def dates(date_d):
	date_d-= datetime.timedelta(days=7)
	if date_d.isoweekday()>1:
		date_d-= datetime.timedelta(days=date_d.weekday())
	print("date:\t", date_d, date_d.isoweekday())
	
def PR():
	print("hello! Module run")

def time_temp_pressure(pandas_datas, time_col, temp_col, pressure_col):
	time_data=pandas_datas.iloc[:, time_col]
	temp_data=pandas_datas.iloc[:, temp_col]
	pressure_data=pandas_datas.iloc[:, pressure_col]
	# print("Time.shape:\n\t",  time_data.shape)
	
	# for i in range(0, len(time_data)):
		# if time_data.isnull() or time_data.notna():
			# print(i, time_data[i])
	return time_data, temp_data, pressure_data
	
#masses of reagents for a period
def raschod(pandas_datas, time_col, kv, raschod):
	time_data=pandas_datas.iloc[:, time_col]
	kv_data=pandas_datas.iloc[:, kv]
	raschod_data=pandas_datas.iloc[:, raschod]

	
	kv_data_i = []
	kv_data_i_buf=[]
	for i in range(1, len(kv_data)):
		if kv_data[i]==1 and kv_data[i-1]==0:
			kv_data_i_buf+=[i]
		elif kv_data[i]==0 and kv_data[i-1]==1:
			kv_data_i_buf+=[i]
			kv_data_i+=[kv_data_i_buf]
			kv_data_i_buf=[]
	#print("-=-=-\tkv_data_i\n", kv_data_i)
	
	raschod_list = []
	for i in kv_data_i:
		if len(i)>1:
			raschod_list_i=0
			for i2 in range(i[0], i[1]+1):
				time_delta = time_data[i2+1].timestamp() - time_data[i2].timestamp()
				#print(i, time_delta)
				raschod_list_i += time_delta*raschod_data[i2]/kg_per_h_to_g_per_s/kg
			raschod_list+=[raschod_list_i]
			i.append(raschod_list_i)
			
			#print("KV:\n", i, raschod_list_i)
	#print("rashod_kv:\n", kv_data_i)
	return kv_data_i
'''
Get function "Temperature-time" or "Pressure-time" for all time
'''
def lin_temp(pandas_datas, time_col, Temperature_col):
	time_list=[]
	temperature_list=[]
	
	time_data=pandas_datas.iloc[:, time_col]
	Temperature_data=pandas_datas.iloc[:, Temperature_col]
	
	start_time=time_data[0].timestamp()
	last_time=time_data[pandas_datas.shape[0] - 1].timestamp()
	dls =  last_time - start_time
	
	time_list = range(0, int(dls))
	
	temp_buf = 0
	
	#print(start_time, last_time, int(dls))
	index=0
	for i in range(1, len(time_data)):
		for i2 in range(int(time_data[i-1].timestamp()),int(time_data[i].timestamp())):
			index+=1
			temperature_list+=[Temperature_data[i-1]]
	#print(len(time_list),len(temperature_list))
	
	return time_list, temperature_list
'''
Get cycle periods
'''	
def getraschodintocycle(raschod_list):
	l=[]
	len_raschod_list = len(raschod_list)
	if len_raschod_list>1:
		for i in range(1, len_raschod_list):
			g=[raschod_list[i-1][0], raschod_list[i][0]]
			l+=[g]
	return l
'''
GRICL - getraschodintocycle_list
RL - raschod_list
'''
def GetReagentsOfSyntheze(GRICL, RL):
	retlist = []
	for i in GRICL:
		sum = 0
		for i2 in RL:
			if (i2[0]<=i[1] and i2[0]>=i[0]) and (i2[1]<=i[1] and i2[1]>=i[0]):
				sum += i2[2]
		retlist+=[[i[0], i[1], sum]]
	return retlist
'''
GRICL - getraschodintocycle_list
RL - raschod_list
TL - time-list
'''
def GetReagentsOfSyntheze2(GRICL, RL, TL):
	decimal.getcontext().prec = 2
	retlist = []
	start_time = TL[0].timestamp()
	for i in GRICL:
		sum = 0
		for i2 in RL:
			if (i2[0]<=i[1] and i2[0]>=i[0]) and (i2[1]<=i[1] and i2[1]>=i[0]):
				sum += i2[2]
		retlist+=[[TL[i[0]].timestamp() -start_time , TL[i[1]].timestamp() -start_time, sum]]
	return retlist
	
	
'''
*** Covar 
'''
def ser_list(ser):
	lll=[]
	if len(lll)>0:
		for i in ser:
			lll+=[i]
	return lll


def cover(dataframe, setcols):
	
	gl = []
	for i in setcols:
		dgl=dataframe.iloc[:, i]
		gl+=[dgl]
	print("gl len:\t", len(gl))
	
	array_out=[]
	
	ans=[]
	
	lengl = len(gl)
	kgl= lengl**2
	
	k0 = 0
	
	
	for i in setcols:
		array_in=[]
		
		for i2 in setcols:
			
			k0=k0+1
			
			print("Step", k0, "/", kgl, "\t")
#			if i!=i2:
			if i<lengl and i2<lengl:
				try: 
					k = gl[i].corr(gl[i2])
				except (AttributeError, TypeError,IndexError) as ATE:
					if i<lengl:
						print(i, i2, ATE,type(gl[i][0]), type(gl[i2][0]))
					else:
						print(i, i2)
					array_in+=[' --- ']
	#				break
				else:
					array_in+=[k]
					if abs(k)>=0.5:
						ans+=[[gl[i-1], gl[i2-1], k]]
	#					ans+=[[g.columns[cols[i]],cols[i], g.columns[cols[i2]], cols[i2],k]]
			else:
				array_in+=["not range"]
		array_out+=[array_in]

	return array_out

def covar_excel(inputfile, sh,writtenexcelfile):
	
#	output=
#	nmpyd = numpy.correlate([1,2,3,4], [1,2,4, 100])
#	print( nmpyd)
	g = pandas.read_excel(inputfile, sh)
	print(g.shape)
#	print("Columns:\t", g.columns)
	

#	print("Excepts:\t", except1, except2)
#	for i in g.columns:
#		print("E:\t",i, i.count(except1))
	exceptes = []
	for i in g.columns:
		if i.count('ww')>0:
			exceptes+=[i]
		elif i.count('ата')>0:
			exceptes+=[i]
	print("Exceptes:\t",exceptes)
	
	cols = []
	for i in range(0, len(g.columns)):
		if g.columns[i]!=exceptes[0] and g.columns[i]!=exceptes[1]:
			cols+=[i]
			print("EXC:",i)
	print(cols)
	
#	g.corr(method='pearson')
	gl=[]
#	for i in range(1, g.shape[1]):
#		gl+=[g.iloc[:, i]]
	for i in cols:
		gl+=[g.iloc[:, i]]
	
#	print(statsmodels.stats.weightstats.DescrStatsW(gl[0], gl[1]))
#	for i in ranges:
#		for i2 in ranges:
#			print(i, i2, , sep="\t")
#	внешний и внутрениий массивы для последующей записи в файл
	array_out=[]
	
	ans=[]
	
	kgl= len(gl)**2
	
	k0 = 0
	
	for i in range(0, len(gl)):
		for i2 in range(i, len(gl)):
			
			k0=k0+1
			
			print("Step", k0, "/", kgl)
			array_in=[]
#			if i!=i2:
			try:
				k = gl[i].corr(gl[i2])
			except (AttributeError, TypeError) as ATE:
				print(i, i2, ATE)
				array_in+=[' --- ']
#				break
			else:
				array_in+=[k]
				if abs(k)>=0.5:
					ans+=[[g.columns[cols[i]], g.columns[cols[i2]], k]]
#					ans+=[[g.columns[cols[i]],cols[i], g.columns[cols[i2]], cols[i2],k]]
		array_out+=[array_in]
	for i in ans:
		print(i[0], i[1], i[2], sep="\t")
	ansl1 = []
	ansl2 = []
	for i in ans:
		ansl1+=[i[0]]
		ansl2+=[i[1]]
	setansl1=set(ansl1)
	setansl2=set(ansl2)
	for i in setansl1:
		print("set 1:\t", i)
	for i in setansl2:
		print("set 2:\t", i)
	setansl3 = setansl1.union(setansl2)
	for i in setansl3:
		print("setans3:\t\t", i)
		
	gpd = pandas.DataFrame(array_out)
	gpd.to_excel(writtenexcelfile, sheet_name='startsheet')
def covar_excel2(inputfile, sh,writtenexcelfile):
	
#	output=
#	nmpyd = numpy.correlate([1,2,3,4], [1,2,4, 100])
#	print( nmpyd)
	g = pandas.read_excel(inputfile, sh)
	print('g.shape[3:5]', type(g.columns), g.shape[3:5])
	gcol = g.columns
	
#	g.corr(method='pearson')
	gl=[]
#	for i in range(1, g.shape[1]):
#		gl+=[g.iloc[:, i]]
	for i in range(1, len(g.columns)):
		gl+=[g.iloc[:, i]]
		
	
	
#	print(statsmodels.stats.weightstats.DescrStatsW(gl[0], gl[1]))
#	for i in ranges:
#		for i2 in ranges:
#			print(i, i2, , sep="\t")
#	внешний и внутрениий массивы для последующей записи в файл
	array_out=[]
	
	ans=[]
	
	lengl = len(gl)
	kgl= lengl**2
	
	k0 = 0
	
	
	for i in range(0, lengl):
		array_in=[]
		
		for i2 in range(0, lengl):
			
			k0=k0+1
			
			print("Step", k0, "/", kgl, "\t")
#			if i!=i2:
			try:
				k = gl[i].corr(gl[i2])
			except (AttributeError, TypeError) as ATE:
				print(i, i2, ATE,type(gl[i][0]), type(gl[i2][0]))
				array_in+=[' --- ']
#				break
			else:
				array_in+=[k]
				if abs(k)>=0.5:
					ans+=[[g.columns[i], g.columns[i2], k]]
#					ans+=[[g.columns[cols[i]],cols[i], g.columns[cols[i2]], cols[i2],k]]
		array_out+=[array_in]
#	for i in ans:
#		print(i[0], i[1], i[2], sep="\t")
#	ansl1 = []
#	ansl2 = []
#	for i in ans:
#		ansl1+=[i[0]]
#		ansl2+=[i[1]]
#	setansl1=set(ansl1)
#	setansl2=set(ansl2)
#	for i in setansl1:
#		print("set 1:\t", i)
#	for i in setansl2:
#		print("set 2:\t", i)
#	setansl3 = setansl1.union(setansl2)
#	for i in setansl3:
#		print("setans3:\t\t", i)
		
	gpd = pandas.DataFrame(array_out)
	gpd.to_excel(writtenexcelfile, sheet_name='startsheet')
#	gpd.to_excel(writtenexcelfile, sheet_name='startsheet', index=g.columns, columns=g.columns)
def covar_excel3(inputfile1, sh1,inputfile2, sh2, writtenexcelfile):

	g1 = pandas.read_excel(inputfile1, sh1)
	gcol1 = g1.columns
	
	g2 = pandas.read_excel(inputfile2, sh2)
	gcol2 = g2.columns
	
#	print(type(gcol2), type(gcol2[0]))
	sl1 = ser_list(gcol1)
	setg1 = set(sl1)
	
	sl2 = ser_list(gcol2)
	setg2 = set(sl2)
	
	for i in setg1:
		print("s1:\t", i, len(setg1))
	for i in setg2:
		print("s2:\t", i, len(setg2))
	setint = setg1.intersection(setg2)
	for i in setint:
		print("setint:\t", i, len(setint))
	
	ggcol1=[]
	ggcol2=[]
	for i in setint:
		for i2 in range(0, len(gcol1)):
			if i==gcol1[i2]:
				ggcol1+=[i2]
		for i2 in range(0, len(gcol2)):
			if i==gcol2[i2]:
				ggcol2+=[i2]
	print(ggcol1)
	print(ggcol2)
	
	gc1 = cover(g1, ggcol1)
	gc2 = cover(g2, ggcol2)
	gc03 = []
	gc13 = []
	
	for i in range(0, len(gc1)):
		gc13 = []
		for i2 in range(0, len(gc1[i])):
			if type(gc1[i][i2])!=str or type(gc2[i][i2])!=str:
				gc13+=[gc1[i][i2] - gc2[i][i2]]
			else:
				gc13+=["---"]
		gc03+=[gc13]
		
	gpd = pandas.DataFrame(gc03)
	gpd.to_excel(writtenexcelfile, sheet_name='startsheet')

'''
Report http://s103as-mes-rs.sibur.local/SSRSServer/Pages/ReportViewer.aspx?%2fLIMS+Reports%2f%d0%9f%d1%80%d0%be%d0%b8%d0%b7%d0%b2%d0%be%d0%b4%d1%81%d1%82%d0%b2%d0%be+%d1%82%d0%b5%d1%80%d0%bc%d0%be%d1%8d%d0%bb%d0%b0%d1%81%d1%82%d0%be%d0%bf%d0%bb%d0%b0%d1%81%d1%82%d0%be%d0%b2%2f%d0%93%d0%be%d1%82%d0%be%d0%b2%d0%b0%d1%8f+%d0%bf%d1%80%d0%be%d0%b4%d1%83%d0%ba%d1%86%d0%b8%d1%8f+%d0%a2%d0%ad%d0%9f+(%d0%b4%d0%bb%d1%8f+%d0%bf%d1%80%d0%be%d0%b8%d0%b7%d0%b2%d0%be%d0%b4%d1%81%d1%82%d0%b2%d0%b0)&rs:Command=Render
'''
def getnaspl(inputfile1, sh1, timecol, datacol ):
	
	print("getnaspl")
	
	g1 = pandas.read_excel(inputfile1, sh1)
	g1rows, g1cols = g1.shape
	print("\t*** getnaspl shape, rows, columns:\n\t", g1.shape, g1rows, g1cols, g1.columns)
	
	timecold = g1.iloc[:, timecol]
	datacold = g1.iloc[:, datacol]
	print("len(datacold):\t", len(datacold), datacold[0], sep="\n\t")
	
	datacoldl = []
	timecoldl = []
	dc = []
	
	for i in range(0, len(datacold)):
		if numpy.isnan(datacold[i])==False:
#			print(datacold[i], type(datacold[i]))
			datacoldl+=[datacold[i]]
			timecoldl+=[timecold[i]]
			dc+=[[timecold[i], datacold[i]]]
			print(datacoldl[len(datacoldl)-1], timecoldl[len(datacoldl)-1])
#	df = pandas.DataFrame(data = [[timecoldl, datacoldl]])
	df = pandas.DataFrame(data = dc)
	print("df-type:\t", type(df))
	
	df.to_excel("C:/Users/Khatuntsevsv/Desktop/W/Datas/temp.0.xlsx")
#	df.ExcelWriter("C:/Users/Khatuntsevsv/Desktop/W/Datas/record.0.xlsx")
	return df
	
#	getnaspl ver. 1.0
def getnaspl_1_0(inputfile1, sh1, timecol, datacol ):
	
	print("getnaspl_1_0")
	
	g1 = pandas.read_excel(inputfile1, sh1)
	g1rows, g1cols = g1.shape
	print("\t*** getnaspl rows, columns:\n\t", g1rows, g1cols, g1.columns)
	
	timecold = g1.iloc[:, timecol]
	print("Type of timecold is\t", type(timecold))
	datacold = g1.iloc[:, datacol]
#	for i in datacold:
#		print("\tdatacold:\t", i)
#	print("len(datacold):\t", len(datacold), datacold[0], sep="\n\t")
	printd("datacold", datacold)
	
	datacoldl = []
	timecoldl = []
	dc = []
#	print("len(datacold):\n\t\t", len(datacold))
	for i in range(0, len(datacold)):
#		if numpy.isnan(datacold[i])==False:
#		type(datacold[i])==float or 
		if numpy.isnan(datacold[i])==False:
#		if type(datacold[i])==float and datacold[i]>0.1 and datacold[i]<1 :
#			print(datacold[i], type(datacold[i]))
			datacoldl+=[datacold[i]]
			timecoldl+=[timecold[i]]
			dc+=[[timecold[i], datacold[i]]]
			print(datacoldl[len(datacoldl)-1], timecoldl[len(datacoldl)-1])
	print("\tlen(datacoldl):\t",len(datacoldl))
#	df = pandas.DataFrame(data = [[timecoldl, datacoldl]])
	df = pandas.DataFrame(data = dc, columns=["Date", "NP"])
	df.to_excel(all_files.exp_4)
	print("df-type:\t", type(df))
	return df
def getnasplins(inputfile1 ):
	
	timerdd_datetime = 0

	naspldatas = pandas.read_excel(inputfile1, 'Sheet1')
	recordsdatas = pandas.read_excel(inputfile1, 4)

	print(recordsdatas.shape)
	
	#times in records
	timerdd = recordsdatas.iloc[:,timerdd_datetime]
	
	npd = naspldatas.iloc[:, 2]
	#хранение строк, даты которых совпадают с датами в наборе данных
	npd_rows = []
	#times in nas.pl
	timenpd = naspldatas.iloc[:, 1]
	
	time_min =[]
#	for i in timerdd:
#		saved_time=[]
#		for i2 in timenpd:
#			d = i.timestamp() - i2.timestamp()
#			if abs(d)<=300*6:
#				saved_time+=[timerdd[i], timenpd[i2]]
#		time_min+=[saved_time]
	changediter= 0
	
	for i in range(0, len(timerdd)):
		saved_time=[]
		
		for i2 in range(changediter, len(timenpd)):
			d = timerdd[i].timestamp() - timenpd[i2].timestamp()
			if abs(d)<=4500.0:
				print(i, i2, d)
				saved_time=[i, i2, d,timerdd[i], timenpd[i2]]
				time_min+=[saved_time]
				changediter = i2+1
				if i2>5:
					for i3 in range(0, 5):
						npd_rows+=[[i2, i-i3]]
#		if len(saved_time):
#		time_min+=[[i2, il]]

	'''
	data`s forming
	'''
	
	datasm = []
	
	for i in npd_rows:
		print(i)
		line = recordsdatas.iloc[i[1], :]
		datasm2 = []
		for i2 in line:
			datasm2+=[i2]
		datasm2+=[npd[i[0]]]
		datasm+=[datasm2]
	
	#	rdd = recordsdatas.iloc[:, :]
#	da = pandas.concat(time_min, axis=1)

	try:
		k = os.unlink("C:/Users/Khatuntsevsv/Desktop/W/Datas/save.0.xlsx")
	except:
		print("Except os.unlink(\"C:/Users/Khatuntsevsv/Desktop/W/Datas/save.0.xlsx\")")
	else:
		print("Deleted file")
		
	
#	da = pandas.DataFrame(data=time_min)
	da = pandas.DataFrame(data=datasm)
#	da.dropna(how='any')
	print("shape:\t", da.shape, len(time_min))
	da.to_excel("C:/Users/Khatuntsevsv/Desktop/W/Datas/save.0.xlsx")
	
# correlation
	cordatalists = []
	for i in range(1, (da.shape[1]-2)):
		cordatalists+=[ser_list(da.iloc[:, i])]
	correlnpd = ser_list( da.iloc[:, (da.shape[1]-1)])
	
	
#	for i in cordatalists:
#		try:
#			k = i.corr(correlnpd)
#		except (AttributeError, TypeError) as ATE:
#			print(' --- ', type(i), type(correlnpd), type(i[0]), type(correlnpd[0]))
#		else:
#			print(k)
#	da.dropna(how='any')
	try:
		k = da.corr()
	except (AttributeError, TypeError) as ATE:
		print(' --- ', type(i), type(correlnpd), type(i[0]), type(correlnpd[0]))
	else:
		print(k)
	
	corframe = pandas.DataFrame(k)
	
	corframe.to_excel("C:/Users/Khatuntsevsv/Desktop/W/Datas/save.1.xlsx")
	


'''
getnasplins2
'''
def getnasplins2(naspldatas, recordsdatas, savedfile, savedfile2):

#	naspldatas = pandas.read_excel(inputfile1, 'Sheet1')
#	recordsdatas = pandas.read_excel(inputfile1, 4)

	print("\tnaspldatas.shape:\n\t", naspldatas.shape)
	print("\trecordsdatas.shape:\n\t", recordsdatas.shape)
	
	#times in records
	print("\ttimerdd")
	timerdd = recordsdatas.iloc[:,0]
	
	print("\ttimenpd")
#	npdout = naspldatas.iloc[0, :]
#	print(naspldatas.shape)
#	for i in npdout:
#		print(i)
	timenpd = naspldatas.iloc[:, 0]
#	timenpd = naspldatas[naspldatas.columns[0]]
	
	print("\tnpd")
	npd = naspldatas.iloc[:, 1]
#	npd = naspldatas[naspldatas.columns[15]]
	print("\tnpd is got")
	#хранение строк, даты которых совпадают с датами в наборе данных
	npd_rows = []
	#times in nas.pl
	
	time_min =[]
#	for i in timerdd:
#		saved_time=[]
#		for i2 in timenpd:
#			d = i.timestamp() - i2.timestamp()
#			if abs(d)<=300*6:
#				saved_time+=[timerdd[i], timenpd[i2]]
#		time_min+=[saved_time]
	changediter= 0
	
	for i in range(0, len(timerdd)):
		saved_time=[]
		
		for i2 in range(changediter, len(timenpd)):
			d = timerdd[i].timestamp() - timenpd[i2].timestamp()
			if abs(d)<=4500.0:
				print(i, i2, d)
				saved_time=[i, i2, d,timerdd[i], timenpd[i2]]
				time_min+=[saved_time]
				changediter = i2+1
				if i2>5:
					for i3 in range(0, 5):
						npd_rows+=[[i2, i-i3]]
#		if len(saved_time):
#		time_min+=[[i2, il]]

	'''
	data`s forming
	'''
	
	datasm = []
	
	for i in npd_rows:
		print(i)
		line = recordsdatas.iloc[i[1], :]
		datasm2 = []
		for i2 in line:
			datasm2+=[i2]
		datasm2+=[npd[i[0]]]
		datasm+=[datasm2]
	
	#	rdd = recordsdatas.iloc[:, :]
#	da = pandas.concat(time_min, axis=1)

	try:
		k = os.unlink(savedfile)
	except:
		print("Except os.unlink(\"C:/Users/Khatuntsevsv/Desktop/W/Datas/save.0.xlsx\")")
	else:
		print("Deleted file")
		
	
#	da = pandas.DataFrame(data=time_min)
	da = pandas.DataFrame(data=datasm)
#	da.dropna(how='any')
	print("***\tda.shape:\t", da.shape, len(time_min), da.columns)
	da.to_excel(savedfile)
	
# correlation
	cordatalists = []
	for i in range(1, (da.shape[1]-2)):
		cordatalists+=[ser_list(da.iloc[:, i])]
	correlnpd = ser_list( da.iloc[:, (da.shape[1]-1)])
	
	
#	for i in cordatalists:
#		try:
#			k = i.corr(correlnpd)
#		except (AttributeError, TypeError) as ATE:
#			print(' --- ', type(i), type(correlnpd), type(i[0]), type(correlnpd[0]))
#		else:
#			print(k)
#	da.dropna(how='any')
	try:
		k = da.corr()
	except (AttributeError, TypeError) as ATE:
		print(' --- ', type(i), type(correlnpd), type(i[0]), type(correlnpd[0]))
	else:
		print(k)
	
	corframe = pandas.DataFrame(k)
	
	corframe.to_excel(savedfile2)
'''
****  ****  ****  ****  ****  ****  ****  ****  ****  
  ****  ****  ****  ****  ****  ****  ****  ****
  Михаил Иванович, Ваш случай - теоретикоигровой случай.
Пример игры. при отстутствии сведений о стратегии противника. 
Допустим, мы с Вами играем, угадывая количество пальцев на руке соперника. Всего можно показать либо 1, либо 2 пальца. Если Вы Вы угадываете количество пальцев, показанное мной, то получаете 3 рубля. Если я угадываю 1 палец, то Вы - мне 2 рубля, а если 2 пальца, то 4 рубля.
Какие условия выгодны: у меня или у Вас?

**  ****  ****  ****  ****  ****  ****  ****  ****        
'''
def getnasplins3(naspldatas, recordsdatas, savedfile, savedfile2):

	
	timerdd_datetime = 0
	
	print("\tnaspldatas.shape:\n\t", naspldatas.shape)
	print("\trecordsdatas.shape:\n\t", recordsdatas.shape)
	if v_dropna==1:
		print("\trecordsdatas shape:\t", recordsdatas.shape)
		recordsdatas.dropna(axis=1)
		print("\trecordsdatas shape after dropna:\t", recordsdatas.shape)
		get_null(recordsdatas)
	
	
	#times in records
#	print("\ttimerdd")
	timerdd = recordsdatas.iloc[:,timerdd_datetime]
#	print("timerdd[0]:\t", timerdd[0])
	
#	***
	g = recordsdatas.iloc[0,:]
#	print("g.ndim, g.shape an output recordsdatas.iloc[0,:]")
#	for i in range(0, len(g)):
#		print(i, g.iat[i])
	
	
	timerddl = timerdd.to_list()
	
	#columns` labels
	rddcols = recordsdatas.columns
	rddcolsl = rddcols.to_list()
#	rddcolsl+=["NP"]
	
#	print(timerddl[0])
	
#	print("\ttimenpd")
#	npdout = naspldatas.iloc[0, :]
#	print(naspldatas.shape)
#	for i in npdout:
#		print(i)
	timenpd = naspldatas.iloc[:, 0]
	timenpdl = timenpd.to_list()
	
#	print("timenpdl:\t", timenpdl[0])
#	timenpd = naspldatas[naspldatas.columns[0]]
	
#	print("\tnpd")
	npd = naspldatas.iloc[:, 1]
#	npdl = npd
#	npd = naspldatas[naspldatas.columns[15]]
#	print("\tnpd is got")
	
	#хранение строк, даты которых совпадают с датами в наборе данных
	npd_rows = []
	#times in nas.pl
	
	time_min =[]
#	for i in timerdd:
#		saved_time=[]
#		for i2 in timenpd:
#			d = i.timestamp() - i2.timestamp()
#			if abs(d)<=300*6:
#				saved_time+=[timerdd[i], timenpd[i2]]
#		time_min+=[saved_time]
	changediter= 0
	
	#if timerdd[i]==bool look for timerdd
	
#	print("start cycle 4 500 s")
#	print("len(timerdd),len(timenpd):", len(timerdd),len(timenpd)) 
	for i in range(0, len(timerdd)):
		saved_time=[]
		for i2 in range(changediter, len(timenpdl)):
#			print("timerdd[i], timenpd[i2]:\t", type(timerdd[i]), type(timenpd[i2]), sep = "\t\n")
#			d = timerdd[i].timestamp() - timenpd[i2].timestamp()
#			print(timerdd[i], " - ", timenpd[i2])
			try:
				d =  timenpdl[i2].timestamp() - timerdd[i].timestamp()
			except:
				print("Except d=...", i, i2)
#				d_ex = datetime.datetime(timerdd[i])
#				print(type(d_ex), d_ex.timestamp())
				break
			else:
				if d<=reactionshightimelimit and d>=reactionslowtimelimit:
					print(i, i2, d)
					saved_time=[i, i2, d,timerdd[i], timenpd[i2]]
					time_min+=[saved_time]
#					changediter = i2+1
					if i2>5:
						for i3 in range(0, reactionstimelimitn):
							npd_rows+=[[i2, i-i3]]
#	print("\tnpd_rows is:\t", npd_rows)
			
#	print("end cycle 4 500 s")
#		if len(saved_time):
#		time_min+=[[i2, il]]
	
	'''
	data`s forming
	'''
	
	datasm = []
	
#	print("len(npd_rows)", len(npd_rows))
#	for i in npd_rows:
#		print("npd_rows:\t", i)

	for i in npd_rows:
		print(i)
		line = recordsdatas.iloc[i[1], :]
		datasm2 = []
		for i2 in line:
			datasm2+=[i2]
		datasm2+=[npd[i[0]]]
		datasm+=[datasm2]
	
	#	rdd = recordsdatas.iloc[:, :]
#	da = pandas.concat(time_min, axis=1)

	try:
		k = os.unlink(savedfile)
	except:
		print("Except os.unlink\t", savedfile)
	else:
		print("Deleted file\t", savedfile)
		
	
#	da = pandas.DataFrame(data=time_min)
	da = pandas.DataFrame(data=datasm)
#	da.dropna(how='any')
	print("***\tda.shape:\t", da.shape, len(time_min), da.columns)
	print("da is\t", da.shape, "rddcolsl is\t", len(rddcolsl))
#	da.to_excel(savedfile, header=rddcolsl)
	da_size_col = da.columns
	da.drop_duplicates(subset=da_size_col)
	da.to_excel(savedfile)
	
# correlation
	cordatalists = []
	for i in range(1, (da.shape[1]-2)):
		cordatalists+=[ser_list(da.iloc[:, i])]
	print("da.shape:\t", da.shape)
	correlnpd = ser_list( da.iloc[:, (da.shape[1]-1)])
	
	
#	for i in cordatalists:
#		try:
#			k = i.corr(correlnpd)
#		except (AttributeError, TypeError) as ATE:
#			print(' --- ', type(i), type(correlnpd), type(i[0]), type(correlnpd[0]))
#		else:
#			print(k)
#	da.dropna(how='any')
	try:
		k = da.corr()
	except (AttributeError, TypeError) as ATE:
		print(' --- ', type(i), type(correlnpd), type(i[0]), type(correlnpd[0]))
	else:
		print(k)
	
	corframe = pandas.DataFrame(k)
	
	corframe.to_excel(savedfile2)
#	corframe.to_excel(savedfile2, header=rddcolsl)
	
	

def getnasplins_debug( ):

#	naspldatas = pandas.read_excel(inputfile1, 'Sheet1')
#	recordsdatas = pandas.read_excel(inputfile1, 4)
#	#times in records
#	timerdd = recordsdatas.iloc[:,0]
#	
#	npd = naspldatas.iloc[:, 2]
#	#times in nas.pl
#	timenpd = naspldatas.iloc[:, 1]
	
	time_min =[[1,1], [3,3]]
	time_min =[[1,3], [1,3]]
#	for i in timerdd:
#		saved_time=[]
#		for i2 in timenpd:
#			d = i.timestamp() - i2.timestamp()
#			if abs(d)<=300*6:
#				saved_time+=[timerdd[i], timenpd[i2]]
#		time_min+=[saved_time]
		
#	for i in range(0, len(timerdd)):
#		saved_time=[]
#		for i2 in range(0, len(timenpd)):
#			d = timerdd[i].timestamp() - timenpd[i2].timestamp()
#			if abs(d)<=1800:
#				print(i, i2, d)
#				saved_time+=[[i, i2]]
#		time_min+=[saved_time]
	
#	rdd = recordsdatas.iloc[:, :]
#	da = pandas.concat(time_min, axis=1)
	da = pandas.DataFrame(data=time_min)
	try:
		k = da.corr()
	except:
		print("\n\t***Except!")
	else:
		print(type(k))
		k.to_excel("C:/Users/Khatuntsevsv/Desktop/W/Datas/save.0.xlsx", sheet_name="run10")
		
def getcolumnsnames(filename, filenamesheet, savedfilename):
	
	get = pandas.read_excel(filename, filenamesheet)
	
	l = get.columns
	ll = l.to_list()
	
	print(type(l), type(ll))
	
	lsaved = []
	
	
	
	for i in l:
		ser = get[i]
		res1 =pandas.notnull(ser)
#		res1 =ser.isna()
#		if  
		print(type(res1), res1.shape)
		
#		na = ser.isna()
#		print(na.shape)
		flag = 0
		for i3 in res1:
			if i3==False:
				flag = 1
				break
			
		if flag==1:
			continue
		
		lsaved+=[i]
	count = 0
	for i in lsaved:
		count = count+1
		print(count, "\tLsaved:\t", i)
		
#		if res1.shape[0]>10:
#			for i2 in range(0, 5):
#				print(res1.iat[i2])
	getdf=pandas.DataFrame(set(l.to_list()))
	getdf.to_excel(savedfilename, header=False, index=False)

def comma_to_dot(strfloat):
	retval='0.0'
	try:
		g = strfloat.split(',')
	except:
		print(__name__)
	else:
		if len(g)==2:
			retval=g[0] + '.' + g[1]
	
	return float(retval)

def getmaxmin(filename, sheet):
	g = pandas.read_excel(filename, sheet)
	columns_names = g.columns
	for i in columns_names:
#		print(i, max(g[i]))
#		print(i, type(g[i].iat[0]), g.shape,g[i], "len(g[i]):\t", type(comma_to_dot(g[i].iat[0])), sep="\t")
		collist = []
		for i2 in g[i]:
			collist+=[comma_to_dot(i2)]
		print(i)
		print(min(collist), '-', max(collist))
	
def open_txt(f):
	of = open(f)
	g = of.read().split("\n")
	for i in g:
		print(i, len(g), sep="\t")
	return g
	
def dropnull(dataframe):
	print('dropnull')
	
def dropnullcol(df):
	'''
	drop null collumns
	'''
	dfr, dfc = df.shape
	
	colnames = df.columns
	
	delcol = []
	
	for el in colnames:
		k = 0
		delrow=[]
		for i in range(0, dfr):
			if type(df[el].iat[i])==str and \
			(df[el].iat[i]=='Null' or df[el].iat[i]=='null' or df[el].iat[i]=='NULL'):
				k+=1
		if k==dfr:
			delcol+=[el]
	return df.drop(delcol, axis=1)

def getnamedcol_1(dataframe, colname):
	'''
	colname - list
	'''
	dfr, dfc = dataframe.shape
	
	lcol = []
	for i in dataframe.columns:
		cond = 0
		for i2 in colname:
			if i.count(i2):
				cond+=1
		if cond==len(colname):
			lcol+=[i]
#		if i.count('RAB') and i.count('112'):
#			lcol+=[i]
#	print('112:\t', lcol)
	retl=[]
#	ret112=retl
	for el in lcol:
		for i in range(0, dfr):
			if type(dataframe[el].iat[i])!=str and dataframe[el].iat[i]==1:
				retl+=[i]
	return set(retl)

from decimal import *
getcontext().prec = 6
def getstatdf(dataframe):
	
	
	rows, columns = dataframe.shape
	
	
	print('Count elements in Series')
	for el in dataframe.columns:
		trig = 0
		sl = dataframe[el].to_list()
		setsl = set(sl)
		for el_setsl in setsl:
			count = 0
			for el_sl in sl:
				if el_sl == el_setsl:
					count+=1
			if count>1:
				if trig==0:
					trig+=1
					print()
				print(el, el_setsl, f'{count}/{rows}')
		try:
			mean = dataframe[el].mean()
		except:
			pass
		else:
#			print(mean)
			l = []
			for i in range(0, rows):
				try:
					l +=[ dataframe[el].iat[i] - mean]
					low = min(l)/mean*100
					maxl = max(l)/mean*100
				except:
					pass
				else:
					print(el, ':\t', min,'\t', max)

def equstr(s1, s2):
	k= min(len(s1), len(s2))
#	print(k)
	
	l=[]
	for i in range(0, k):
		if s1[i]==s2[i]:
			l+=[1]
		else:
			l+=[0]
	print(l)
	
	print(sum(l), k)

#get columns` names by criteria
def getcolname(df, critl):
	kl=[]
#	print(df.__doc__)
#	print(df.__name__)
	for eldf in df.columns:
		k = 0
		for ind in critl:
			if eldf.count(ind):
				k+=1
		if k==len(critl):
			kl+=[eldf]
	return sorted(kl)

# get indexes if datas are equal to 1 znachen
# получить названия всех колонок, удовлетворяющих одному условию
def getindexes(df, columnname, l):
	ll = []
	for i in range(0, df.shape[0]):
		if type(l) == type(df[columnname].iat[i]):
			if l == df[columnname].iat[i]:
				ll+=[i]
	return ll
# обработка временных интервалов (выделение периодов, т.е. от и до)			
def gettimeinterval(df, timecol, got_ind):
	print('***\tgettimeinterval')
	d = 0
	ind = 0
	periods=[]
	last = 0
	start = 0
	for el in got_ind:
		if ind ==0 and el == got_ind[0]:
			ind = 1
			start = el
#			continue
		else:
			diff = el - last
			if diff>1:
#				print(last, el)
#				periods+=[[start, last]]
				periods+=[[\
						   df.iat[start, 0], df.iat[last, 0],\
							df.iat[start, 0].ceil(freq='H'), df.iat[last, 0].floor(freq='H'),\
							start, last
							 ]]
				
				start = el
		
		last = el
	return periods
# получить название колонки по номеру столбца (от 0)
def getcolnamebynumcol(df, numer):
	k = -1
	for el in df.columns:
		if numer==k:
			k = el
			break
		k+=1
	if k==-1:
		print('Error getcolnamebynumcol')
#	else:
#		print('getcolnamebynumcol:\t', k)
	return k
# получить номер по названию колонки
#def getn

# прибавить временной интервал
def addtime(tstp, t):
	k = tstp.timestamp()
	k+=t
	return pandas.Timestamp(k, unit='s')
# преобразовать в ряд временной промежуток
def gettimeseries(tstp1, tstp2):
	t1 = tstp1.timestamp()
	t2 = tstp2.timestamp()
	
	l=[]
	end = t1
	while end<=t2:
		l+=[pandas.Timestamp(end, unit='s')]
		end+=3600
#	l+=[tstp2]
	return l

#get cut string
def getbeetstr(string, start, end):
	return string[len(start):string.find(end)]


			
	
			
			
	
			
	
			
	


