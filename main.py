# test started 29/01/2023
# final modification @ 20/02/2023
from calibrations.noExposureCalib import offsetCalib, defectCalib
from calibrations.pixelDefectCalibration import pixedDefectCalib
from calibrations.shadingCalibration import shadingCalib
from calibrations.uniformityCalibration import uniformityCalib
from util.serialCOM import initSerial
from calibrations.verification import mAVerification, testCommunication, ADCtest
import os

isRunning = True
while isRunning:
    print('\nAutomatic MG FPD Calibration script by Gibran Valle FFMX\n')
    print(' 1) Offset \n 2) Defect')
    print(' 3) Pixel-defect \n 4) Shading \n 5) X-ray uniformity')
    print(' 6) mA Verification \n 7) Test communication \n 8) ADC Reading TEST')
    print(' 0) Exit program\n')
    selection = input('selected: ')
    os.system('cls')
    arduino = initSerial()
    if selection == '1':
        offsetCalib(debug=1)
    elif selection == '2':
        defectCalib(debug=1)
    elif selection == '3':
        pixedDefectCalib(arduino)
    elif selection == '4':
        shadingCalib(arduino)
    elif selection == '5':
        uniformityCalib(arduino)
    elif selection == '6':
        mAVerification(arduino)
    elif selection == '7':
        testCommunication(arduino)
    elif selection == '8':
        ADCtest(arduino)
    elif selection == '0':
        isRunning = False
        arduino.close()
