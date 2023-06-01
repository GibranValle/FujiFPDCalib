import pyautogui
import time
from typing import Literal
from pyautogui import moveTo

from calibrations.variables import CALIB_FPD, OFFSET, DEFECT, FIELD_CALIBRATION, MUTL_CALIBRATION, RIGHT_OPTIONS, \
    LEFT_OPTIONS, MUTL_CALIBRATION_CLOSE, DEFECT_SOLID, PIXEL_DEFECT, SHADING, UNIFORMITY, RUPCTOOL_DIR, RUPCTOOL_EXE, \
    RUPCTOOL_CLOSE, MCU0, MUTL
from shell.processRunning import process_exists
from shell.activeWindow import getWindowName
_TYPES = Literal["RUPCTOOLS", "MUTL"]


def moveCursorAndClick(coordinates, d=1):
    x, y = coordinates
    time.sleep(.4)
    pyautogui.moveTo(x, y, duration=d)
    time.sleep(.4)
    pyautogui.click(x, y)


def changeTab(presses=1):
    pyautogui.keyDown("altleft")
    time.sleep(.2)
    pyautogui.press("tab", presses=presses)
    time.sleep(.2)
    pyautogui.keyUp('alt')


def typeTextEnter(string):
    # pyautogui.typewrite("rupctool")
    pyautogui.typewrite(string)
    time.sleep(.4)
    pyautogui.typewrite(["enter"])
    time.sleep(.4)


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
        time.sleep(.4)
        if i > 12:
            print(' ** CANNOT FIND OPEN PROGRAM PLEASE CONTACT SUPPORT **')
            return
    return


# ---------------- comple


def openRequest(appName: _TYPES):
    if appName == 'RUPCTOOLS':
        if process_exists('RuPcTool.exe'):
            look4Window('RU')
        openRUPcTools()

    if appName == 'MUTL':
        if process_exists('MUTL.exe'):
            look4Window('MUTL')
        openMUTLCalibMenu()


def closeRequest(appName: _TYPES):
    if appName == 'RUPCTOOLS':
        if process_exists('RuPcTool.exe'):
            look4Window('RU')
            moveCursorAndClick(RUPCTOOL_CLOSE)
            return
        print('RuPcTool.exe not open')

    if appName == 'MUTL':
        if process_exists('MUTL.exe'):
            look4Window('MUTL')
            moveCursorAndClick(MUTL_CALIBRATION_CLOSE)
            return
        print('MUTL.exe not open')


def openRUPcTools():
    pyautogui.typewrite(["win"])
    time.sleep(.4)
    typeTextEnter("cmd")
    time.sleep(.4)
    typeTextEnter(RUPCTOOL_DIR)
    time.sleep(.4)
    typeTextEnter(RUPCTOOL_EXE)
    time.sleep(.4)
    look4Window('cmd')
    time.sleep(.4)
    typeTextEnter("exit")


def openMUTLCalibMenu():
    moveCursorAndClick(MCU0)
    moveCursorAndClick(MUTL)
    moveCursorAndClick(RIGHT_OPTIONS)
    moveCursorAndClick(MUTL_CALIBRATION)


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
