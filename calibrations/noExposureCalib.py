import threading
import time

from readConfigFile import isDemoMode
from util.mouseKeyboard import openRUPcTools, openMUTLCalibMenu, runOffsetCalibration, runDefectCalibration, \
    closeMUTLCalibMenu, closeRUPcTools

isFinished = False
isDemo = isDemoMode()


def offsetCalib():
    global isFinished, isDemo
    print("Offset calibration selected")
    print("Estimated waiting time: 5 mins")
    print("Exposures required: 0")

    print("Open RUPcTools")
    if not isDemo:
        openRUPcTools()
    print("Open MUTL Calibration window")
    if not isDemo:
        openMUTLCalibMenu()
    print("Starting field calibration\n")
    if not isDemo:
        runOffsetCalibration()

    inputThread = threading.Thread(target=getInput)
    inputThread.start()
    count = 0
    while not isFinished:
        time.sleep(1)
        if count >= 500:
            isFinished = True
        print(f"\rWaited time in secs {count}", end='')
        count += 1

    print("\nClose MUTL Calibration window")
    if not isDemo:
        closeMUTLCalibMenu()
    print("Close RUPcTool")
    if not isDemo:
        closeRUPcTools()

    print("\n --Calibration complete-- \n")


def defectCalib():
    global isFinished, isDemo
    print("Defect calibration selected")
    print("Estimated waiting time: 5 mins")
    print("Exposures required: 0")

    print("Open RUPcTools")
    if not isDemo:
        openRUPcTools()
    print("Open MUTL Calibration window")
    if not isDemo:
        openMUTLCalibMenu()
    print("Starting field calibration\n")
    if not isDemo:
        runDefectCalibration()

    inputThread = threading.Thread(target=getInput)
    inputThread.start()
    count = 0
    while not isFinished:
        time.sleep(1)
        if count >= 500:
            isFinished = True
        print(f"\rWaited time in secs {count}", end='')
        count += 1

    print("\nClose MUTL Calibration window")
    if not isDemo:
        closeMUTLCalibMenu()
    print("Close RUPcTool")
    if not isDemo:
        closeRUPcTools()

    print("\n --Calibration complete-- \n")


def getInput():
    global isFinished
    selection = input(" --PRESS ENTER TO QUIT-- \n\n")
    # thread doesn't continue until key is pressed
    isFinished = True

