

#start all computers function, this is what activates the computers themselves.
# 

import RPi.GPIO as GPIO
from time import sleep 

STARTUP_TIME = 4
PAUSE_TIME = 5
HIGH =1
LOW = 0

def startupAll():
##    computers= {
##        "raspi2b1": 17,
##        "raspi2b2": 27,
##        "raspi2b3": 22,
##        "raspi3b1": 23,
##        "raspi3b2": 24
##        }

    try:
        GPIO.setwarnings(False)
        print("!-!		In startupALL, right before pulling each line high")
        startup2b1()
        sleep(PAUSE_TIME)
        startup2b2()
        sleep(PAUSE_TIME)
        startup2b3()
        sleep(PAUSE_TIME)
        startup3b1()
        sleep(PAUSE_TIME)
        startup3b2()
    except Exception as e:
        print("!!!!!!!		FAILURE in startupAll function")
        print(str(e))
    print("!-!		Start all computers function is finished running")

def startup2b1():
    try:
        print("!-!		Starting raspi2b1 now")
        GPIO.setwarnings(False)
        GPIO.output(17, HIGH)         # set GPIO to 1/GPIO.HIGH/True  
        sleep(STARTUP_TIME)                   # wait a second  
        GPIO.output(17, LOW)         # set GPIO to 0/GPIO.LOW
        print("!-!		Finished start up routine for raspi2b1")
    except Exception as e:
        print("!!!!!		FAILURE in startup2b1 function")
        print(str(e))
    print("!-!		Start 2b1 function is finished running")


def startup2b2():
    try:
        print("!-!		Starting raspi2b2 now")
        GPIO.setwarnings(False)
        GPIO.output(27, HIGH)         # set GPIO to 1/GPIO.HIGH/True  
        sleep(STARTUP_TIME)                   # wait a second  
        GPIO.output(27, LOW)         # set GPIO to 0/GPIO.LOW
        print("!-!		Finished start up routine for raspi2b2")
    except Exception as  e:
        print("!!!!!!		FAILURE in startup2b2 function")
        print(str(e))
    print("!-!		Start 2b2 function is finished running")

def startup2b3():
    try:
        print("!-!		Starting raspi2b3 now")
        GPIO.setwarnings(False)
        GPIO.output(22, HIGH)         # set GPIO to 1/GPIO.HIGH/True  
        sleep(STARTUP_TIME)                   # wait a second  
        GPIO.output(22, LOW)         # set GPIO to 0/GPIO.LOW
        print("!-!		Finished start up routine for raspi2b3")
    except Exception as e:
        print("!!!!!!		FAILURE in startup2b3 function")
        print(str(e))
    print("!-!		Start 2b3 function is finished running")

def startup3b1():
    try:
        print("!-!		Starting raspi3b1 now")
        GPIO.setwarnings(False)
        GPIO.output(23, HIGH)         # set GPIO to 1/GPIO.HIGH/True  
        sleep(STARTUP_TIME)                   # wait a second  
        GPIO.output(23, LOW)         # set GPIO to 0/GPIO.LOW
        print("!-!		Finished start up routine for raspi3b1")
    except:
        print("!!!!!!		FAILURE in startup3b1 function")
        print(str(e))
    print("!-!		Start 3b1 function is finished running")

def startup3b2():
    try:
        print("!-!		Starting raspi3b2 now")
        GPIO.setwarnings(False)
        GPIO.output(24, HIGH)
        sleep(STARTUP_TIME)
        GPIO.output(24, LOW)
        print("!-!		Finished start up routine for raspi3b2")
    except Exception as e:
        print("!!!!!!		FAILURE in startup3b2 function")
        print(str(e))
    print("!-!		Start 3b2 function is finished running")



def setup():
    try:
        print("!-!		Starting initizalization of GPIO pins NOW")
        GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD  PIO(): 
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)
        GPIO.output(17, LOW)
        GPIO.output(27, LOW)
        GPIO.output(22, LOW)
        GPIO.output(23, LOW)    
        GPIO.output(24, LOW)
        print("!-!		GPIO pins initialized")
    except Exception as e:
        print("!!!!!!		FAILURE in the initalization of GPIO pins")
        print(str(e))



