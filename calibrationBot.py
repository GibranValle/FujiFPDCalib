# test started 29/01/2023
# final modification @ 19/03/2023
import time
import os
import threading

from calibrations.defectSolidCalib import defectSolidCalib
from calibrations.noExposureCalib import offsetCalib, defectCalib
from calibrations.pixelDefectCalibration import pixedDefectCalib
from calibrations.shadingCalibration import shadingCalib
from calibrations.uniformityCalibration import uniformityCalib
from calibrations.verification import mAVerification, testCommunication
from util.mouseKeyboard import openRequest, closeRequest
from util.readConfigFile import setAutoMouse, unsetAutoMouse, setSkipSerial, unsetSkipSerial
from util.serialCOM import startListening, endListening, getSerialError
enableAutoMenu = False
isRunning = True


# ------------------------------------------- MAIN -------------------------------------------------
def main():
    global enableAutoMenu, isRunning
    print("OPENING SERIAL PORT... PLEASE WAIT")
    # use threading for SERIAL COMMUNICATION WITH ARDUINO
    serialThread = threading.Thread(target=startListening)
    serialThread.start()
    os.system('cls')
    if getSerialError():
        print(' ** Verify connection with handswitch emulator **')
        return
    while isRunning:
        if getSerialError():
            print(' ** Verify connection with handswitch emulator **')
            break

        if not enableAutoMenu:
            mainMenu()
            try:
                options()
            except KeyboardInterrupt:
                print("FINISHING...")
                isRunning = False
                endListening()

        else:
            print(enableAutoMenu)
            autoMenu()
            try:
                autoOptions()
            except KeyboardInterrupt:
                print("FINISHING...")
# ------------------------------------------- MAIN -------------------------------------------------


def autoMenu():
    print('\nAutomatization keyboard and mouse script testing menu\n')
    print(' 1) Open RUPCTools')
    print(' 2) Close RUPCTools')
    print(' 3) Open MUTL')
    print(' 4) Close MUTL')
    print(' 5) set Automatic mouse mode')
    print(' 6) unset Automatic mouse mode')
    print(' 7) set error if COM not open')
    print(' 8) unset error if COM not open')
    print(' a) Start FPD - Offset Calibration')
    print(' b) Start FPD - Defect Calibration')
    print(' c) Start FPD - Defect solid Calibration')
    print(' d) Start FPD - Pixel defect Calibration')
    print(' e) Start FPD - Shading Calibration')
    print(' f) Start FPD - Uniformity Calibration')
    print(' 0) Return to main menu\n')


def autoOptions():
    global enableAutoMenu
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
    elif selection == '5':
        setAutoMouse()
    elif selection == '6':
        unsetAutoMouse()
    elif selection == '7':
        unsetSkipSerial()
    elif selection == '8':
        setSkipSerial()
    elif selection == '0':
        enableAutoMenu = False


def mainMenu():
    print('\nAutomatic MG FPD Calibration script by Gibran Valle FFMX\n')
    print(' 1) Offset \n 2) Defect')
    print(' 3) Defect-solid\n 4) Pixel-defect \n 5) Shading \n 6) X-ray uniformity')
    print(' 7) mA Verification \n 8) Test communication')
    print(' 9) Enter Automatization Menu')
    print(' 0) Exit program\n')


def options():
    global enableAutoMenu, isRunning
    selection = input('selected: ')
    os.system('cls')
    if selection == '1':
        offsetCalib()
    elif selection == '2':
        defectCalib()
    elif selection == '3':
        defectSolidCalib()
    elif selection == '4':
        pixedDefectCalib()
    elif selection == '5':
        shadingCalib()
    elif selection == '6':
        uniformityCalib()
    elif selection == '7':
        mAVerification()
    elif selection == '8':
        testCommunication()
    elif selection == '9':
        enableAutoMenu = True
    elif selection == '0':
        isRunning = False
        endListening()


if __name__ == '__main__':
    main()
