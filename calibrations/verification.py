import threading
import time

from readConfigFile import getUltraLong, getMaxCount, getCountDown
from util.serialCOM import communicate, isLightOn, lightValue

isFinished = False


def mAVerification(arduino, waitTime=getCountDown()):
    print("mA verification selected")
    print("1 LONG Exposure required")
    print("Estimated duration of exposure 5min")
    print("Requesting for exposure...")
    # VERIFY CONNECTION BEFORE COUNTDOWN
    dataLost = communicate("T", "T", 1, arduino)
    if dataLost:
        print("Communication error")
        return
    print("Exposure request accepted")
    for i in reversed(range(1, waitTime+1)):
        print("\rStarting LONG exposure in " + str(i) + " secs...", end='')
        time.sleep(1)
    # REQUEST FOR LONG EXPOSURE NOW
    communicate("L", "L", 5, arduino)
    print("\nPerforming LONG EXPOSURE...")
    inputThread = threading.Thread(target=getInput)
    inputThread.start()
    for j in range(1, getUltraLong()):
        if isFinished:
            break
        print("\rUNDER EXPOSURE " + str(j) + " s", end='')
        time.sleep(1)
    dataLost = communicate("X", "X", 1, arduino)
    if dataLost:
        print("Communication error")
        print(" -- PLEASE END EXPOSURE MANUALLY --")
        return
    print("Exposure done")


def testCommunication(arduino):
    print("Communication test selected")
    dataLost = communicate("T", "T", 1, arduino)
    if not dataLost:
        print("Communication correct")
        return
    print("Communication error")


def ADCtest(arduino, samples=20):
    print("ADC Reading test selected")
    for i in range(samples):
        value = lightValue(1, arduino)
        print("Value: "+str(value))
        time.sleep(0.25)


def getInput():
    global isFinished
    selection = input(" --PRESS ENTER TO SKIP-- \n")
    # thread doesn't continue until key is pressed
    isFinished = True

