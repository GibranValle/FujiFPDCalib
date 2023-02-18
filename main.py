# test started 29/01/2023
# final modification @ 14/02/2023
from helper import offsetCalib, defectCalib
from comHelper import mAVerification, uniformityCalib, shadingCalib, pixedDefectCalib, testCommunication
from comHelper import initSerial, ADCtest
import os
isRunning = True

while isRunning:
    print('\nAutomatic MG FPD Calibration script by Gibran Valle FFMX\n')
    print('Available options')
    print(' 1) Offset \n 2) Defect')
    print(' 3) Pixel-defect \n 4) Shading \n 5) X-ray uniformity')
    print(' 6) mA Verification')
    print(' 7) Test communication')
    print(' 8) ADC Reading TEST')
    print(' 0) Exit program\n')
    selection = input('selected: ')
    os.system('cls')
    arduino = initSerial()
    if selection == '1':
        offsetCalib()
    elif selection == '2':
        defectCalib()
    elif selection == '3':
        pixedDefectCalib(arduino)
    elif selection == '4':
        shadingCalib(arduino)
    elif selection == '5':
        uniformityCalib()
    elif selection == '6':
        mAVerification()
    elif selection == '7':
        testCommunication(arduino)
    elif selection == '8':
        ADCtest(arduino)
    elif selection == '0':
        isRunning = False
        arduino.close()
