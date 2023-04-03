from util.delayManager import waitForExposureReady, waitForExposureEnd
from util.serialCOM import communicate
from calibrations.exposureCalib import initMessage, exposureMessage, endMessage


def defectSolidCalib(timer, exposures=1):
    initMessage('Defect solid', 5)
    print(f'{exposures} total exposures needed')
    # TODO MOUSE CALIB
    # wait 500 secs OR wait SS
    if not timer:
        waitForExposureReady(1, 500)
    exposureMessage(1, exposures)
    if not communicate("S"):
        return
    print("\r ----- UNDER EXPOSURE ------")
    waitForExposureEnd(1, 5, timer)
    print(" <-- Requesting end of exposure -->", end='')
    if not communicate("X"):
        return
    print("\r--> Exposure done <--")
    endMessage()
