import threading

from util.LightDelay import setLightDelay
from util.serialCOM import communicate


def pixedDefectCalib(exposures=1):
    print("Pixel defect calibration selected")
    print("Estimated waiting time: 5 mins")
    print(f"Exposures required: {exposures}")
    # exposures loop
    print(f"\n<-- Requesting exposure 1 of {exposures} -->\n")
    comError = communicate("S")
    if comError:
        return

    # wait 10 secs OR wait light to turn off
    setLightDelay(0, 10)

    print(" <-- Requesting end of exposure -->")
    comError = communicate("X")
    if comError:
        return
    print(" --> Exposure done <--")

    print("\nCalibration completed successfully please check AWS")
    print("----------------------------------------------------")
