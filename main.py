# test started 29/01/2023
# final modification @ 28/02/2023
import time
import os
import threading

from calibrations.defectSolidCalib import defectSolidCalib
from calibrations.noExposureCalib import offsetCalib, defectCalib
from calibrations.pixelDefectCalibration import pixedDefectCalib
from calibrations.shadingCalibration import shadingCalib
from calibrations.uniformityCalibration import uniformityCalib
from calibrations.verification import mAVerification, ADCtest, testCommunication
from util.serialCOM import startListening, endListening


def main():
    # use threading for SERIAL COMMUNICATION WITH ARDUINO
    serialThread = threading.Thread(target=startListening)
    serialThread.start()
    print("OPENING SERIAL PORT... PLEASE WAIT")
    os.system('cls')
    time.sleep(1.5)
    print(" ** PLEASE CLOSE ALL WINDOWS OPENED ** ")

    isRunning = True
    while isRunning:
        print('\nAutomatic MG FPD Calibration script by Gibran Valle FFMX\n')
        print(' 1) Offset \n 2) Defect')
        print(' 3) Defect-solid \n 4) Pixel-defect \n 5) Shading \n 6) X-ray uniformity')
        print(' 7) mA Verification \n 8) Test communication \n 9) ADC Reading TEST')
        print(' 0) Exit program\n')
        try:
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
                ADCtest()
            elif selection == '0':
                isRunning = False
                endListening()
        except KeyboardInterrupt:
            print("FINISHING...")
            isRunning = False
            endListening()


if __name__ == '__main__':
    main()
