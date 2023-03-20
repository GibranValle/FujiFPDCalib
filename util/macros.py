import time
from util.mouseKeyboard import openRequest, changeTab, clickOffsetCalibration, clickDefectCalibration, \
    clickDefectSolidCalibration, clickPixelDefectCalibration, clickShadingCalibration, clickUniformityCalibration


def startMouseCalib(calibration):
    """
    :param calibration:
    available: offset, defect, defect-solid, pixel-defect, shading, uniformity.
    :return: none, only moves cursor.
    """
    openRequest('RUPCTOOLS')
    openRequest('MUTL')
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
