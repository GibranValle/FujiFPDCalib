from util.delayManager import waitForExposureReady, waitForExposureEnd
from util.serialCOM import communicate
from calibrations.exposureCalib import initMessage, exposureMessage, endMessage


def pixedDefectCalib(timer, exposures=1):
    initMessage('Pixel defect', 5)
    print(f'{exposures} total exposures needed')
    # TODO MOUSE CALIB
    # wait 500 secs OR wait SS
    if not timer:
        waitForExposureReady(1, 500)
    exposureMessage(1, exposures)
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
    endMessage()
