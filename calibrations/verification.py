import time

from readConfigFile import getUltraLong, getMaxCount, getCountDown
from util.serialCOM import communicate, lightStatus, lightValue


def mAVerification(arduino, waitTime=getCountDown()):
    print("mA verification selected")
    print("1 LONG Exposure required")
    print("Estimated duration of exposure 5min")
    print("Requesting for exposure...")
    # VERIFY CONNECTION BEFORE COUNTDOWN
    dataLost = communicate("T", "T", 5, arduino)
    if dataLost:
        print("Communication error")
        return
    print("Exposure request accepted")
    for i in reversed(range(1, waitTime)):
        print("\rStarting LONG exposure in " + str(i) + " secs...", end='')
        time.sleep(1)
    # REQUEST FOR LONG EXPOSURE NOW
    communicate("L", "L", 5, arduino)
    print("\nPerforming LONG EXPOSURE...")
    count = 0
    for j in range(1, getUltraLong()):

        if count > getMaxCount():
            print("Request to finish exposure before countdown")
            dataLost = communicate("X", "X", 5, arduino)
            if not dataLost:
                break
        status = lightStatus("M", 1000, 1, arduino)

        if status == 'Off':
            print("\rSTAND BY", end='')
            count += 1
        else:
            print("\rUNDER EXPOSURE " + str(j) + " s", end='')

    print("Exposure done")


def testCommunication(arduino):
    print("Communication test selected")
    dataLost = communicate("T", "T", 5, arduino)
    if not dataLost:
        print("Communication correct")
        return
    print("Communication error")


def ADCtest(arduino):
    print("ADC Reading test selected")
    value = lightValue("M", 1, arduino)
    print("Value: "+str(value))
