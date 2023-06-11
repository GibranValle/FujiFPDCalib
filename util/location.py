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
        return x, y


# FF_tools
def isExposing():
    return genericCoordinates('ff/xray_exposing')


# AWS
def blockedIcon():
    return genericCoordinates('aws/xray_blocked')


def stdbyIcon():
    return genericCoordinates('aws/xray_standby')


def okExposure():
    return genericCoordinates('aws/ok')


def calib_button():
    return genericCoordinates('aws/calib_button')


def fieldCalib():
    return genericCoordinates('aws/fieldcalib_button')


# RUPCTOOL SCREEN
def MU0():
    return genericCoordinates('ru/MU0')


def MCU0():
    return genericCoordinates('ru/MCU0')


def new():
    return genericCoordinates('ru/new')


def install():
    return genericCoordinates('ru/install')


# MUTL
def calibration():
    return genericCoordinates('mutl/calibration')


def calibrationOptional():
    return genericCoordinates('mutl/calibration_option')


def left():
    return genericCoordinates('mutl/left')


def right():
    return genericCoordinates('mutl/right')


#CALIBRATION MENU
def offset():
    return genericCoordinates('mutl/calib_offset')


def defect():
    return genericCoordinates('mutl/calib_defect')


def defectSolid():
    return genericCoordinates('mutl/calib_defect_solid')


def defectSolidStereo():
    return genericCoordinates('mutl/calib_defect_solid_stereo')


def defectSolidBpy():
    return genericCoordinates('mutl/calib_defect_solid_bpy')


def defectSolidTomo():
    return genericCoordinates('mutl/calib_defect_solid_tomo')


def pixelDefect():
    return genericCoordinates('mutl/calib_pixel_defect')


def shading():
    return genericCoordinates('mutl/calib_shading')


def uniformity():
    return genericCoordinates('mutl/calib_uniformity')


def uniformityStereo():
    return genericCoordinates('mutl/calib_uniformity_stereo')


def uniformityBpy():
    return genericCoordinates('mutl/calib_uniformity_bpy')


def uniformityTomo():
    return genericCoordinates('mutl/calib_uniformity_tomo')


def uniformityES():
    return genericCoordinates('mutl/calib_uniformity_es')


def sensitivity():
    return genericCoordinates('mutl/calib_sensitivity')


