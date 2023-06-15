import time

from util.location import blockedIcon, stdbyIcon, isExposing


def createText(msg, count):
    minutes = count // 60
    secs = count % 60
    text = f'\r{msg}: {secs}s' if minutes <= 0 else f'\r{msg}: {minutes}m {secs}s'
    return text


def waitTillEnd(init, final):
    """
    Delay of n secs until blocked icon is displayed on screen.
    :param init: initial count in secs
    :param final: final count in secs
    :return: breaks if icon is found
    """
    minTime = 3
    secsPassed = 0
    print('\r(Ctrl + C to abort) Waiting for exposure end: 0s', end='')
    try:
        for c in range(init, final + 1):
            time.sleep(1)
            secsPassed += 1
            text = createText('(Ctrl + C to abort) Waiting for exposure end', secsPassed)
            if (isStdBy() and c >= minTime) or c == final:
                print(text)
                break
            print(text, end='')
        return secsPassed
    except KeyboardInterrupt:
        text = createText('(User interrupted!) Waited for exposure end', secsPassed)
        print(text)
        return secsPassed


def waitTillReady(init, final):
    """
    Delay of n secs until standby icon is displayed on screen.
    :param init: initial count in secs
    :param final: final count in secs
    :return: breaks if icon is found
    """
    minTime = 10
    secsPassed = 0
    print('\r(Ctrl + C to abort) Waiting for next exposure: 0s', end='')
    try:
        for c in range(init, final + 1):
            time.sleep(1)
            secsPassed += 1
            text = createText('(Ctrl + C to abort) Waiting for next exposure', secsPassed)
            if (isBlocked() and c >= minTime) or c == final:
                print(text)
                break
            print(text, end='')
        return secsPassed
    except KeyboardInterrupt:
        text = createText('(User interrupted!) Waited for next exposure', secsPassed)
        print(text)
        return secsPassed


def waitTillEndYellow(final, init):
    """
    Delay of n secs until blocked icon is displayed on screen, reverse count
    :param init: initial count in secs
    :param final: final count in secs
    :return: breaks if icon is found
    """
    minTime = 60*10
    secsPassed = 0
    print('\r(Ctrl + C to abort) Waiting for exposure end: 0s', end='')
    try:
        for c in range(init, final - 1):
            time.sleep(1)
            secsPassed += 1
            text = createText('(Ctrl + C to abort) Waiting for exposure end', secsPassed)
            if (isExposureDone() and c >= minTime) or c == final:
                print(text)
                break
            print(text, end='')
        return secsPassed
    except KeyboardInterrupt:
        text = createText('(User interrupted!) Waited for exposure end', secsPassed)
        print(text)
        return secsPassed


def keyboardDelay(init, final, message):
    passed = 0
    try:
        count = range(init, final + 1)
        if init > final:
            count = range(init, final, -1)
        for _ in count:
            passed += 1
            text = createText(f'* PRESS CTRL + C TO ABORT | {message} ', passed)
            clearLine()
            print(text, end='')
            time.sleep(1)
        clearLine()
        text = createText('Time waited', passed)
        print(text)
        return passed
    except KeyboardInterrupt:
        clearLine()
        print('\r....SKIPPING COUNTDOWN....', end=' ')
        text = createText('Time waited', passed)
        print(text)
        return


def clearLine():
    print('\r                                                                                     ', end='\r')


def isStdBy():
    x, y = stdbyIcon()
    if x > 0 and y > 0:
        return True
    return False


def isBlocked():
    x, y = blockedIcon()
    if x > 0 and y > 0:
        return True
    return False


def isExposureDone():
    x, y = isExposing()
    if x > 0 and y > 0:
        return False
    return True
