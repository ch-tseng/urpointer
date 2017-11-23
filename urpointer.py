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

while True:
	
	#data = ''
    if(serial.inWaiting()):
        bytesToRead = serial.inWaiting()
        data = str(serial.read(bytesToRead), errors='replace')
        print("First")	
        time.sleep(0.3)
        serial.flushInput()	
        time.sleep(doubleClick)
		
        if(serial.inWaiting()):	
            bytesToRead = serial.inWaiting()
            data = str(serial.read(bytesToRead), errors='replace')

            print("Next")
            print ("上一頁")            	
            pyautogui.typewrite(["left", "ctrlleft"])
			
            
                				
        else:
            print ("下一頁")	
            pyautogui.typewrite(["right", "ctrlright"])
			
        #time.sleep(doubleClick)
        #serial.flushInput()	
        
