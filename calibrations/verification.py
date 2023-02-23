import threading
import time

from readConfigFile import getUltraLong, getCountDown
from util.serialCOM import communicate, lightValue
from util.TimerDelay import setTimerDelay, startTimerDelay, endTimerDelay


def mAVerification(waitTime=getUltraLong()):
    print("mA verification selected")
    print("1 LONG Exposure required")
    print("Estimated duration of exposure: 5min")
    print(" <-- Requesting for exposure -->")
    # VERIFY CONNECTION BEFORE COUNTDOWN
    comError = communicate("T", "T")
    if comError:
        return print(" *** COMMUNICATION ERROR ***")
    print(" >-- Exposure request accepted --< ")

    setTimerDelay("STARTING EXPOSURE IN: ", initValue=getCountDown(), finalValue=0)
    startTimerDelay()

    # REQUEST FOR LONG EXPOSURE NOW
    comError = communicate("L", "L")
    if comError:
        return print(" *** COMMUNICATION ERROR ***")
    print("\nPerforming LONG EXPOSURE...")

    # thread for finish task
    inputThread = threading.Thread(target=abortExposure)
    inputThread.start()

    # timer for duration of exposure
    setTimerDelay("\r !! UNDER EXPOSURE: ", initValue=0, finalValue=waitTime)
    startTimerDelay()

    print(" <-- Requesting end of exposure -->")
    comError = communicate("X", "X")
    if comError:
        print(" *** PLEASE END EXPOSURE MANUALLY *** ")
        return print(" *** COMMUNICATION ERROR ***")
    print(" >-- Exposure done --< ")


def testCommunication():
    print("Communication test selected")
    comError = communicate("T", "T")
    if comError:
        print("Communication error")
        return
    print(" >-- Communication correct <--")


def ADCtest(samples=20):
    print("ADC Reading test selected")
    for i in range(samples):
        value = lightValue(1)
        print("Value: "+str(value))
        time.sleep(0.25)


def abortExposure():
    selection = input(" \n------- PRESS ENTER TO SKIP -------- \n")
    # thread doesn't continue until key is pressed
    endTimerDelay()
