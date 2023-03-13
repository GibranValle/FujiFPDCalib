import threading
import time

isFinished = False


def offsetCalib():
    global isFinished
    print("Offset calibration selected")
    print("Estimated waiting time: 7 mins")
    print("Exposures required: 0")
    print("Starting offset calibration\n")
    starMouseCalib('offset')

    inputThread = threading.Thread(target=getInput)
    inputThread.start()
    count = 0
    while not isFinished:
        time.sleep(1)
        if count >= 500:
            isFinished = True
        print(f"\rWaited time in secs {count}", end='')
        count += 1
    print("\n --Calibration complete-- \n")


def defectCalib():
    global isFinished
    print("Defect calibration selected")
    print("Estimated waiting time: 7 mins")
    print("Exposures required: 0")
    print("Starting offset calibration\n")
    starMouseCalib('defect')

    inputThread = threading.Thread(target=getInput)
    inputThread.start()
    count = 0
    while not isFinished:
        time.sleep(1)
        if count >= 500:
            isFinished = True
        print(f"\rWaited time in secs {count}", end='')
        count += 1
    print("\n --Calibration complete-- \n")


def getInput():
    global isFinished
    selection = input(" --PRESS ENTER TO QUIT-- \n\n")
    # thread doesn't continue until key is pressed
    isFinished = True

