import pyautogui
import os

path = os.getcwd()


def genericCoordinates(name):
    confidence = 0.9
    try:
        x, y, w, h = pyautogui.locateOnScreen(f'{path}/img/{name}.png', confidence=confidence)
        return x, y, w, h
    except TypeError:
        return -1, -1, -1, -1


def genericCoordinatesCenter(name):
    confidence = 0.9
    if name == 'mutl/calibration_s':
        confidence = 0.55
    x, y = -1, -1
    try:
        x, y = pyautogui.locateCenterOnScreen(f'{path}/img/{name}.png', confidence=confidence)
        return x, y

    except TypeError:
        return x, y


# FF_tools
def isExposing():
    return genericCoordinatesCenter('ff/xray_exposing')


# AWS
def blockedIcon():
    return genericCoordinatesCenter('aws/xray_blocked')


def stdbyIcon():
    return genericCoordinatesCenter('aws/xray_standby')


def okExposure():
    return genericCoordinatesCenter('aws/ok')


def calib_button():
    return genericCoordinatesCenter('aws/calib_button')


def fieldCalib():
    return genericCoordinatesCenter('aws/fieldcalib_button')


# RUPCTOOL SCREEN
def MU0():
    x, y = genericCoordinatesCenter('ru/MU0')
    x1, y1 = genericCoordinatesCenter('ru/MU0_S')
    if x > 0 and y > 0:
        return x, y
    if x1 > 0 and y1 > 0:
        return x1, y1
    else:
        return -1, -1


def MCU0():
    x, y = genericCoordinatesCenter('ru/MCU0')
    x1, y1 = genericCoordinatesCenter('ru/MCU0_S')
    if x > 0 and y > 0:
        return x, y
    if x1 > 0 and y1 > 0:
        return x1, y1
    else:
        return -1, -1


def mutl():
    return genericCoordinatesCenter('ru/mutl')


def new():
    return genericCoordinatesCenter('ru/new')


def install():
    return genericCoordinatesCenter('ru/install')


# MUTL
def calibration():
    x0, y0, w, h = genericCoordinates('mutl/calibration_selected')
    if x0 and y0 > 0:
        x = x0 + w/2
        y = y0 + h/2
        return x, y
    x0, y0, w, h = genericCoordinates('mutl/calibration_unselected')
    if x0 and y0 > 0:
        x = x0 + 3*w/7
        y = y0 + h/2
        return x, y
    x0, y0, w, h = genericCoordinates('mutl/calibration_opt_selected')
    if x0 and y0 > 0:
        x = x0 + (2*w/5)
        y = y0 + h/2
        return x, y
    return -1, -1


def calibrationOptional():
    x0, y0, w, h = genericCoordinates('mutl/calibration_selected')
    if x0 and y0 > 0:
        x = x0 + 4*w/5
        y = y0 + h/2
        return x, y
    x0, y0, w, h = genericCoordinates('mutl/calibration_unselected')
    if x0 and y0 > 0:
        x = x0 + (4*w/5)
        y = y0 + h/2
        return x, y
    x0, y0, w, h = genericCoordinates('mutl/calibration_opt_selected')
    if x0 and y0 > 0:
        x = x0 + (4*w/5)
        y = y0 + h/2
        return x, y
    return -1, -1


def lastPage():
    # only left
    x0, y0, w, h = genericCoordinates('mutl/left_noright')
    y = y0 + h/2
    x = x0 + w/4
    return x, y


def firstPage():
    x0, y0, w, h = genericCoordinates('mutl/right_noleft')
    y = y0 + h/2
    x = x0 + (3*w/4)
    return x, y


def midPage(side):
    x0, y0, w, h = genericCoordinates('mutl/left_right')
    if side == 'left' and x0 > 0:
        y = y0 + h / 2
        x = x0 + w / 4
        return x, y
    if side == 'right' and x0 > 0:
        y = y0 + h / 2
        x = x0 + (3 * w / 4)
        return x, y


def left():
    x, y = lastPage()
    if x > 0 and y > 0:
        return x, y
    x, y = midPage('left')
    if x > 0 and y > 0:
        return x, y
    print('No icon found')
    return -1, -1


def right():
    x, y = firstPage()
    if x > 0 and y > 0:
        return x, y
    x, y = midPage('right')
    if x > 0 and y > 0:
        return x, y
    print('No icon found')
    return -1, -1


# CALIBRATION MENU
def offset():
    return genericCoordinatesCenter('mutl/calib_offset')


def defect():
    return genericCoordinatesCenter('mutl/calib_defect')


def defectSolid():
    return genericCoordinatesCenter('mutl/calib_defect_solid')


def defectSolidStereo():
    return genericCoordinatesCenter('mutl/calib_defect_solid_stereo')


def defectSolidBpy():
    return genericCoordinatesCenter('mutl/calib_defect_solid_bpy')


def defectSolidTomo():
    return genericCoordinatesCenter('mutl/calib_defect_solid_tomo')


def pixelDefect():
    return genericCoordinatesCenter('mutl/calib_pixel_defect')


def shading():
    return genericCoordinatesCenter('mutl/calib_shading')


def uniformity():
    return genericCoordinatesCenter('mutl/calib_uniformity')


def uniformityStereo():
    return genericCoordinatesCenter('mutl/calib_uniformity_stereo')


def uniformityBpy():
    return genericCoordinatesCenter('mutl/calib_uniformity_bpy')


def uniformityTomo():
    return genericCoordinatesCenter('mutl/calib_uniformity_tomo')


def uniformityES():
    return genericCoordinatesCenter('mutl/calib_uniformity_es')


def sensitivity():
    return genericCoordinatesCenter('mutl/calib_sensitivity')


