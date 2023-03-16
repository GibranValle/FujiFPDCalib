import time

import numpy as np
import cv2
import pyautogui

import os

path = os.getcwd()


def mse(img1, img2):
    # print(img1.shape)
    h, w, e = img1.shape
    diff = cv2.subtract(img1, img2)
    err = np.sum(diff ** 2)
    return err / (float(h * w))


def getSS():
    img = pyautogui.screenshot()
    return img


def saveXRayIcon(img):
    width, height = pyautogui.size()
    if height > 1000:
        xray_box = getXRayIcon()
    else:
        xray_box = getXRayIconSmall()
    xray_icon = img.crop(xray_box)
    xray_icon.save(f'{path}/img/xray_icon.png')


def getXRayIcon():
    X_0 = 1095
    Y_0 = 1520
    X_1 = 1155
    Y_1 = 1580
    return X_0, Y_0, X_1, Y_1


def getXRayIconSmall():
    X_0 = 1095
    Y_0 = 1020
    X_1 = 1155
    Y_1 = 1080
    return X_0, Y_0, X_1, Y_1


def scanXRayIcon():
    img = getSS()
    saveXRayIcon(img)
    imgREF1 = cv2.imread(f'{path}/img/xray_standby.png')
    imgREF2 = cv2.imread(f'{path}/img/xray_blocked.png')
    imgComp = cv2.imread(f'{path}/img/xray_icon.png')
    error1 = mse(imgREF1, imgComp)
    error2 = mse(imgREF2, imgComp)
    print("Image matching Error between the two images:", error1, error2)
    if error1 < 10:
        return 'stdby'
    elif error2 < 10:
        return 'blocked'
    else:
        return -1


def isStandBy():
    status = scanXRayIcon()
    if status == 'stdby':
        print("Unit is ready to perform exposure")
        return True
    elif status == 'blocked':
        print("Unit is NOT ready to perform exposure")
        return False
    elif status == -1:
        #print(" ** CANNOT READ UNIT STATUS PLEASE VERIFY **")
        return -1


def setSSDelay(init, final, standByWanted=True):
    counter = init
    offset = 1 if final > init else -1
    for i in range(init, final):
        counter += offset
        print(f"\rWaiting: {counter}s", end='')
        time.sleep(1)
        status = isStandBy()
        if standByWanted and status:
            print("\n\n ** MU0 IS READY TO CONTINUE... ABORTING COUNTDOWN **", end='')

            break
        elif not standByWanted and not status:
            print("\n\n ** MU0 IS READY TO CONTINUE... ABORTING COUNTDOWN **", end='')
            break

        if standByWanted:
            print(f'Waiting for exposure ready signal{counter}s', end='')
        elif not standByWanted:
            print(f'Waiting for exposure end{counter}s', end='')


def waitForExposureReady(init, final):
    setSSDelay(init, final, standByWanted=True)


def waitForExposureEnd(init, final):
    setSSDelay(init, final, standByWanted=False)
