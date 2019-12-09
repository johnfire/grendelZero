#!/usr/bin/python3
import RPi.GPIO as GPIO
import computerStartUpFunctions as cSF


#cSF.restartAll()
GPIO.setmode(GPIO.BCM)
cSF.setUpRestart('101')

cSF.restartComputer('101')

