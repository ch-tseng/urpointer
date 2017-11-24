# -*- coding: utf-8 -*- 

comPort = "com26"   #PC的TTL2USB port
doubleClick = 0.55  #double click 的間隔最長到幾秒?
ignoreTime = 0.15  #double click間隔多少秒以下就視為一個click (避免誤觸)
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
			if(dclicktime>(ignoreTime*1000) and dclicktime<=(doubleClick*1000)):
				print ("{}. Last:{} Now:{} Diff:{}  ---> 上一頁".format(i, lastClicktime, nowtime, nowtime-lastClicktime))
				i += 1				
				lastClicktime = 0
				pyautogui.typewrite(["left", "ctrlleft"])
				serial.flushInput()
