import numpy as np
import cv2
import pyautogui
import os

from util.readConfigFile import getMainSide
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
    h, w, e = img1.shape
    # print(h,w,e)
    # h1, w1, e1 = img2.shape
    # print(h1, w1, e1)
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


def saveXRayIconYellow(img, size):
    xray_box = getYellowXRayIconSmall()
    if size == 'm':
        xray_box = getYellowXRayIcon()
    elif size == 'l':
        xray_box = getYellowXRayIconLarge()
    xray_icon = img.crop(xray_box)
    xray_icon.save(f'{path}/img/xray_icon_yellow.png')


def getXRayIconSmall():
    offset = 1200 if getMainSide() != 'LEFT' else 0
    # 60x60
    X_0 = 1095 + offset
    X_1 = X_0 + 60
    Y_0 = 1020
    Y_1 = Y_0 + 60
    return X_0, Y_0, X_1, Y_1


def getXRayIcon():
    offset = 1200 if getMainSide() != 'LEFT' else 0
    # 60x60
    X_0 = 1095 + offset
    X_1 = X_0 + 60
    Y_0 = 1520
    Y_1 = Y_0 + 60
    return X_0, Y_0, X_1, Y_1


def getXRayIconLarge():
    offset = 1536 if getMainSide() != 'LEFT' else 0
    # 65x65
    X_0 = 1410 + offset
    X_1 = X_0 + 65
    Y_0 = 1955
    Y_1 = Y_0 + 65
    return X_0, Y_0, X_1, Y_1


def getYellowXRayIconSmall():
    offset = 1200 if getMainSide() != 'LEFT' else 0
    # 300 x 300
    X_0 = 897 + offset
    Y_0 = 781
    X_1 = X_0 + 300
    Y_1 = Y_0 + 300
    return X_0, Y_0, X_1, Y_1


def getYellowXRayIcon():
    offset = 1200 if getMainSide() != 'LEFT' else 0
    X_0 = 897 + offset
    Y_0 = 1296
    X_1 = X_0 + 300
    Y_1 = Y_0 + 300
    return X_0, Y_0, X_1, Y_1


def getYellowXRayIconLarge():
    offset = 1536 if getMainSide() != 'LEFT' else 0
    X_0 = 1233 + offset
    Y_0 = 1744
    X_1 = X_0 + 300
    Y_1 = Y_0 + 300
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
    img = getSS()
    saveXRayIconYellow(img, size)
    imgREF1 = cv2.imread(f'{path}/img/xray_exposing.png')
    imgComp = cv2.imread(f'{path}/img/xray_icon_yellow.png')
    error = mse(imgREF1, imgComp)
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
