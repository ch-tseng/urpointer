# -*- coding: utf-8 -*- 

comPort = "com26"
doubleClick = 0.5
baudRate = 9600

import serial
import pyautogui
import sys
import time

current_milli_time = lambda: int(round(time.time() * 1000)) 
serial = serial.Serial(comPort, baudRate)

i = 0

while True:
	
    countClick = 0
    if(serial.inWaiting()):
        bytesToRead = serial.inWaiting()
        data = str(serial.read(bytesToRead), errors='replace')
        countClick += 1
        time.sleep(doubleClick)
        i += 1	
	
        if(serial.inWaiting()):	
            bytesToRead = serial.inWaiting()
            data = str(serial.read(bytesToRead), errors='replace')
            countClick += 1

    if(countClick>1):
        print ("{} 上一頁".format(i))            	
        pyautogui.typewrite(["left", "ctrlleft"])
		
    if(countClick==1):
        print ("{} 下一頁".format(i))
        pyautogui.typewrite(["right", "ctrlright"])
        serial.flushInput()
        #time.sleep(doubleClick)
        #serial.flushInput()	
        
