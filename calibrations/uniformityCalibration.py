import time

from util.LightDelay import waitForDoneSignal, waitForReadySignal
from util.compareImgs import waitForExposureEnd, waitForExposureReady
from util.serialCOM import communicate


def uniformityCalib(exposures=7):
    print("Uniformity calibration selected")
    print("Estimated waiting time: 10 mins")
    print("Exposures required: "+str(exposures))
    waitForExposureReady(0, 25)

    # exposures loop
    for i in range(1, exposures+1):
        print(f"\nRequesting exposure {i} of {exposures}")
        comError = communicate("S")
        if comError:
            return

        waitForExposureEnd(0, 10)

        print("\nRequesting end of exposure\n")
        comError = communicate("X")
        if comError:
            return
        print("Exposure done")

        # wait 25 secs or wait light to turn ON
        waitForExposureReady(0, 25)

    print("\nCalibration completed successfully please check AWS")
    print("----------------------------------------------------")
