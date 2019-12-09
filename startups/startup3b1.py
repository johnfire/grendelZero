#!/usr/bin/python3

import startUpFunctions2 as comp
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
try:
	print("!-!		Starting 3b1 only")
	comp.setup()
	comp.startup3b1()
	print("!-!		3b1 is up and running")
except Exception as e:
	print ("!!!!!		FAILURE in the 3b1 startup script")
	print(str(e))

