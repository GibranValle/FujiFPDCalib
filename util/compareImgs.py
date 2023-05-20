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
    if height >= 1100:
        xray_box = getXRayIcon()
    elif height >= 2000:
        xray_box = getXRayIconLarge()
    else:
        xray_box = getXRayIconSmall()
    xray_icon = img.crop(xray_box)
    xray_icon.save(f'{path}/img/xray_icon.png')


def saveXRayIconYellow(img):
    width, height = pyautogui.size()
    if height >= 1100:
        xray_box = getYellowXRayIcon()
    elif height >= 2000:
        xray_box = getYellowXRayIconLarge()
    else:
        xray_box = getXRayIconSmall()
    xray_icon = img.crop(xray_box)
    xray_icon.save(f'{path}/img/xray_icon_yellow.png')


def getXRayIcon():
    X_0 = 1095  #1410
    Y_0 = 1520  #1955
    X_1 = 1155  #1497
    Y_1 = 1580  #2020
    return X_0, Y_0, X_1, Y_1


def getXRayIconLarge():
    X_0 = 1410
    Y_0 = 1955
    X_1 = 1497
    Y_1 = 2020
    return X_0, Y_0, X_1, Y_1


def getYellowXRayIcon():
    X_0 = 897
    Y_0 = 1196
    X_1 = 1296
    Y_1 = 1595
    return X_0, Y_0, X_1, Y_1


def getYellowXRayIconLarge():
    X_0 = 897
    Y_0 = 1196
    X_1 = 1296
    Y_1 = 1595
    return X_0, Y_0, X_1, Y_1


def getXRayIconSmall():
    X_0 = 1095
    Y_0 = 1020
    X_1 = 1155
    Y_1 = 1080
    return X_0, Y_0, X_1, Y_1


def compareYellowIcon():
    img = getSS()
    saveXRayIconYellow(img)
    imgREF1 = cv2.imread(f'{path}/img/xray_icon_exposing.png')
    imgComp = cv2.imread(f'{path}/img/xray_icon_yellow.png')
    error = mse(imgREF1, imgComp)
    return error


def compareStandByIcon():
    img = getSS()
    saveXRayIcon(img)
    imgREF1 = cv2.imread(f'{path}/img/xray_standby.png')
    imgComp = cv2.imread(f'{path}/img/xray_icon.png')
    error = mse(imgREF1, imgComp)
    return error


def compareBlockIcon():
    img = getSS()
    saveXRayIcon(img)
    imgREF2 = cv2.imread(f'{path}/img/xray_blocked.png')
    imgComp = cv2.imread(f'{path}/img/xray_icon.png')
    error = mse(imgREF2, imgComp)
    return error


def isExposing():
    error = compareStandByIcon()
    if error < 10:
        return True
    return False


def isStandBy():
    error = compareStandByIcon()
    if error < 10:
        return True
    return False


def isBlocked():
    error = compareBlockIcon()
    if error < 10:
        return True
    return False
