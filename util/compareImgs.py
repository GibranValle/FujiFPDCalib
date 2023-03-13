import numpy as np
import cv2
import pyautogui


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
    #xray_box = getXRayIcon()
    xray_box = getXRayIconWide()
    xray_icon = img.crop(xray_box)
    xray_icon.save('../img/compare/xray_icon.png')


def getXRayIcon():
    X_0 = 1095
    Y_0 = 1520
    X_1 = 1155
    Y_1 = 1580
    return X_0, Y_0, X_1, Y_1


def getXRayIconWide():
    X_0 = 1095
    Y_0 = 1020
    X_1 = 1155
    Y_1 = 1080
    return X_0, Y_0, X_1, Y_1


def compareXRayIcon():
    img = getSS()
    saveXRayIcon(img)
    imgREF1 = cv2.imread('../img/xray_standby.png')
    imgREF2 = cv2.imread('../img/xray_blocked.png')
    imgComp = cv2.imread('../img/compare/xray_icon.png')
    error1 = mse(imgREF1, imgComp)
    error2 = mse(imgREF2, imgComp)
    print("Image matching Error between the two images:", error1, error2)


def isStandBy():
    img = getSS()
    saveXRayIcon(img)
    standby = cv2.imread('../img/xray_standby.png')
    blocked = cv2.imread('../img/xray_blocked.png')
    current = cv2.imread('../img/compare/xray_icon.png')
    isInStandby = mse(standby, current)
    isInBlocked = mse(blocked, current)
    if isInStandby < 10:
        return True
    if not isInBlocked:
        print(" ** CANNOT SEE UNIT STATUS, PLEASE VERIFY **")
    return False

