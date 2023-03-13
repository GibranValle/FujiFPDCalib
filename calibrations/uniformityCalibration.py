import time

from util.LightDelay import waitForDoneSignal, waitForReadySignal
from util.serialCOM import communicate


def uniformityCalib(exposures=7):
    print("Uniformity calibration selected")
    print("Estimated waiting time: 10 mins")
    print("Exposures required: "+str(exposures))
    # exposures loop
    for i in range(1, exposures+1):
        print(f"\nRequesting exposure {i} of {exposures}")
        comError = communicate("S")
        if comError:
            return

        # wait 10 secs OR wait light to turn off
        # waitForDoneSignal(0, 10)
        # TODO CHECK FOR LIGHT BEFORE EXPOSURE
        # TODO IMPLEMENT WAIT FOR
        time.sleep(10)

        print("\nRequesting end of exposure\n")
        comError = communicate("X")
        if comError:
            return
        print("Exposure done")

        # wait 25 secs or wait light to turn ON
        waitForReadySignal(0, 20)

    print("\nCalibration completed successfully please check AWS")
    print("----------------------------------------------------")
