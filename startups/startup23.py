#!/usr/bin/python3

import startUpFunctions2 as comp
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
try:
	print("!-!		Starting 23 only")
	comp.setup()
	comp.startup23()
	print("!-!		23 is up and running")
except Exception as e:
	print ("!!!!!		FAILURE in the 23 startup script")
	print(str(e))

