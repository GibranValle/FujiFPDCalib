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
    pressWindows()
    typeTextEnter("cmd")
    typeTextEnter(variables.RUPCTOOL_DIR)
    typeTextEnter(variables.RUPCTOOL_EXE)


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


def openFPDCalibMenu():
    moveCursorandClick(variables.MCU0)
    moveCursorandClick(variables.MUTL)
    moveCursorandClick(variables.PING)
    moveCursorandClick(variables.RIGHT_OPTIONS)
    moveCursorandClick(variables.MUTL_CALIBRATION)


def runOffsetCalibration():
    moveCursorandClick(variables.OFFSET)
    changeTab()
    moveCursorandClick(variables.FIELD_CALIBRATION)
    print("Wait ")
    time.sleep()




