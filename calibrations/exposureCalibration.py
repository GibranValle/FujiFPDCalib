import time

from util.delayManager import waitTillEnd, waitTillReady, createText
from util.serialCOM import communicate


def initMessage(calibName, minutes):
    print(f"{calibName} calibration selected")
    print(f"Estimated waiting time: {minutes} mins")
    print("----------------------------------------------------")


def endMessage():
    print("Calibration completed successfully please check AWS")
    print("----------------------------------------------------")


def genericCalibration(name, exposures, mouse, duration=9, pause=30):
    totaltime = 0
    print(f'{exposures} total exposures needed')
    if mouse:
        0

    if mouse:  # wait 500 secs OR wait SS
        print('WAITING FOR READY SIGNAL...')
        totaltime += waitTillReady(1, 500)

    for i in range(1, exposures+1):
        print(f"\n<-- Requesting exposure {i} of {exposures} -->", end='')
        if not communicate("S"):
            return  # return if no communication is established
        print(f"\r<-- Requested exposure {i} of {exposures} -->")

        totaltime += waitTillEnd(1, duration)
        print("\r<-- Requesting end of exposure -->", end='')
        if not communicate("X"):
            return  # return if no communication is established
        print("\r                                  ", end='\r')
        if exposures > 1:
            totaltime += waitTillReady(1, pause)

    text = createText('\n<---- This calibration took', totaltime)
    print(text, end=' ---->\n')
    endMessage()


def defectSolidCalib(mouse=False, exposures=1):
    initMessage('Defect solid', 5)
    genericCalibration('defect-solid', exposures, mouse)


def pixedDefectCalib(mouse=False, exposures=1):
    initMessage('Pixel defect', 5)
    genericCalibration('pixel-defect', exposures, mouse)


def shadingCalib(mouse=False, exposures=44):
    initMessage('Shading calibration', 25)
    genericCalibration('shading', exposures, mouse)


def uniformityCalib(mouse=False, exposures=7):
    initMessage('Uniformity calibration', 10)
    genericCalibration('uniformity', exposures, mouse)


def defectSolidStereoCalib(mouse=False, exposures=2):
    initMessage('Defect solid', 5)
    genericCalibration('uniformity', exposures, mouse)


def defectSolidBpyCalib(mouse=False, exposures=4):
    initMessage('Defect solid', 5)
    genericCalibration('uniformity', exposures, mouse)


def defectSolidTomoCalib(mouse=False, exposures=2):
    initMessage('Defect solid', 5)
    genericCalibration('uniformity', exposures, mouse)


def uniformityCalibStereo(mouse=False, exposures=2):
    initMessage('Uniformity calibration', 10)
    genericCalibration('uniformity', exposures, mouse)


def uniformityCalibBpy(mouse=False, exposures=4):
    initMessage('Uniformity calibration', 10)
    genericCalibration('uniformity', exposures, mouse)


def uniformityCalibTomo(mouse=False, exposures=2):
    initMessage('Uniformity calibration', 10)
    genericCalibration('uniformity', exposures, mouse)


def uniformityCalibES(mouse=False, exposures=2):
    initMessage('Uniformity calibration', 10)
    genericCalibration('uniformity', exposures, mouse)
