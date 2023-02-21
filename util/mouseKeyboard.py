import pyautogui
import time
import variables


def moveCursorandClick(x,y,d=1):
    # print(pyautogui.size())
    pyautogui.moveTo(x, y, duration=d)
    pyautogui.click(x, y)


def pressWindows():
    pyautogui.typewrite(["win"])
    time.sleep(0.5)


def changeTab(keys):
    pyautogui.hotkey("altleft", "tab")
    time.sleep(0.5)


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
    time.sleep(0.5)


def closeMUTLCalibMenu():
    time.sleep(0.5)
    moveCursorandClick(variables.MUTL_CALIBRATION_CLOSE)
    time.sleep(0.5)


def runOffsetCalibration():
    time.sleep(0.5)
    moveCursorandClick(variables.OFFSET)
    time.sleep(0.5)
    moveCursorandClick(variables.CALIB_FPD)
    time.sleep(0.5)
    moveCursorandClick(variables.CALIB_FPD)
    time.sleep(0.5)
    moveCursorandClick(variables.FIELD_CALIBRATION)
    time.sleep(0.5)


def runDefectCalibration():
    time.sleep(0.5)
    moveCursorandClick(variables.DEFECTE)
    time.sleep(0.5)
    moveCursorandClick(variables.CALIB_FPD)
    time.sleep(0.5)
    moveCursorandClick(variables.CALIB_FPD)
    time.sleep(0.5)
    moveCursorandClick(variables.FIELD_CALIBRATION)
    time.sleep(0.5)


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






