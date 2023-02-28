# test started 29/01/2023
# final modification @ 20/02/2023
from calibrations.noExposureCalib import offsetCalib, defectCalib
from calibrations.pixelDefectCalibration import pixedDefectCalib
from calibrations.shadingCalibration import shadingCalib
from calibrations.uniformityCalibration import uniformityCalib
from calibrations.verification import mAVerification, ADCtest, testCommunication
import os
import threading
from util.serialCOM import startListening

# use threading for SERIAL COMMUNICATION WITH ARDUINO
serialThread = threading.Thread(target=startListening)
serialThread.start()

# use infinite loop for interaction
isRunning = True

while isRunning:
    print('\nAutomatic MG FPD Calibration script by Gibran Valle FFMX\n')
    print(' 1) Offset \n 2) Defect')
    print(' 3) Pixel-defect \n 4) Shading \n 5) X-ray uniformity')
    print(' 6) mA Verification \n 7) Test communication \n 8) ADC Reading TEST')
    print(' 0) Exit program\n')
    selection = input('selected: ')
    os.system('cls')
    if selection == '1':
        offsetCalib()
    elif selection == '2':
        defectCalib()
    elif selection == '3':
        pixedDefectCalib()
    elif selection == '4':
        shadingCalib()
    elif selection == '5':
        uniformityCalib()
    elif selection == '6':
        mAVerification()
    elif selection == '7':
        testCommunication()
    elif selection == '8':
        ADCtest()
    elif selection == '0':
        isRunning = False
