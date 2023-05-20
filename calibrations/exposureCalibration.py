from util.delayManager import waitForExposureReadySS, waitForExposureEndSS
from util.macros import startMouseCalib
from util.serialCOM import communicate


def initMessage(calibName, minutes):
    print(f"{calibName} calibration selected")
    print(f"Estimated waiting time: {minutes} mins")
    print("----------------------------------------------------")


def endMessage():
    print("Calibration completed successfully please check AWS")
    print("----------------------------------------------------")


def genericCalibration(name, exposures, mouse):
    totaltime = 0
    print(f'{exposures} total exposures needed')
    if mouse:
        startMouseCalib(name)

    if mouse:  # wait 500 secs OR wait SS
        print('WAITING FOR READY SIGNAL...')
        waitForExposureReadySS(1, 500)

    for i in range(1, exposures):
        totaltime += 1
        print(f"\n<-- Requesting exposure {i} of {exposures} -->", end='')
        if not communicate("S"):
            return  # return if no communication is established
        print(f"\r<-- Requested exposure {i} of {exposures} -->")

        waitForExposureEndSS(1, 5)
        print("\r<-- Requesting end of exposure -->", end='')
        if not communicate("X"):
            return  # return if no communication is established
        print("\r                                  ", end='\r')
        if exposures > 1:
            waitForExposureReadySS(1, 30)

    minutes = int(totaltime / 60)
    secs = totaltime % 60
    text = f'{secs}s'
    if minutes >= 1:
        text = f'{minutes}m {secs}s'
    print('This calibration took: ', text)
    endMessage()


def defectSolidCalib(mouse, exposures=1):
    initMessage('Defect solid', 5)
    genericCalibration('defect-solid', exposures, mouse)


def pixedDefectCalib(mouse, exposures=1):
    initMessage('Pixel defect', 5)
    genericCalibration('pixel-defect', exposures, mouse)


def shadingCalib(mouse, exposures=44):
    initMessage('Shading calibration', 25)
    genericCalibration('shading', exposures, mouse)


def uniformityCalib(mouse, exposures=7):
    initMessage('Uniformity calibration', 10)
    genericCalibration('uniformity', exposures, mouse)


def defectSolidStereoCalib(mouse, exposures=2):
    initMessage('Defect solid', 5)
    genericCalibration('uniformity', exposures, mouse)


def defectSolidBpyCalib(mouse, exposures=4):
    initMessage('Defect solid', 5)
    genericCalibration('uniformity', exposures, mouse)


def defectSolidTomoCalib(mouse, exposures=2):
    initMessage('Defect solid', 5)
    genericCalibration('uniformity', exposures, mouse)


def uniformityCalibStereo(mouse, exposures=2):
    initMessage('Uniformity calibration', 10)
    genericCalibration('uniformity', exposures, mouse)


def uniformityCalibBpy(mouse, exposures=4):
    initMessage('Uniformity calibration', 10)
    genericCalibration('uniformity', exposures, mouse)


def uniformityCalibTomo(mouse, exposures=2):
    initMessage('Uniformity calibration', 10)
    genericCalibration('uniformity', exposures, mouse)


def uniformityCalibES(mouse, exposures=2):
    initMessage('Uniformity calibration', 10)
    genericCalibration('uniformity', exposures, mouse)
