import pyautogui
import os

path = os.getcwd()
confidence = 0.9


def isBlocked():
    global confidence
    x, y = -1, -1
    try:
        xray_blocked_xy = pyautogui.locateCenterOnScreen(f'{path}/img/xray_blocked.png', confidence=confidence)
        x, y = xray_blocked_xy
        return x, y

    except TypeError:
        print('Icon not found on screen')
        return x, y


def isExposing():
    global confidence
    x, y = -1, -1
    try:
        xray_exposing_xy = pyautogui.locateCenterOnScreen(f'{path}/img/xray_exposing.png', confidence=confidence)
        x, y = xray_exposing_xy
        return x, y
    except TypeError:
        print('Icon not found on screen')
        return x, y


def isStandby():
    global confidence
    x, y = -1, -1
    try:
        xray_standby_xy = pyautogui.locateCenterOnScreen(f'{path}/img/xray_standby.png', confidence=confidence)
        x,y = xray_standby_xy
        return x, y
    except TypeError:
        print('Icon not found on screen')
        return x, y


