import time

from readConfigFile import getThreshold
from util.serialCOM import readADC


def lightDelayThread(init, final, sampling=4):
    counter = init
    offset = 1 if final > init else -1
    lightCount = 0
    darkCount = 0
    for i in range(init, final):
        avg = 0
        for s in range(sampling):
            value = readADC()
            avg += value
            time.sleep(0.15)
        counter += offset
        avg = avg / sampling

        if lightCount > 2:
            print("\n\n ** MU0 IS READY TO CONTINUE... ABORTING COUNTDOWN **", end='')
            break

        if avg > getThreshold():
            lightCount += 1
        else:
            darkCount += 1
        print(f"\rWaiting: {counter}s AVG:{avg} ON:{lightCount} OFF:{darkCount}", end='')
    print("\n")


def setLightDelay(init, final):
    lightDelayThread(init, final)
