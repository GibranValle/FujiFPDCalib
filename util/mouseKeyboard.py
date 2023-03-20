import pyautogui
import time
from typing import Literal

from calibrations.variables import CALIB_FPD, OFFSET, DEFECT, FIELD_CALIBRATION, MUTL_CALIBRATION, RIGHT_OPTIONS, \
    LEFT_OPTIONS, MUTL_CALIBRATION_CLOSE, DEFECT_SOLID, PIXEL_DEFECT, SHADING, UNIFORMITY, RUPCTOOL_DIR, RUPCTOOL_EXE, \
    RUPCTOOL_CLOSE, MCU0, MUTL
from shell.processRunning import process_exists
from shell.activeWindow import getWindowName
_TYPES = Literal["RUPCTOOLS", "MUTL"]


def moveCursorAndClick(x, y, d=1):
    # print(pyautogui.size())
    pyautogui.moveTo(x, y, duration=d)
    pyautogui.click(x, y)
    time.sleep(.2)


def changeTab(presses=1):
    pyautogui.keyDown("altleft")
    time.sleep(.2)
    pyautogui.press("tab", presses=presses)
    time.sleep(.2)
    pyautogui.keyUp('alt')


def typeTextEnter(string):
    # pyautogui.typewrite("rupctool")
    pyautogui.typewrite(string)
    time.sleep(0.2)
    pyautogui.typewrite(["enter"])
    time.sleep(0.2)


def startFDPOptionCalib():
    moveCursorAndClick(CALIB_FPD)
    moveCursorAndClick(CALIB_FPD)
    moveCursorAndClick(FIELD_CALIBRATION)


def look4Window(windowName):
    index = getWindowName().find(windowName)
    i = 0
    while index < 0:
        print(getWindowName())
        i += 1
        changeTab(i)
        index = getWindowName().find(windowName)
        time.sleep(0.1)
        if i > 12:
            print(' ** CANNOT FIND OPEN PROGRAM PLEASE CONTACT SUPPORT **')
            return
    return


# ---------------- comple


def openRequest(appName: _TYPES):
    if appName == 'RUPCTOOLS':
        if process_exists('rupc'):
            look4Window('RU')
        openRUPcTools()

    if appName == 'MUTL':
        if process_exists('mutl'):
            look4Window('MUTL')
        openMUTLCalibMenu()


def closeRequest(appName: _TYPES):
    if appName == 'RUPCTOOLS':
        if process_exists('rupc'):
            look4Window('RU')
            closeRUPcTools()

    if appName == 'MUTL':
        if process_exists('mutl'):
            look4Window('MUTL')
            closeMUTLCalibMenu()


def openRUPcTools():
    pyautogui.typewrite(["win"])
    time.sleep(0.2)
    typeTextEnter("cmd")
    time.sleep(0.2)
    typeTextEnter(RUPCTOOL_DIR)
    time.sleep(0.2)
    typeTextEnter(RUPCTOOL_EXE)


def closeRUPcTools():
    moveCursorAndClick(RUPCTOOL_CLOSE)


def openMUTLCalibMenu():
    moveCursorAndClick(MCU0)
    moveCursorAndClick(MUTL)
    moveCursorAndClick(RIGHT_OPTIONS)
    moveCursorAndClick(MUTL_CALIBRATION)


def closeMUTLCalibMenu():
    moveCursorAndClick(MUTL_CALIBRATION_CLOSE)


def selectCalibMUTL():
    moveCursorAndClick(LEFT_OPTIONS)
    moveCursorAndClick(LEFT_OPTIONS)
    moveCursorAndClick(RIGHT_OPTIONS)
    moveCursorAndClick(MUTL_CALIBRATION)


def clickOffsetCalibration():
    moveCursorAndClick(OFFSET)
    startFDPOptionCalib()


def clickDefectCalibration():
    moveCursorAndClick(DEFECT)
    startFDPOptionCalib()


def clickDefectSolidCalibration():
    moveCursorAndClick(DEFECT_SOLID)
    startFDPOptionCalib()


def clickPixelDefectCalibration():
    moveCursorAndClick(PIXEL_DEFECT)
    startFDPOptionCalib()


def clickShadingCalibration():
    moveCursorAndClick(SHADING)
    startFDPOptionCalib()


def clickUniformityCalibration():
    moveCursorAndClick(UNIFORMITY)
    startFDPOptionCalib()
