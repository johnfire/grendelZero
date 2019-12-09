#!/usr/bin/python3
# this function starts all the computers in the grendel system
# written by christopher rehm july 8th 2018

import startUpFunctions2 as comp
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

try:
	print("!+!		In startALLcomputers.py function")
	print("!+!		Initializing GPIO pins for system")
	comp.setup()
	print("!+!		Starting system computers now")
	comp.startupAll()
	print("!+!		Finishing system computer start function")
	print("!+!		Leaving startAllComputers.py function")
except Exception as e:
	print("!!!!!!		ERROR in startAllComputers.py function!  ")
	print(str(e))


