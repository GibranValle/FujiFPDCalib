import time
import threading
from util.mouseKeyboard import openRUPcTools, openMUTLCalibMenu, runOffsetCalibration, runDefectCalibration, \
    closeMUTLCalibMenu, closeRUPcTools

isFinished = False


def offsetCalib(debug=0):
    global isFinished
    print("Offset calibration selected")
    print("Estimated waiting time: 5 mins")
    print("Exposures required: 0")

    print("Open RUPcTools")
    if debug:
        openRUPcTools()
    print("Open MUTL Calibration window")
    if debug:
        openMUTLCalibMenu()
    print("Starting field calibration\n")
    if debug:
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
    if debug:
        closeMUTLCalibMenu()
    print("Close RUPcTool")
    if debug:
        closeRUPcTools()

    print("\n --Calibration complete-- \n")


def defectCalib(debug=0):
    global isFinished
    print("Defect calibration selected")
    print("Estimated waiting time: 5 mins")
    print("Exposures required: 0")

    print("Open RUPcTools")
    if debug:
        openRUPcTools()
    print("Open MUTL Calibration window")
    if debug:
        openMUTLCalibMenu()
    print("Starting field calibration\n")
    if debug:
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
    if debug:
        closeMUTLCalibMenu()
    print("Close RUPcTool")
    if debug:
        closeRUPcTools()

    print("\n --Calibration complete-- \n")


def getInput():
    global isFinished
    selection = input(" --PRESS ANY ENTER TO QUIT-- \n\n")
    # thread doesn't continue until key is pressed
    isFinished = True

