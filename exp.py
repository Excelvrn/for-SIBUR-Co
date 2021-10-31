# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
Выгрузка данных через интервал времени: 24 х количество дней / количество тегов 

"""
#f="C:/Users/Khatuntsevsv/Desktop/TagsMES.xlsx"
#f="C:/Users/Khatuntsevsv/Desktop/W/PRJ/datat.xlsx"
#f="C:/Users/Khatuntsevsv/Desktop/W/PRJ/fp_tags_to_load.xlsx"
'''
f - рабочий документ
shn - рабочий лист
'''
f="C:/Users/Khatuntsevsv/Desktop/W/PRJ/Temps16.xlsx"
shn=2#sheet_name=2

'''
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.values.html
Time - https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html?highlight=timestamp#pandas.Timestamp

Indexing in Numpy:a.to_numpy()[0,0]

'''
import  sys, pandas, numpy



#print(sys.argv,  "\n\n\n")
#print(sys.version, sys.version_info, sep='\n')
print("\n\n\n")
for i in range(0, len(sys.path)):
    print(sys.path[i])

#a=pandas.read_excel(f, sheet_name)
a=pandas.read_excel(f, shn)
#print(a )
#print(len(a))
#a.info(verbose=False)
#a.info()

print("\n\n\n")
na = a.to_numpy()
#nag = numpy.array(na, dtype = float)
#print(na.shape)
#print(na)
#print("NA:\t", na[0,])
#print("NA 0:3:\t", na[0:3,0], "\n")
#print("NA`s type:\t", type(na[0:3,0]))

#datalist=[]
print("na.shape:\t", na.shape)

#dl = na[0:na.shape[0], 1]# !!!
#print("dl:\n", dl)

#for i in range(1, na.shape[0]):
#   print(dl[i])
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
'''

def main():
#    M1 = numpy.array([[2., 5.], [1., -10.]]) # Матрица (левая часть системы)
#    v1 = numpy.array([1., 3.]) # Вектор (правая часть системы)
#    solar = numpy.linalg.solve(M1, v1)
#    printlist(solar)
#    print(na[0:30, 1])
    nashape = 3

    Q=numpy.copy(na[1:3, 1:3])
    C = numpy.copy(na[1:3, 4])
    print("Q:\t", Q)
    print("C:\t", C)
#    deter = numpy.linalg.det(Q, C)
    A = numpy.linalg.solve(Q,C)
#    print(A)
    pass
main()    

