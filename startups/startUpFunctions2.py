

#start all computers function, this is what activates the computers themselves.
# 

import RPi.GPIO as GPIO
from time import sleep 

STARTUP_TIME = 1
PAUSE_TIME = 2
HIGH = 1
LOW = 0

def startupAll():
##    computers = {
##        101: 17,
##        103: 27,
##        104: 22,
##        102: 23,
##        105: 24,
##        106: 10,
##        107: 9,
##        }

    try:
        GPIO.setwarnings(False)
        print("!-!		In startupALL, right before pulling each line high")
        startup17()
        sleep(PAUSE_TIME)
        startup27()
        sleep(PAUSE_TIME)
        startup22()
        sleep(PAUSE_TIME)
        startup23()
        sleep(PAUSE_TIME)
        startup24()
        sleep(PAUSE_TIME)
        startup10()
        sleep(PAUSE_TIME)
        startup9()
        #sleep(PAUSE_TIME)
        #startup11()

    except Exception as e:
        print("!!!!!!!		FAILURE in startupAll function")
        print(str(e))
    print("!-!		Start all computers function is finished running")

def startup17():
    try:
        print("!-!		Starting 2b1 now")
        GPIO.setwarnings(False)
        GPIO.output(17, HIGH)         # set GPIO to 1/GPIO.HIGH/True  
        sleep(STARTUP_TIME)                   # wait a second  
        GPIO.output(17, LOW)         # set GPIO to 0/GPIO.LOW
        print("!-!		Finished start up routine for 2b1")
    except Exception as e:
        print("!!!!!		FAILURE in startup 2b1 function")
        print(str(e))
    print("!-!		Start 2b1 function is finished running")


def startup27():
    try:
        print("!-!		Starting 2b2 now")
        GPIO.setwarnings(False)
        GPIO.output(27, HIGH)         # set GPIO to 1/GPIO.HIGH/True  
        sleep(STARTUP_TIME)                   # wait a second  
        GPIO.output(27, LOW)         # set GPIO to 0/GPIO.LOW
        print("!-!		Finished start up routine for 2b2")
    except Exception as  e:
        print("!!!!!!		FAILURE in startup 2b2 function")
        print(str(e))
    print("!-!		Start 2b2 function is finished running")

def startup22():
    try:
        print("!-!		Starting 2b3 now")
        GPIO.setwarnings(False)
        GPIO.output(22, HIGH)         # set GPIO to 1/GPIO.HIGH/True  
        sleep(STARTUP_TIME)                   # wait a second  
        GPIO.output(22, LOW)         # set GPIO to 0/GPIO.LOW
        print("!-!		Finished start up routine for 2b3")
    except Exception as e:
        print("!!!!!!		FAILURE in start up 2b3 function")
        print(str(e))
    print("!-!		Start 2b3 function is finished running")

def startup23():
    try:
        print("!-!		Starting 2b4 now")
        GPIO.setwarnings(False)
        GPIO.output(23, HIGH)         # set GPIO to 1/GPIO.HIGH/True  
        sleep(STARTUP_TIME)                   # wait a second  
        GPIO.output(23, LOW)         # set GPIO to 0/GPIO.LOW
        print("!-!		Finished start up routine for 2b4")
    except:
        print("!!!!!!		FAILURE in startup 2b4 function")
        print(str(e))
    print("!-!		Start 2b4 function is finished running")

def startup24():
    try:
        print("!-!		Starting 3b1 now")
        GPIO.setwarnings(False)
        GPIO.output(24, HIGH)
        sleep(STARTUP_TIME)
        GPIO.output(24, LOW)
        print("!-!		Finished start up routine for 3b1")
    except Exception as e:
        print("!!!!!!		FAILURE in startup 3b1 function")
        print(str(e))
    print("!-!		Start 3b1 function is finished running")

def startup10():
    try:
        print("!-!		Starting 4b1 now")
        GPIO.setwarnings(False)
        GPIO.output(10, HIGH)
        sleep(STARTUP_TIME)
        GPIO.output(10, LOW)
        print("!-!		Finished start up routine for 4b1")
    except Exception as e:
        print("!!!!!!		FAILURE in startup 4b1 function")
        print(str(e))
    print("!-!		Start 4b1 function is finished running")

def startup9():
    try:
        print("!-!		Starting 3b2 now")
        GPIO.setwarnings(False)
        GPIO.output(9, HIGH)
        sleep(STARTUP_TIME)
        GPIO.output(9, LOW)
        print("!-!		Finished start up routine for 3b2")
    except Exception as e:
        print("!!!!!!		FAILURE in startup 3b2 function")
        print(str(e))
    print("!-!		Start 3b2 function is finished running")

def startup11():
    try:
        print("!-!		Starting raspi--- now")
        GPIO.setwarnings(False)
        GPIO.output(11, HIGH)
        sleep(STARTUP_TIME)
        GPIO.output(11, LOW)
        print("!-!		Finished start up routine for raspi---")
    except Exception as e:
        print("!!!!!!		FAILURE in startup--- function")
        print(str(e))
    print("!-!		Start --- function is finished running")

def setup():
    try:
        print("!-!		Starting initizalization of GPIO pins NOW")
        GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD  PIO(): 
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)
        GPIO.setup(10, GPIO.OUT)
        GPIO.setup(9,  GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        GPIO.output(17, LOW)
        GPIO.output(27, LOW)
        GPIO.output(22, LOW)
        GPIO.output(23, LOW)    
        GPIO.output(24, LOW)
        GPIO.output(10, LOW)
        GPIO.output(9,  LOW)
        GPIO.output(11, LOW)
        print("!-!		GPIO pins initialized")
    except Exception as e:
        print("!!!!!!		FAILURE in the initalization of GPIO pins")
        print(str(e))



