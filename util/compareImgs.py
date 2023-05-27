import numpy as np
import cv2
import pyautogui
import os
path = os.getcwd()


def getSize():
    size = 's'
    width, height = pyautogui.size()
    if height >= 1100:
        size = 'm'
    elif height >= 2000:
        size = 'l'
    return size


def mse(img1, img2):
    # print(img1.shape)
    h, w, e = img1.shape
    diff = cv2.subtract(img1, img2)
    err = np.sum(diff ** 2)
    return err / (float(h * w))


def getSS():
    img = pyautogui.screenshot()
    img.save(f'{path}/img/ss.png')
    return img


def saveXRayIcon(img, size):
    xray_box = getXRayIconSmall()
    if size == 'm':
        xray_box = getXRayIcon()
    elif size == 'l':
        xray_box = getYellowXRayIconLarge()
    xray_icon = img.crop(xray_box)
    xray_icon.save(f'{path}/img/xray_icon.png')


def getXRayIconSmall():
    X_0 = 1095
    Y_0 = 1020
    X_1 = 1155
    Y_1 = 1080
    return X_0, Y_0, X_1, Y_1


def getXRayIcon():
    X_0 = 1095
    Y_0 = 1520
    X_1 = 1155
    Y_1 = 1580
    return X_0, Y_0, X_1, Y_1


def getXRayIconLarge():
    X_0 = 1410
    Y_0 = 1955
    X_1 = 1497
    Y_1 = 2020
    return X_0, Y_0, X_1, Y_1


def getYellowXRayIconSmall():
    X_0 = 1095
    Y_0 = 1020
    X_1 = 1155
    Y_1 = 1080
    return X_0, Y_0, X_1, Y_1


def getYellowXRayIcon():
    X_0 = 897
    Y_0 = 1196
    X_1 = 1296
    Y_1 = 1595
    return X_0, Y_0, X_1, Y_1


def getYellowXRayIconLarge():
    X_0 = 1233
    Y_0 = 1744
    X_1 = 1523
    Y_1 = 2043
    return X_0, Y_0, X_1, Y_1


def compareImages(imgName, size):
    img = getSS()
    saveXRayIcon(img, size)
    imgREF1 = cv2.imread(f'{path}/img/{imgName}.png')
    imgComp = cv2.imread(f'{path}/img/xray_icon.png')
    error = mse(imgREF1, imgComp)
    return error


def compareYellowIcon():
    size = getSize()
    name = 'xray_exposing_large' if size == 'l' else 'xray_exposing'
    error = compareImages(name, size)
    return error


def compareStandByIcon():
    size = getSize()
    name = 'xray_standby_large' if size == 'l' else 'xray_standby'
    error = compareImages(name, size)
    return error


def compareBlockIcon():
    size = getSize()
    name = 'xray_blocked_large' if size == 'l' else 'xray_blocked'
    error = compareImages(name, size)
    return error


def isExposing():
    error = compareYellowIcon()
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
