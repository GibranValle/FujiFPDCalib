import os

from calibrations.exposureCalibration import defectSolidCalib, pixedDefectCalib, shadingCalib, uniformityCalib
from calibrations.maFullCalib import mAFullCalibration
from util.macros import startMouseCalib
from util.mouseKeyboard import openRequest, closeRequest


def mainMenu():
    print('FPD Calibration helper by Gibran Valle FFMX')
    print('Available emulator modes:')
    print(' 1) HandSwitch')
    print(' 2) Mouse [UNDER DEVELOPMENT]')
    print(' 3) HSS+M [UNDER DEVELOPMENT]')
    print(' 0) Exit')
    select = input('Selected option: ')
    return select


def offlineMenu():
    print('FPD Calibration helper by Gibran Valle FFMX [OFFLINE MODE]')
    print('Available emulator modes:')
    print(' 1) Mouse (M) [DEVELOPMENT]')
    print(' 0) Exit')
    select = input('Selected option: ')
    return select


def handswitchMenu():
    print('Calibration options')
    print(' 1) Defect-solid\n 2) Pixel-defect\n 3) Shading\n 4) X-ray uniformity\n 5) mA Full calibration')
    print(' 0) Return to main menu')


def handswitchSelection(mouse=False):
    selection = input('selected: ')
    os.system('cls')
    if selection == '1':
        defectSolidCalib(mouse)
        return True
    elif selection == '2':
        pixedDefectCalib(mouse)
        return True
    elif selection == '3':
        shadingCalib(mouse)
        return True
    elif selection == '4':
        uniformityCalib(mouse)
        return True
    elif selection == '5':
        mAFullCalibration(mouse)
        return True
    elif selection == '0':
        return False


def mouseMenu():
    print('Mouse options')
    print(' 1) Open RUPCTools')
    print(' 2) Close RUPCTools')
    print(' 3) Open MUTL')
    print(' 4) Close MUTL')
    print(' a) Select Offset Calibration')
    print(' b) Select Defect Calibration')
    print(' c) Select Defect solid Calibration')
    print(' d) Select Pixel defect Calibration')
    print(' e) Select Shading Calibration')
    print(' f) Select Uniformity Calibration')
    print(' 0) Return to main menu\n')


def mouseOptions():
    selection = input('selected: ')
    os.system('cls')
    if selection == '1':
        openRequest('RUPCTOOLS')
        return True
    elif selection == '2':
        openRequest('MUTL')
        return True
    elif selection == '3':
        closeRequest('RUPCTOOLS')
        return True
    elif selection == '4':
        closeRequest('MUTL')
        return True
    elif selection == 'a':
        startMouseCalib('offset')
        return True
    elif selection == 'b':
        startMouseCalib('defect')
        return True
    elif selection == 'c':
        startMouseCalib('defect-solid')
        return True
    elif selection == 'd':
        startMouseCalib('pixel-defect')
        return True
    elif selection == 'e':
        startMouseCalib('shading')
        return True
    elif selection == 'f':
        startMouseCalib('uniformity')
        return True
    elif selection == '0':
        return False




