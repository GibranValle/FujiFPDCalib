import threading

from util.compareImgs import waitForExposureReady, waitForExposureEnd
from util.serialCOM import communicate


def pixedDefectCalib(exposures=1):
    print("Pixel defect calibration selected")
    print("Estimated waiting time: 5 mins")
    # wait 500 secs OR wait light
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
