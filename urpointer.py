# -*- coding: utf-8 -*- 

comPort = "com26"
doubleClick = 0.55
baudRate = 9600

import serial
import pyautogui
import sys
import time


serial = serial.Serial(comPort, baudRate)

i = 0
nowtime = 0
lastClicktime = 0


while True:
	
	nowtime = int(round(time.time() * 1000)) 
	dclicktime = nowtime-lastClicktime
	
	if(lastClicktime>0 and (dclicktime>(doubleClick*1000))):
		print ("{}. Last:{} Now:{} Diff:{}  ---> 下一頁".format(i, lastClicktime, nowtime, dclicktime))
		lastClicktime = 0
		i += 1		
		pyautogui.typewrite(["right", "ctrlright"]) 
		serial.flushInput()

		
	if(serial.inWaiting()):
		serial.flushInput()
		
		if(lastClicktime==0):
			lastClicktime = nowtime
			
		else:
			dclicktime = nowtime-lastClicktime
			if(dclicktime>200 and dclicktime<=(doubleClick*1000)):
				print ("{}. Last:{} Now:{} Diff:{}  ---> 上一頁".format(i, lastClicktime, nowtime, nowtime-lastClicktime))
				i += 1				
				lastClicktime = 0
				pyautogui.typewrite(["left", "ctrlleft"])
				serial.flushInput()
