import time

from util.delayManager import keyboardDelay, waitTillEndYellow
from util.readConfigFile import getMACalibDuration, getCountDown, getCalcTime
from util.serialCOM import communicate


def mAFullCalibration(mouse):
    print(f"ma full calibration selected")
    print(f"Estimated waiting time: 20 mins")
    print("----------------------------------------------------")
    print(f"<-- Requesting exposure 1 of 1 -->")
    if not communicate("T"):     # VERIFY CONNECTION BEFORE COUNTDOWN
        return
    print("\n>-- Exposure request accepted --< ")
    keyboardDelay(getCountDown(), 0, ' Starting exposure in: ')
    if not communicate("L"):     # REQUEST FOR LONG EXPOSURE
        return
    time = waitTillEndYellow(getMACalibDuration(), 0)
    print(" <-- Requesting end of exposure -->")
    if not communicate("X"):
        return
    print(" >-- Exposure done --< ")
    keyboardDelay(getCalcTime(), 0, ' Calculating: ')
