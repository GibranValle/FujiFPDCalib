import time
from shell.activeWindow import getWindowName
from util.mouseKeyboard import openRequest, changeTab, clickOffsetCalibration, clickDefectCalibration, \
    clickDefectSolidCalibration, clickPixelDefectCalibration, clickShadingCalibration, clickUniformityCalibration


def startMouseCalib(calibration):
    """
    :param calibration:
    available: offset, defect, defect-solid, pixel-defect, shading, uniformity.
    :return: none, only moves cursor.
    """
    isRUOpen = openRequest("RUPCTOOLS")
    if isRUOpen:
        index = getWindowName().find('RU')
        i = 0
        while index < 0:
            i += 1
            changeTab(i)
            index = getWindowName().find('RU')
            time.sleep(0.1)

    isMUTLOpen = openRequest("MUTL")
    if isMUTLOpen:
        index = getWindowName().find('MUTL')
        i = 0
        while index < 0:
            i += 1
            changeTab(i)
            index = getWindowName().find('MUTL')
            time.sleep(0.1)

    if calibration == 'offset':
        clickOffsetCalibration()
    elif calibration == 'defect':
        clickDefectCalibration()
    elif calibration == 'defect-solid':
        clickDefectSolidCalibration()
    elif calibration == 'pixel-defect':
        clickPixelDefectCalibration()
    elif calibration == 'shading':
        clickShadingCalibration()
    elif calibration == 'uniformity':
        clickUniformityCalibration()
