from time import sleep
from win32gui import GetWindowText, GetForegroundWindow


def getWindowName():
    return GetWindowText(GetForegroundWindow())
