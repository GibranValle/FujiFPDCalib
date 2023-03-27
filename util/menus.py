import os
from calibrations.defectSolidCalib import defectSolidCalib
from calibrations.noExposureCalib import offsetCalib, defectCalib
from calibrations.pixelDefectCalibration import pixedDefectCalib
from calibrations.shadingCalibration import shadingCalib
from calibrations.uniformityCalibration import uniformityCalib
from calibrations.verification import mAVerification
from util.macros import startMouseCalib
from util.mouseKeyboard import openRequest, closeRequest


def mainMenu():
    print('FPD Calibration helper by Gibran Valle FFMX')
    print('Available emulator modes:')
    print(' 1) HandSwitch with Timer(HST)')
    print(' 2) HandSwitch Smart(HSS)')
    print(' 3) Mouse (M) [DEVELOPMENT]')
    print(' 4) HSS+M [DEVELOPMENT]')
    print(' 0) Exit')
    select = input('Selected option: ')
    return select


def handswitchMenu():
    print(' 1) Defect-solid\n 2) Pixel-defect\n 3) Shading\n 4) X-ray uniformity\n 5) mA Verification')
    print(' 0) Return to main menu')


def handswitchSelection(timer):
    selection = input('selected: ')
    os.system('cls')
    if selection == '1':
        defectSolidCalib(timer)
    elif selection == '2':
        pixedDefectCalib(timer)
    elif selection == '3':
        shadingCalib(timer)
    elif selection == '4':
        uniformityCalib(timer)
    elif selection == '5':
        mAVerification(timer)
    elif selection == '0':
        return


def mouseMenu():
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
    elif selection == '2':
        openRequest('MUTL')
    elif selection == '3':
        closeRequest('RUPCTOOLS')
    elif selection == '4':
        closeRequest('MUTL')
    elif selection == 'a':
        startMouseCalib('offset')
    elif selection == 'b':
        startMouseCalib('defect')
    elif selection == 'c':
        startMouseCalib('defect-solid')
    elif selection == 'd':
        startMouseCalib('pixel-defect')
    elif selection == 'e':
        startMouseCalib('shading')
    elif selection == 'f':
        startMouseCalib('uniformity')
    elif selection == '0':
        return
