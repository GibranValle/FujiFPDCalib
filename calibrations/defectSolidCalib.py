import threading

from util.compareImgs import waitForExposureReady, waitForExposureEnd
from util.macros import startMouseCalib
from util.serialCOM import communicate


def defectSolidCalib(exposures=1):
    print("Defect solid calibration selected")
    print("Estimated waiting time: 5 mins")
    # TODO MOUSE CALIB
    startMouseCalib('defect-solid')
    # wait 500 secs OR wait SS
    waitForExposureReady(0, 500)
    print(f"Exposures required: {exposures}")
    print(f"\n<-- Requesting exposure 1 of {exposures} -->\n")
    comError = communicate("S")
    if comError:
        return
    print(" ----- UNDER EXPOSURE ------\n")
    waitForExposureEnd(0, 10)

    print(" <-- Requesting end of exposure -->")
    comError = communicate("X")
    if comError:
        return
    print(" --> Exposure done <--")

    print("\nCalibration completed successfully please check AWS")
    print("----------------------------------------------------")
