# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
Выгрузка данных через интервал времени: 24 х количество дней / количество тегов 

f - рабочий документ
shn - рабочий лист
"""
f="C:/Users/Khatuntsevsv/Desktop/W/Datas/Params.copy.1.xlsx"
shn=2#sheet_name=2


'''
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.values.html
Time - https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html?highlight=timestamp#pandas.Timestamp

Indexing in Numpy:a.to_numpy()[0,0]

'''
import  sys, pandas, numpy, matplotlib, math
import matplotlib.pyplot as mpl



#print(sys.argv,  "\n\n\n")
#print(sys.version, sys.version_info, sep='\n')
print("\n\n\n")
for i in range(0, len(sys.path)):
    print(sys.path[i])
	#sys.path+=['C:\asdfsadf']

#a=pandas.read_excel(f, sheet_name)
a=pandas.read_excel(f, shn)
numpy_a = a.to_numpy()
print(a.columns)
print(a.shape)
temp1=[]
p1=[]
tp = []
ptemp=[]

for i in range(0, a.shape[0]):
	if a.iat[i, 1]!="Null" and a.iat[i, 4]!="Null" :
		temp = a.iat[i, 1]+271.0
		temp1+=[temp]
		press = numpy_a[i, 4]
		p1+=[press*10]
		presstemp = numpy.float64(press) / numpy.float64(temp)
		ptemp+=[presstemp]
#		ptemp+=[(a.iat[i, 1]+271.0) * numpy_a[i, 4]]

#	tp+=[[l[i], p1[i]]]
#    l+=[[a.iat[i, 1], a.iat[i, 0]]]
#print(l[1], len(l), sep="\t")
'''
определение роста/спада
'''
def updown(l):
    new = 0
    last =0
    for i in range(0, len(l)):
        if i == 0:
            last = l[i]
        else:
            new = l[i]
            if (new < last):
                print("less", last, "-", new, "\t", i)
            elif (new > last):
                print("more", last, "-", new, "\t", i)
            last=new
    pass  
def updown_1(l):
	new = 0
	last =0
	UD1 = 0 #Three positions: 1 - equal, 2-more, 0 - less
	UD2 = 0
	retlist=[]
	for i in range(0, len(l)):
		new=l[i]
		if new>last:
			UD1 = 2
		elif new==last:
			UD1 = 1
		else:
			UD1 = 0
		if UD1!=UD2:
#			print(i, new,UD1, sep="\t")
			UD2=UD1
			retlist+=[[i,new, UD1]]
		last = new
	return retlist
def updown_less_param(l, param):
	for i in range(0, len(l)):
		if l[i]<param:
			print(i, l[i], sep="\t")
	pass

'''
решение уравнения
'''
def printlist(l):
    if (len(l)>1):
        for i in range(0, len(l)):
            print(i, "\t", l[i])
    else:
        print(l)
    pass

'''
Вырезка процесса
'''
def getmin(listl):
	listllen = len(listl)
	vlast = 0
	vnext = 0
	eud = 0
	eudlist=[]
	down_list=[]
#	 equ 1, more 2, less 0
	for i in range(0, listllen):
		if (listl[i]!="Null"):
#			print(i)
			if i>0:
				vnext=listl[i]
				if (vnext<vlast):
					down_list+=[[i, vnext]]
#					print(i, vnext, sep="\t")
			vlast = vnext
#	print(down_list)
	down_list2=[]
	for i in range(0, len(down_list)):
		if down_list[i][1]<0.05 and down_list[i][1]>0.01:
			down_list2+=[down_list[i]]
		print(down_list2)
			
#	print(listl[0:10, len(listl)])
	return down_list
def getmin2(listl):
#	print("Getmin2")
	listllen = len(listl)
	listi=[]
	cuttime=[]
	eud=0
#	 equ 1, more 2, less 0

	for i in range(0, listllen):
		if listl[i]>=330:
			listi+=[i]
	print(len(listi))
#			print(i, listl[i], sep="\t\t")
	for i in range(0, len(listi)):
		if i>0:
			if (listi[i]-listi[i-1])>15:
				cuttime+=[[listi[i-1], listi[i]]]
#				print(listi[i-1], listi[i], listi[i]-listi[i-1], sep="\t")
	print(len(cuttime))
	eud=0
	for i in range(cuttime[1][1], cuttime[2][0]):
		eud+=1
		print(i, listl[i])
	print(eud)
#				print(eud, listi[i-1], listi[i], listi[i]-listi[i-1], sep="\t")
#	for i in range(40970, 41012):
#		print(i, listl[i], sep="\t")
	

'''
Execute
'''
def main():
#	k = updown_1(l)
	ddelay= 19
	delay_step = 600
	delay=delay_step*ddelay + 552
	lim = 1440*14 + delay
	lim2 = lim + delay_step
	g=range(0,delay_step)
	matplotlib.pyplot.grid()
	mpl.plot(g, temp1[lim:lim2], label="Temperature")
	mpl.plot(g, p1[lim:lim2], label="Pressure")
	mpl.legend()
	mpl.xlabel("Time, minutes")
	mpl.ylabel("Temperature, *C")
	mpl.show()
#	print(lim/1440, lim2/1440)
#	mpl.draw()
#	getmin(p1)

#	updown_less_param(l, 36)
	pass
	

def main2():#	k = updown_1(l)
	ddelay= 19
	delay_step = 600
	delay=delay_step*ddelay + 552
	lim = 1440*14 + delay
	lim2 = lim + delay_step
	g=range(0,delay_step)
#	matplotlib.pyplot.grid()
	
	
	fig, (ax1, ax2) = mpl.subplots(2, 1)
	fig.suptitle('A tale of 2 subplots')
	
	ax1.plot(g, temp1[lim:lim2], label="Temperature")
	ax1.set_ylabel('Damped oscillation')
	
	ax2.plot(g, p1[lim:lim2], label="Pressure")
	ax1.grid()
	ax2.grid()
#	mpl.legend()
#	mpl.xlabel("Time, minutes")
#	mpl.ylabel("Temperature, *C")
	mpl.show()
#	print(lim/1440, lim2/1440)
#	mpl.draw()
#	getmin(p1)

#	updown_less_param(l, 36)
	pass
def main3():
#	k = updown_1(l)
	delay_step = 500
	delay= 0
	lim = 1440*14 + delay
	lim2 = lim + delay_step
	t=range(lim,lim2)
	
#	t = np.arange(0.01, 10.0, 0.01)
	data1 = temp1[lim:lim2]
	data2 = p1[lim:lim2]
	
	fig, ax1 = mpl.subplots()
	
	color = 'tab:red'
	ax1.set_xlabel('time, min')
	ax1.set_ylabel('Temperature, C', color=color)
	ax1.plot(t, data1, color=color)
	ax1.tick_params(axis='y', labelcolor=color)
	
	ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
	
	color = 'tab:blue'
	ax2.set_ylabel('Pressure, kgF/sm^2', color=color)  # we already handled the x-label with ax1
	ax2.plot(t, data2, color=color)
	ax2.tick_params(axis='y', labelcolor=color)
	
	fig.tight_layout()  # otherwise the right y-label is slightly clipped
	mpl.grid()
	mpl.show()
	pass
def main3_1():
#	k = updown_1(l)
	delay_step = 500
	delay= 0
	lim = 1440*14 + delay
	lim2 = lim + delay_step
	t=range(lim,lim2)
	
#	t = np.arange(0.01, 10.0, 0.01)
	data1 = temp1[lim:lim2]
#	data2 = p1[lim:lim2]
	data2 = ptemp[lim:lim2]
	
	fig, ax1 = mpl.subplots()
	
	color = 'tab:red'
	ax1.set_xlabel('time, min')
	ax1.set_ylabel('Temperature, K', color=color)
	ax1.plot(t, data1, color=color)
	ax1.tick_params(axis='y', labelcolor=color)
	
	ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
	
	color = 'tab:blue'
	ax2.set_ylabel('Press/Temp, kgF/(sm^2*K)', color=color)  # we already handled the x-label with ax1
	ax2.plot(t, data2, color=color)
	ax2.tick_params(axis='y', labelcolor=color)
	
	fig.tight_layout()  # otherwise the right y-label is slightly clipped
	mpl.grid()
	mpl.show()
	pass
def main4():
	'''
	anima
	'''
	import numpy as np
	import matplotlib.pyplot as plt
	from matplotlib.animation import FuncAnimation
	
	fig, ax = plt.subplots()
	xdata, ydata = [], []
	ln, = plt.plot([], [], 'ro')
	
	def init():
	    ax.set_xlim(0, 2*np.pi)
	    ax.set_ylim(-1, 1)
	    return ln,
	
	def update(frame):
	    xdata.append(frame)
	    ydata.append(np.sin(frame))
	    ln.set_data(xdata, ydata)
	    return ln,
	
	ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128), init_func=init, blit=True)
	plt.show()
	pass
def datas():
	'''
	transforming of data
	'''
	print('data transform:')
	for i in range(0, a.shape[0]):
#		if a.iat[i, 1]!="Null" or a.iat[i, 4]!="Null":
#		if (type(a.iat[i, 1])!='numpy.float64'):
#			print(i)
		if (type(a.iat[i, 1])!='numpy.float64'):
			print(i, type(a.iat[i, 1]))
#		temp1+=[a.iat[i, 1]+271.0]
#		p1+=[numpy_a[i, 4]*10]
def runprogram():
	run = 4
	if run ==1:
		main()
	elif run ==2:
		main2()
	elif run ==3:
		main3()
	elif run ==4:
		main3_1()
	elif run ==5:
		main4()
	pass

getmin2(temp1)
#datas()
runprogram()


