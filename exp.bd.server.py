# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
Выгрузка данных через интервал времени: 24 х количество дней / количество тегов 

f - рабочий документ
shn - рабочий лист
"""
debug = 2 #Условие 1 Место выгрузки данных: 0 - файл, 1- сеть (БД)
run = 1 # Условие 2


#f="C:/Users/Khatuntsevsv/Desktop/W/Datas/FQR1461.xlsx"
#FRCA1411="C:/Users/Khatuntsevsv/Desktop/W/Datas/FRCA1411.xlsx"
#MR201A102407="C:/Users/Khatuntsevsv/Desktop/W/Datas/MR201A.1024.07.xlsx"
#MR201A101305="C:/Users/Khatuntsevsv/Desktop/W/Datas/MR201A.1013.05.xlsx"
#MR201_temperature_txt="C:/Users/Khatuntsevsv/Desktop/W/Datas/MR201.A.txt"
#MR201_temperature_txt = "\\tsclient\C\Users\Khatuntsevsv\Desktop\W\Datas\MR201.temperature.txt"
#MR201_temperature_server="D:/KhatuntsevSV/MR201.A.txt"
#MR201_temperature_server="D:\KhatuntsevSV/MR201.A.txt"
MR201_temperature_server='D:/KhatuntsevSV/MR201.AF.txt'
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
import sys, pandas, numpy, matplotlib, math
import matplotlib.pyplot as mpl

import sqlalchemy as sa
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
#    numpy_a = a.to_numpy()
#    print(a.columns)
#    print(a.shape)
    return a
def main():
    if debug==0:
        a = pandas.read_csv(MR201_temperature_server)
        a = open(MR201_temperature_server)
    elif debug==1:
#    '''
#    from SQL
#        '''
        server_data = "vertica+vertica_python://" + "Khatuntsevsv" + ":" + "Excelvrn!234" + "@vertica.sibur.local:5433/dwh"
        engine = sa.create_engine(server_data)
        conn = engine.connect()
        #MR_201*.temperature
        a = pandas.read_sql('''SELECT  tag_name,ts, value_float FROM ODS_MES_HIST_VSK.KAFKA_MESINT_VERTICA where tag_name like 'PSP_MR201_A.TRSA2012' or tag_name like 'PSP_MR201_B.TRSA2017' or tag_name like 'PSP_MR201_C.TRSA2023' or tag_name like 'PSP_MR201_D.TRSA20114' or tag_name like 'PSP_MR201_E.TRSA20120' or tag_name like 'PSP_MR201_F.TRSA20126' ORDER BY  tag_name, ts''', conn)
        #MR_201*.FT* (Количество вещества)
        #позже
#        b = pandas.read_sql('''SELECT  count(*),tag_name FROM ODS_MES_HIST_VSK.KAFKA_MESINT_VERTICA where tag_name like '%201%FT%' group by tag_name ; ''', conn)
    elif debug==2:
#    '''
#    from SQL
#        '''
        server_data = "vertica+vertica_python://" + "Khatuntsevsv" + ":" + "Excelvrn!234" + "@vertica.sibur.local:5433/dwh"
        engine = sa.create_engine(server_data)
        conn = engine.connect()
        #MR_201*.temperature
        a = pandas.read_sql('''SELECT  tag_name,ts, value_float FROM ODS_MES_HIST_VSK.KAFKA_MESINT_VERTICA where tag_name like 'PSP_MR201_A.TRSA2012' ORDER BY  tag_name, ts''', conn)
#        b = pandas.read_sql('''SELECT  count(*),tag_name FROM ODS_MES_HIST_VSK.KAFKA_MESINT_VERTICA where tag_name like '%201%FR%' group by tag_name ; ''', conn)

   # print("Step",a.shape)
#    print(a.iloc[1])
    '''
    tag_name     ts     values
    '''
    tags=a.iloc[:,0]
    tss=a.iloc[:,1]
    values = a.iloc[:,2]
    
    #tagsi - tags` names
    tagsi = []
    
    # tagsise - start|end tags
    # all tags, founded in "tags"
    tagsise = []
    #
    #    tagspositions    tag`s start position
    tagspositions=[]
    print("\t\t\tDB is downloaded")
    for i in range(0, len(tags)):
        if i==0:
            tagsi+=[tags[i]]
            tagspositions+= [i]
        else:
            if tagsi.count(tags[i])==0:
                tagsi+=[tags[i]]
                tagspositions+= [i]
    print(tagsi,tagspositions)
    
    
    '''
    loop_start=0
    for i in range(0, len(tagsi)):
        for i2 in range(loop_start, len(tags)):
            if (tagsi[i] == tags[i2]):
                tagsise+=[tagsi[i], i2]
                loop_start=i
                break
    print("tags and index", tagsise)
    '''
#    print(a.iloc[:tagsise[3], 2])
    
#    ts_A=a.iloc[tagsise[1]:tagsise[3], 1]
#    temp_A=a.iloc[tagspositions[0]:tagspositions[1], 2]
    temp_A=a.iloc[tagspositions[0]:, 2]
    print("\t\t\ttemp_A is created")
#    print(ts_A[0], temp_A[0])
#    synteze_B=a.iloc[tagsise[3]:tagsise[5], 1:3]
#    synteze_C=a.iloc[tagsise[5]:tagsise[7], 1:3]
#    synteze_D=a.iloc[tagsise[7]:tagsise[9], 1:3]
#    synteze_E=a.iloc[tagsise[9]:tagsise[11], 1:3]
#    synteze_F=a.iloc[tagsise[11]:, 1:3]
#    synteze_all=[synteze_A, synteze_B, synteze_C, synteze_D, synteze_E, synteze_F]
    
#    print(synteze_A[0])
    # return syntheze times
#    temperature_lim=50
    def getsynthezetime(syntheze, temperature_lim=50):
        retlist=[]
        len_synth=len(syntheze)
        if len_synth>1:
            updown = -1
            for i in range(1, len_synth):
                if updown<0:
                    if (syntheze[i]>=temperature_lim) and (syntheze[i-1]<temperature_lim):
                        retlist+=[i]
                        updown = 1
                else:
                    if (i%10000==0):
                        print("\tdone", i, " of ", len_synth)
                    if (syntheze[i]>=temperature_lim) and (syntheze[i-1]<temperature_lim) and (updown==0):
                        retlist+=[i]
                        updown = 1
                    elif (syntheze[i]<temperature_lim) and (syntheze[i-1]>=temperature_lim) and (updown==1):
                        retlist+=[i]
                        updown = 0
        return retlist
    
    templist_A=getsynthezetime(temp_A)
    print(templist_A)
    tss_A=[]
    wrotenfile = open("./temp_a.txt", 'w')
    for i in range(1, len(templist_A),2):
        tss_A+=[[tss[templist_A[i-1]], tss[templist_A[i]]]]
        print("temperatures_A:\t", a.iat[templist_A[i-1], 1], a.iat[templist_A[i], 1], file=wrotenfile)
    wrotenfile.close()
    
#        tss_A+=[[tss[templist_A[i-1]], tss[templist_A[i]], tss[templist_A[i]].timestamp()- tss[templist_A[i-1]].timestamp()]]
    
##    tss_A[i][0],tss_A[i][1],tss_A[i][2], file=wrotenfile, sep="\t"
#    for i in range(0 ,len(tss_A)):
#        print()
#        print(i,":",tss_A[i], sep="\t\t")
#        print("Temperature_MR201A", a.iat[tss_A[i][0], 1],tss_A[i][1],tss_A[i][2], file=wrotenfile, sep="\t")
#    wrotenfile.close()

#    for i in range(1,len(tagsise))

#        print(len(temp_a_index), temp_a_index, sep="\t\n")
    '''
SELECT COUNT(*) as count FROM 
'''
    
def main2():
#    a = readfile(MR201A102407, 7)
    a=pandas.read_excel(MR201A102407, 6)
    print(a.shape)
    print(a.columns)
    print(a.iloc[0])
    '''
    min-max temperature
    '''
#    print(a.iloc[:,0])
    g=a.iloc[:,4]
    updown=0
    iterprocess = 0
    uplist=[]
    downlist=[]
    for i in range(0, len(g)):
        if g[i]>50:
            if updown == 0:
                iterprocess+=1
#                print(iterprocess, i, g[i])
                uplist+=[i]
            updown = 1
#            print(i, g[i], sep="\t")
        else:
            if updown == 1:
                downlist+=[i]
            updown = 0
    full=uplist + downlist
    print(len(uplist), len(downlist), len(full))
    sortedfull=sorted(full)
#    print(full)
#    print(sortedfull)
    '''
    periods
    '''
    modifiedfull=[]
    timelist=a.iloc[:,0]

#    for i in range(0, len(sortedfull)):
#        print(timelist[sortedfull[i]])
    if full[0]==uplist[0]:
        print("uplist")
        for i in range(0, len(full),2):
#            print(i)
            if i>0:
                modifiedfull+=[[full[i-2], full[i-1]]]
#        print("modifiedfull:", modifiedfull)
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
#                    print(timedelta1, timedelta2)
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
#        print("Start", "End", "1461", "1471", "1411")
#        for i in range(0, len(modifiedfull)):
#            print(modifiedfull[i])
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

#        fig, ax1 = mpl.subplots()
        steps = range(0, len(modifiedfull))
        
#        color = 'tab:red'
#        ax1.set_xlabel('Synteze number, #')
#        ax1.set_ylabel('sprep1461', color=color)
#        ax1.plot(steps, data1, color=color)
#        ax1.tick_params(axis='y', labelcolor=color)
#        
#        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
#        
#        color = 'tab:blue'
#        ax2.set_ylabel('sprep1471', color=color)  # we already handled the x-label with ax1
#        ax2.plot(steps, data2, color=color)
#        ax2.tick_params(axis='y', labelcolor=color)
#        
#        fig.tight_layout()  # otherwise the right y-label is slightly clipped
#        mpl.grid()
        
        # red dashes, blue squares and green triangles
        mpl.plot(steps, data1, 'r--', steps, data2, 'bs', steps, data3, 'g^')
        mpl.show()
#        print(modifiedfull[2])
#        print(modifiedfull)
#    else:

def main3(readfile, sheet):
#    a = readfile(MR201A102407, 7)
    a=pandas.read_csv(readfile, sheet)
    print(a.shape)
    print(a.columns)
    print(a.iloc[0])
    '''
    min-max temperature
    '''
#    print(a.iloc[:,0])
    g=a.iloc[:,4]
    updown=0
    iterprocess = 0
    uplist=[]
    downlist=[]
    for i in range(0, len(g)):
        if g[i]>50:
            if updown == 0:
                iterprocess+=1
#                print(iterprocess, i, g[i])
                uplist+=[i]
            updown = 1
#            print(i, g[i], sep="\t")
        else:
            if updown == 1:
                uplist+=[i]
            updown = 0
#    full=uplist + downlist
#    print(len(uplist), len(downlist), len(full))
#    sortedfull=sorted(full)
#    print(full)
#    print(sortedfull)
    '''
    periods
    '''
    modifiedfull=[]
    timelist=a.iloc[:,0]


#    print(uplist)
    for i in range(0, len(uplist), 2):
        if i>0:
            modifiedfull+=[[uplist[i-2], uplist[i-1]]]
#    print(modifiedfull)

#    for i in range(0, len(sortedfull)):
#        print(timelist[sortedfull[i]])
#    if full[0]==uplist[0]:
#        print("uplist")
#        for i in range(0, len(uplist), 2):
##            print(i)
#            if i>0:
#                modifiedfull+=[[uplist[i-2], uplist[i-1]]]
#        print("modifiedfull:", modifiedfull)
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
#                    print(timedelta1, timedelta2)
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
#        print("Start", "End", "1461", "1471", "1411")
#        for i in range(0, len(modifiedfull)):
#            print(modifiedfull[i])
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
#        data1+=[modifiedfull[i][2]/M_DDS]
#        data2+=[modifiedfull[i][3]/M_SiCl4]
#        data3+=[modifiedfull[i][4] / M_nBuLi/10]
    for i in range(0, len(modifiedfull)):
        if i!=5 and i!=18 and i!=21 and i!=22:
#        if i!=6 and i!=10 and i!=13 and i!=15 and i!=21 and i!=22:
            data4+=[0.32]
        else:
            data4+=[0.26]
        
#        mpl.plot(steps, data1, 'r--', steps, data2, 'bs', steps, data3, 'g^')

#        fig, ax1 = mpl.subplots()
    steps = range(0, len(modifiedfull))
        
#        color = 'tab:red'
#        ax1.set_xlabel('Synteze number, #')
#        ax1.set_ylabel('sprep1461', color=color)
#        ax1.plot(steps, data1, color=color)
#        ax1.tick_params(axis='y', labelcolor=color)
#        
#        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
#        
#        color = 'tab:blue'
#        ax2.set_ylabel('sprep1471', color=color)  # we already handled the x-label with ax1
#        ax2.plot(steps, data2, color=color)
#        ax2.tick_params(axis='y', labelcolor=color)
#        
#        fig.tight_layout()  # otherwise the right y-label is slightly clipped
#        mpl.grid()
        
        # red dashes, blue squares and green triangles
    mpl.plot(steps, data1, 'r--', steps, data2, 'bs-', steps, data3, 'g^-', steps, data4, 'c^-')
    mpl.show()
#        mpl.savefig('myfig.png')
#        print(modifiedfull[2])
#        print(modifiedfull)
#        writingfile = open("newfile.txt", os.O_WRONLY)
##        print("asdfasdf", file=writingfile)
#        os.close(writingfile)
    def correl(text, d1, d2):
        g1=numpy.corrcoef(d1, d2)
        g2 = numpy.cov(d1, d2)
#        g2 = numpy.corrcoef(d2, d1)
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

def runprogram():
    if run ==1:
        main()
    elif run ==2:
        main2()
    elif run ==3:
        k = main3(MR201A101305, "1013_05")
#        model = CatBoostRegressor(iterations=1000)

#getmin2(temp1)
#datas()
runprogram()


