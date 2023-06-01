import pyautogui
import os

path = os.getcwd()
confidence = 0.9


def genericCoordinates(name):
    global confidence
    x, y = -1, -1
    try:
        x, y = pyautogui.locateCenterOnScreen(f'{path}/img/{name}.png', confidence=confidence)
        return x, y

    except TypeError:
        print('Icon not found on screen')
        return x, y


# STUDY
def isBlocked():
    return genericCoordinates('xray_blocked')


def isExposing():
    return genericCoordinates('xray_exposing')


def isStandby():
    return genericCoordinates('xray_standby')


def okExposure():
    return genericCoordinates('ok')


def calib_button():
    return genericCoordinates('calib_button')


def fieldCalib():
    return genericCoordinates('fieldcalib_button')


# RUPCTOOL SCREEN
def MU0():
    return genericCoordinates('MU0')


def MCU0():
    return genericCoordinates('MCU0')


def new():
    return genericCoordinates('new')


def install():
    return genericCoordinates('install')


# MUTL
def calibration():
    return genericCoordinates('calibration')


def calibrationOptional():
    return genericCoordinates('calibration_option')


def left():
    return genericCoordinates('left')


def right():
    return genericCoordinates('right')


#CALIBRATION MENU
def offset():
    return genericCoordinates('calib_offset')


def defect():
    return genericCoordinates('calib_defect')


def defectSolid():
    return genericCoordinates('calib_defect_solid')


def pixelDefect():
    return genericCoordinates('calib_pixel_defect')


def shading():
    return genericCoordinates('calib_shading')


def uniformity():
    return genericCoordinates('calib_uniformity')


def sensitivity():
    return genericCoordinates('calib_sensitivity')


