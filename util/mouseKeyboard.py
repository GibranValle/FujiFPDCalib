import pyautogui
import time
import variables
from shell.activeWindow import getWindowName
from shell.processRunning import process_exists


def moveCursorandClick(x, y, d=1):
    # print(pyautogui.size())
    pyautogui.moveTo(x, y, duration=d)
    pyautogui.click(x, y)


def pressWindows():
    pyautogui.typewrite(["win"])
    time.sleep(0.5)


def changeTab(presses=1):
    pyautogui.keyDown("altleft")
    time.sleep(.2)
    pyautogui.press("tab", presses=presses)
    time.sleep(.2)
    pyautogui.keyUp('alt')


def typeTextEnter(string):
    # pyautogui.typewrite("rupctool")
    pyautogui.typewrite(string)
    time.sleep(0.5)
    pyautogui.typewrite(["enter"])
    time.sleep(0.5)


def typeText(string):
    # pyautogui.typewrite("rupctool")
    pyautogui.typewrite(string)
    time.sleep(0.5)


# ---------------- complex options
def openRequest(appName):    
    if appName == 'RUPCTOOLS':
        if process_exists('rupc'):
            return False
        openRUPcTools()
        return True

    if appName == 'MUTL':
        if process_exists('rupc'):
            return False
        openMUTLCalibMenu()
        return True


def closeRequest(appName):
    if appName == 'RUPCTOOLS':
        if process_exists('rupc'):
            openRUPcTools()
            return True
        return False

    elif appName == 'MUTL':
        if process_exists('rupc'):
            openMUTLCalibMenu()
            return True
        return False


def openRUPcTools():
    time.sleep(0.5)
    pressWindows()
    time.sleep(0.5)
    typeTextEnter("cmd")
    time.sleep(0.5)
    typeTextEnter(variables.RUPCTOOL_DIR)
    time.sleep(0.5)
    typeTextEnter(variables.RUPCTOOL_EXE)
    time.sleep(0.5)


def closeRUPcTools():
    time.sleep(0.5)
    moveCursorandClick(variables.RUPCTOOL_CLOSE)
    time.sleep(0.5)


def openMUTLCalibMenu():
    time.sleep(0.5)
    moveCursorandClick(variables.MCU0)
    time.sleep(0.5)
    moveCursorandClick(variables.MUTL)
    time.sleep(0.5)
    moveCursorandClick(variables.RIGHT_OPTIONS)
    time.sleep(0.5)
    moveCursorandClick(variables.MUTL_CALIBRATION)


def closeMUTLCalibMenu():
    time.sleep(0.5)
    moveCursorandClick(variables.MUTL_CALIBRATION_CLOSE)
    time.sleep(0.5)


def selectCalibMUTL():
    time.sleep(0.5)
    moveCursorandClick(variables.LEFT_OPTIONS)
    time.sleep(0.1)
    moveCursorandClick(variables.LEFT_OPTIONS)
    time.sleep(0.5)
    moveCursorandClick(variables.RIGHT_OPTIONS)
    time.sleep(0.5)
    moveCursorandClick(variables.MUTL_CALIBRATION)


def clickOffsetCalibration():
    time.sleep(0.5)
    moveCursorandClick(variables.OFFSET)
    time.sleep(0.5)
    moveCursorandClick(variables.CALIB_FPD)
    time.sleep(0.5)
    moveCursorandClick(variables.CALIB_FPD)
    time.sleep(0.5)
    moveCursorandClick(variables.FIELD_CALIBRATION)
    time.sleep(0.5)


def clickDefectCalibration():
    time.sleep(0.5)
    moveCursorandClick(variables.DEFECTE)
    time.sleep(0.5)
    moveCursorandClick(variables.CALIB_FPD)
    time.sleep(0.5)
    moveCursorandClick(variables.CALIB_FPD)
    time.sleep(0.5)
    moveCursorandClick(variables.FIELD_CALIBRATION)
    time.sleep(0.5)


def clickDefectSolidCalibration():
    time.sleep(0.5)
    moveCursorandClick(variables.DEFECT_SOLID)
    time.sleep(0.5)
    moveCursorandClick(variables.CALIB_FPD)
    time.sleep(0.5)
    moveCursorandClick(variables.CALIB_FPD)
    time.sleep(0.5)
    moveCursorandClick(variables.FIELD_CALIBRATION)
    time.sleep(0.5)


def clickPixelDefectCalibration():
    time.sleep(0.5)
    moveCursorandClick(variables.PIXEL_DEFECT)
    time.sleep(0.5)
    moveCursorandClick(variables.CALIB_FPD)
    time.sleep(0.5)
    moveCursorandClick(variables.CALIB_FPD)
    time.sleep(0.5)
    moveCursorandClick(variables.FIELD_CALIBRATION)
    time.sleep(0.5)


def clickShadingCalibration():
    time.sleep(0.5)
    moveCursorandClick(variables.SHADING)
    time.sleep(0.5)
    moveCursorandClick(variables.CALIB_FPD)
    time.sleep(0.5)
    moveCursorandClick(variables.CALIB_FPD)
    time.sleep(0.5)
    moveCursorandClick(variables.FIELD_CALIBRATION)
    time.sleep(0.5)


def clickUniformityCalibration():
    time.sleep(0.5)
    moveCursorandClick(variables.UNIFORMITY)
    time.sleep(0.5)
    moveCursorandClick(variables.CALIB_FPD)
    time.sleep(0.5)
    moveCursorandClick(variables.CALIB_FPD)
    time.sleep(0.5)
    moveCursorandClick(variables.FIELD_CALIBRATION)
    time.sleep(0.5)


# TODO ADVANCED FUNTIONS IN DEVELOPMENT
def deleteMU0():
    moveCursorandClick(variables.MU0)
    moveCursorandClick(variables.DELETE_RU)


def deleteMCU0():
    moveCursorandClick(variables.MCU0)
    moveCursorandClick(variables.DELETE_RU)


def addMU0():
    moveCursorandClick(variables.NEW_RU)
    moveCursorandClick(variables.RU_NAME)
    typeText("MU0")
    moveCursorandClick(variables.RU_IP)
    typeText("192168000100")
    moveCursorandClick(variables.PING)


def addMCU0():
    moveCursorandClick(variables.NEW_RU)
    moveCursorandClick(variables.RU_NAME)
    typeText("MCU0")
    moveCursorandClick(variables.RU_IP)
    typeText("192168000101")
    moveCursorandClick(variables.PING)


def addBPY():
    moveCursorandClick(variables.NEW_RU)
    moveCursorandClick(variables.RU_NAME)
    typeText("BPY")
    moveCursorandClick(variables.RU_IP)
    typeText("192168000102")
    moveCursorandClick(variables.PING)
