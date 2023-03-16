# test started 29/01/2023
# final modification @ 28/02/2023
import time
import os
import threading

from calibrations.noExposureCalib import offsetCalib, defectCalib
from calibrations.pixelDefectCalibration import pixedDefectCalib
from calibrations.shadingCalibration import shadingCalib
from calibrations.uniformityCalibration import uniformityCalib
from calibrations.verification import mAVerification, testCommunication
from util.compareImgs import scanXRayIcon
from util.serialCOM import startListening, endListening, getSerialError


def main():
    # use threading for SERIAL COMMUNICATION WITH ARDUINO
    serialThread = threading.Thread(target=startListening)
    serialThread.start()
    print("OPENING SERIAL PORT... PLEASE WAIT")
    os.system('cls')
    time.sleep(1.5)
    if getSerialError():
        print(' ** Verify connection with handswitch emulator **')
        return
    isRunning = True
    while isRunning:
        if getSerialError():
            print(' ** Verify connection with handswitch emulator **')
            break
        print('\nAutomatic MG FPD Calibration script by Gibran Valle FFMX\n')
        print(' 1) Offset \n 2) Defect')
        print(' 3) Pixel-defect \n 4) Shading \n 5) X-ray uniformity')
        print(' 6) mA Verification \n 7) Test communication')
        print(' 9) SS Test')
        print(' 0) Exit program\n')
        try:
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
            elif selection == '9':
                scanXRayIcon()
            elif selection == '0':
                isRunning = False
                endListening()
        except KeyboardInterrupt:
            print("FINISHING...")
            isRunning = False
            endListening()


if __name__ == '__main__':
    main()
