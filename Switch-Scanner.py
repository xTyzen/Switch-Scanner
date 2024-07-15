#!/usr/bin/python3
#Code by Thitou kas ツ
#Developper by Thitou Kas ツ
#My channel youtube : Thitou Kas ツ

print("""\x1b[36;40m███████╗██╗    ██╗██╗████████╗ ██████╗██╗  ██╗      ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔════╝██║    ██║██║╚══██╔══╝██╔════╝██║  ██║      ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
███████╗██║ █╗ ██║██║   ██║   ██║     ███████║█████╗███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
╚════██║██║███╗██║██║   ██║   ██║     ██╔══██║╚════╝╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
███████║╚███╔███╔╝██║   ██║   ╚██████╗██║  ██║      ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚══════╝ ╚══╝╚══╝ ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝      ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝V.3.0""")

# Les outils spéciales 

import sys 
import os                                     
import socket

#code
Ip = input('>>> Veuillez entrer adresse ip a scanner : ')
print('[*] Scan de : ' + Ip + ' Loading...')
try:
	for port in range(1,1025):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((Ip, port))
		if result == 0:
			print('[#] Port ' + str(port) + ' Ouvert')
		sock.close()
except socket.gaierror:
	print('Serveur Injoignable')		
	sys.exit()
except socket.error:
	print('Serveur Injoignable')
	sys.exit()

print('Fin du scan')



