#!/usr/bin/python3
from picamera import PiCamera
from time import sleep
from datetime import datetime


camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/rZeroImages/'+str(datetime.now())+'Zero.jpg')
camera.stop_preview()
