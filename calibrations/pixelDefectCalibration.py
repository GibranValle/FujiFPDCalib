from util.light import setLightDelay
from util.serialCOM import communicate


def pixedDefectCalib(exposures=1):
    print("Pixel defect calibration selected")
    print("Estimated waiting time: 5 mins")
    print(f"Exposures required: {exposures}")
    # exposures loop
    print(f"\nRequesting exposure 1 of {exposures}")
    comError = communicate("S")
    if comError:
        print("Communication error")
        return

    # wait 10 secs OR wait light to turn off
    setLightDelay("Under exposure...", 1, 10)

    print("\nRequesting end of exposure\n")
    comError = communicate("X")
    if comError:
        print("Communication error")
        return
    print("Exposure done")

    print("\nCalibration completed successfully please check AWS")
    print("----------------------------------------------------")
