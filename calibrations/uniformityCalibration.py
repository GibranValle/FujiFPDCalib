from util.delayManager import waitForExposureReady, waitForExposureEnd
from util.serialCOM import communicate
from calibrations.exposureCalib import initMessage, exposureMessage, endMessage


def uniformityCalib(timer, exposures=7):
    initMessage('Uniformity calibration', 10)
    print(f'{exposures} total exposures needed')
    # TODO MOUSE CALIB
    # wait 500 secs OR wait SS
    if not timer:
        waitForExposureReady(1, 500)
    for i in range(1, exposures + 1):
        exposureMessage(i, exposures)
        comError = communicate("S")
        if comError:
            return
        print("\r----- UNDER EXPOSURE ------")
        waitForExposureEnd(1, 5, timer)
        print(" <-- Requesting end of exposure -->", end='')
        comError = communicate("X")
        if comError:
            return
        print("\r--> Exposure done <--")
        print(f'X-ray device preparing for next exposure {i+1}/{exposures}...')
        waitForExposureReady(1, 30, timer)
    endMessage()
