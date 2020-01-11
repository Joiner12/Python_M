#-*- encoding:utf-8-*-

import serial
import serial.tools.list_ports as lp
import os 
import datetime

from PyQt5.QWidgets import QComboBox,QListView
from PyQt5.QtCore import pyqtSignal

global com_port_avilable
com_port_avilable=[]


# list of serial
def ListOutPort():
	portlist = list(lp.comports())
	if len(portlist) == 0:
		print('no port exist')
	else:
		for i in portlist:
			if i.description.find("USB-to-Serial")!= -1:
				com_port_avilable.append(i)
				print(i)
			
# read port
def ReadPort33():
	SerialStatus = False
	try:
		# open port
		A33_Port = serial.Serial("COM5",115200,timeout = 10)
		print("USB-Serial-Port Open Succeed...")
		SerialStatus = True
		# close 
		
		A33_Port.close()

	except Exception as ep:
		print("Serial Port Open failed:",ep)
		SerialStatus = False

	return SerialStatus



if __name__ == "__main__":
	#---------#
	os.system("cls")
	a = datetime.datetime.now()
	time_now = a.strftime('%a, %b %d %H:%M:%S')
	print(time_now)
	'''
		---------
	'''
	ListOutPort()

	'''
		b = ReadPort33()
		print(b)
	'''
	

	'''
		PyQt5 Com tool
	'''
