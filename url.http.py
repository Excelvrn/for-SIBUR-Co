# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 09:46:51 2021

@author: KhatuntsevSV
"""

import sys
import struct
import socket, ssl
import time
import select
import re
#from optparse import OptionParser
import urllib.request
import http.client as I_HC
import os
#import http.client

global vaddr 
vaddr = 2

def _print(i, stri):
	print(i, stri)
	pass

def control(equ, sign, text):
	if equ == sign:
		print(text)
	else:
		print("\n\t***Control***")
	pass

def controla(equ, sign, a):
	if equ == sign:
		a
	else:
		print("\n\t***Control***")
	pass

if vaddr==1:
	addr=("www.google.ru", 443)
elif vaddr==2:
	addr=("www.alib.ru", 80)

#addr=("hop.ru", 80)
#datas = b"GET search?q=aliexpress+penis"
#datar = bytes(1024)
#data2 = str()
#sites_tup = list()
##req1 = "/search?q=send+recv+in+python+ssl"
#req2 = "/search?q=aliexpress+penis"

#with urllib.request.urlopen("https://www.google.com/") as f:
#	print(f.read() )


def main():
	HC_CONN = 	I_HC.HTTPSConnection(addr[0],addr[1], timeout = 2)
	_print("1.0.0", HC_CONN)
	print(HC_CONN.connect())
	_print("1.0.1",HC_CONN.request("POST","https://www.google.com/search?client=firefox-b-e&q=send+recv+in+python+ssl") )
	
	SOCK =  socket.socket(socket.AF_INET)
	control(SOCK, 0, "Error SOCK!")
	
#	SOCK_CON = socket.create_connection(addr, 1)
#	control(SOCK_CON, 0, "Error SOCK_CON!")
	
	SOCK_WRAP = ssl.wrap_socket(SOCK)
	_print("1.2", SOCK_WRAP)
	
	SOCK_WRAP.settimeout(2)
	
	SOCK_WRAP_CON = SOCK_WRAP.connect(addr)
	_print("1.3", SOCK_WRAP)
	
	#SOCK_CERT = ssl.get_server_certificate(addr, ssl.PROTOCOL_SSLv23)
	SOCK_CERT =SOCK_WRAP.getpeercert(True)
	_print("1.4",len(SOCK_CERT))
	_print("1.5", ssl.SSLContext(ssl.PROTOCOL_SSLv23))
	
	#data = SOCK_WRAP.recv(1024)
	
#	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#	ss = ssl.wrap_socket(s, ssl.PROTOCOL_TLSv1)
#	addr = ('www.google.com', 443)
#	ss.connect(addr)
#	SOCK_WRAP.send(datas)
#	resp = SOCK_WRAP.recv(1000)
#s	print(resp)
#	ss.close()

	_print(2, SOCK_WRAP.close())
	_print(3, SOCK.close())
	
	pass


def work():
	conn = http.client.HTTPSConnection(addr[0], addr[1])

	conn.request("GET", "/search?q=asdf")
	r1 = conn.getresponse()
	print(r1.status, r1.reason)

	data1 = r1.read()  # This will return entire content.
	print(len(data1))

	FD = open("data.html", mode = 'a')
	_print("1.0.0.1", len(data1))
	data2 = str(data1).encode("utf-8")
	print(data2[2: (len(data1) - 1)], file=FD)
	print("FD is\t", FD)
	sites_tup.append(FD)	
	FD.close()
	conn.close()
	#pass
	return data2

def work2(addr_tup, request, createfilename):
	conn = http.client.HTTPSConnection(addr_tup[0], addr_tup[1])
	#addr_tup=("www.google.ru", 443)

	conn.request("GET", request)
	r1 = conn.getresponse()
	print(r1.status, r1.reason)

	data1 = r1.read()  # This will return entire content.
	print(len(data1))

	FD = open(createfilename, mode = 'a')
	_print("1.0.0.1", len(data1))
	data2 = str(data1).encode("utf-8")
	print(data2[2: (len(data1) - 1)], file=FD)
	print("FD is\t", FD)
	sites_tup.append(FD)	
	FD.close()
	conn.close()
	#pass
	return data2
def connect_to(adr):
	print(adr[0], adr[1])
	conn = I_HC.HTTPSConnection(adr[0], adr[1])
	print(conn)
	conn.request("GET", "/")
	r1 = conn.getresponse()
	print(r1)
	data = r1.read()
	print(data)
	

	#main()
#work()
#print("sites_tup:\t", sites_tup)
connect_to(("www.beget.ru", 443))