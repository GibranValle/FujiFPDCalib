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
        # TODO MOVE ALT TAB TO RU
        windowName = getWindowName()
        while windowName != 'RUPTools':
            changeTab()
            windowName = getWindowName()

    isMUTLOpen = openRequest("MUTL")
    if isMUTLOpen:
        # TODO MOVE ALT TAB TO MUTL
        windowName = getWindowName()
        while windowName != 'RUPTools':
            changeTab()
            windowName = getWindowName()

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
