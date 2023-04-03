import time

from calibrations.exposureCalib import initMessage, exposureMessage, endMessage
from util.delayManager import keyboardDelay
from util.readConfigFile import getMACalibDuration, getCountDown, getCalcTime
from util.serialCOM import communicate


def mAFullCalibration(timer):
    initMessage('mA full calibration', 20)
    exposureMessage(1, 1)
    if not communicate("T"):     # VERIFY CONNECTION BEFORE COUNTDOWN
        return

    print("\n>-- Exposure request accepted --< ")
    if timer:
        keyboardDelay(getCountDown(), 0, ' Starting exposure in: ')
    else:
        # TODO IMAGECOMPARATION
        pass

    if not communicate("L"):     # REQUEST FOR LONG EXPOSURE
        return

    if timer:
        keyboardDelay(getMACalibDuration(), 0, ' Under exposure... ')
    else:
        # TODO IMAGECOMPARATION
        pass

    print(" <-- Requesting end of exposure -->")
    if not communicate("X"):
        return print(" *** PLEASE END EXPOSURE MANUALLY *** ")

    print(" >-- Exposure done --< ")
    if timer:
        keyboardDelay(getCalcTime(), 0, ' Calculating: ')
    else:
        # TODO IMAGECOMPARATION
        pass

    endMessage()
