# christopher rehm author grendel one project
# www.tandkcybernetics. christopherrehm.de
# released under the creative commons share for noncommerical use
import RPi.GPIO as GPIO
from time import sleep

################################################################
#restart function for computers in system:
def setUpRestart(computerNumber):

### list of computers and which pin resets the system here:
    listOfComputersAndGPIOPins={'101': 17,'102': 27,'103': 22,'104': 23}
    #code
    """Set up GPIO pins for computer remote restart.
       planned use is in the grendel start up routine."""

    try:
        print("in restart")
        GPIO.setmode(GPIO.BCM)
        print("setmode")
        startNumber=listOfComputersAndGPIOPins[computerNumber]
        print(startNumber, type(startNumber))
        GPIO.setup(startNumber, GPIO.OUT)
        GPIO.output(startNumber, 0)         # set GPIO to 1/GPIO.HIGH/True
    except:
        print("Failure in the setupRestart routine.")
        
def restartComputer(computerNumber):

SAxxzaAAAAAAAAAAAAAAAAAAAAAAAAAA    """This function takes an integer value and sends a pulse to the correct
    gpio pin to cause a reset action."""

    ### list of computers and which pin resets the system here:
    listOfComputersAndGPIOPins={'101': 17,
                                '102': 27,
                                '103': 22,
                                '104': 23
                            }
    #code
    try:
        print(type(computerNumber))
        pinNumber = listOfComputersAndGPIOPins[computerNumber]
        print(type(pinNumber))
        GPIO.output(17, 1)
        print("didntFAil")
        sleep(1)
        GPIO.output(pinNumber, 0)       
    except:
        print("Failure in the restartComputer function")
        
def restartAll():

    """ This function attempts to restart all the computurs in grendel one."""

    for eachComputer in ["101","102","103","104"]:
        try:
            print("restarting computer "+listOfComputersAndGPIOPins[computerNumber])
            computerStartUpFunctions.restartComputer(eachComputer)
            sleep(10)
        except:
            print("Failure: Computer Number "+ str(eachComputer) +" failed to start at restart: All function")
            
    
    
