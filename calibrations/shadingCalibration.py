from util.compareImgs import waitForExposureReady, waitForExposureEnd
from util.macros import startMouseCalib
from util.readConfigFile import isAutoMouse
from util.serialCOM import communicate


def shadingCalib(exposures=44):
    print("Shading calibration selected")
    print("Estimated waiting time: 30 mins")
    if isAutoMouse():
        startMouseCalib('shading')
    print("Exposures required: "+str(exposures))
    if isAutoMouse():
        waitForExposureReady(0, 500)
    # exposures loop
    for i in range(1, exposures+1):
        print(f"\nRequesting exposure {i} of {exposures}")
        comError = communicate("S")
        if comError:
            return

        waitForExposureEnd(0, 5)

        print("\nRequesting end of exposure\n")
        comError = communicate("X")
        if comError:
            return
        print("Exposure done")

        # wait 15 secs or wait light to turn ON
        waitForExposureReady(0, 30)

    print("\nCalibration completed successfully please check AWS")
    print("----------------------------------------------------")
