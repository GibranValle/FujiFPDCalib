import time

from util.readConfigFile import getThreshold, getLowThreshold

THRESHOLD = getThreshold()
LOW_THRESHOLD = getLowThreshold()


def setLightDelay(init, final, lightWanted=True, sampling=4):
    counter = init
    offset = 1 if final > init else -1
    lightCount = 0
    darkCount = 0
    for i in range(init, final):
        avg = 0
        # TODO wait for end of exposure
        if (lightWanted and lightCount > 2) or (not lightWanted and darkCount > 2):
            print("\n\n ** MU0 IS READY TO CONTINUE... ABORTING COUNTDOWN **", end='')
            break

        for s in range(sampling):
            value = readADC()
            avg += value
            time.sleep(0.15)
        counter += offset
        avg = avg / sampling

        if avg > THRESHOLD:
            lightCount += 1
        elif LOW_THRESHOLD > avg > THRESHOLD:
            darkCount += 1
        else:
            print("\n ** AVG TOO LOW PLEASE VERIFY **")

        print(f"\rWaiting: {counter}s AVG:{avg} ON:{lightCount} OFF:{darkCount}", end='')
    print("\n")


def waitForReadySignal(init, final):
    setLightDelay(init, final, lightWanted=True)


def waitForDoneSignal(init, final):
    setLightDelay(init, final, lightWanted=False)