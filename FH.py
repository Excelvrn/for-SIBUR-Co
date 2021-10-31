# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 11:19:33 2021
communication FH-3050, FH-5050
@author: KhatuntsevSV
"""

import socket
import traceback


#addrIP = '127.0.0.1'
#addrIP = '10.81.28.1'
addrIP = 'yandex.ru'
#addrIP = 'localhost'
portIP = 80
addresIP = (addrIP, portIP)
#
##sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#print("getdeftimeout:\t")
#socket.setdefaulttimeout(5)
#try:
#	sock = socket.create_connection(addresIP)
#	ggg=' '
#	sock.recv(ggg)
#	print(ggg)
##	sock = socket.socket()
##except Exception:
#except:
#	traceback.print_exc()
#else:
#	print("sock:\t", sock)
#	print("hostname:\t", socket.gethostname())
##print()
#print(g)
	
	
'''
**** **** **** **** **** **** **** **** **** **** **** **** **** ****
Example
**** **** **** **** **** **** **** **** **** **** **** **** **** ****
'''
import socket
import sys

# СоздаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаем сокет к порту, через который прослушивается сервер
server_address = addresIP
print('Подключено к {} порт {}'.format(*server_address))
sock.connect(server_address)

try:
    # Отправка данных
    mess = '/?'
    mess='hop.ru'
    print(f'Отправка: {mess}')
    message = mess.encode()
    sock.sendall(message)
    
    # Смотрим ответ
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        mess = data.decode()
        print(f'Получено: {data.decode()}')

finally:
    print('Закрываем сокет')
    sock.close()