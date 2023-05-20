import time
from util.compareImgs import isStandBy, isBlocked


def clearLine():
    print('\r                                                                                 ', end='\r')


def keyboardDelay(init, final, message):
    try:
        count = range(init, final + 1)
        if init > final:
            count = range(init, final, -1)
        passed = 0
        for c in count:
            passed += 1
            minutes = int(c/60)
            secs = c % 60
            text = f'\r* PRESS CTRL + C TO ABORT * | {message} {secs}s'
            if minutes >= 1:
                text = f'\r* PRESS CTRL + C TO ABORT * | {message} {minutes}m {secs}s'
            clearLine()
            print(text, end='')
            time.sleep(1)
        minutes = int(passed / 60)
        secs = passed % 60
        clearLine()
        text = f'\rTime waited: {secs}s'
        if minutes >= 1:
            text = f'\rTime waited: {minutes}m {secs}s'
        print(text)
    except KeyboardInterrupt:
        clearLine()
        print('\r....SKIPPING COUNTDOWN....', end=' ')
        minutes = int(passed / 60)
        secs = passed % 60
        text = f'Time waited: {secs}s'
        if minutes >= 1:
            text = f'Time waited: {minutes}m {secs}s'
        print(text)
        return


def setSSDelay(init, final, standByWanted):
    passed = 0
    try:
        count = range(init, final + 1)
        if init > final:
            count = range(init, final, -1)
        for c in count:
            time.sleep(1)
            passed += 1
            minutes = int(c/60)
            secs = c % 60
            text = f'* PRESS CTRL + C TO ABORT * | {secs}s'
            if minutes >= 1:
                text = f'* PRESS CTRL + C TO ABORT * |{minutes}m {secs}s'
            if standByWanted:
                status = '✓' if isStandBy() else '⤫'
                text += f' Ready for exposure: {status}'
                if status:
                    break
            else:
                status = isBlocked()
                text += f' Exposure finished: {status}'
                if status:
                    break
            print(f'\r{text}', end='')

        minutes = int(passed / 60)
        secs = passed % 60
        text = f'{secs}s'
        if minutes >= 1:
            text = f'{minutes}m {secs}s'
        clearLine()
        if not standByWanted:
            print('Time under exposure: ', text)
        else:
            print('Time waiting for next exposure: ', text)
    except KeyboardInterrupt:
        clearLine()
        print('....SKIPPING COUNTDOWN....', end=' ')
        minutes = int(passed / 60)
        secs = passed % 60
        text = f'{secs}s'
        if minutes >= 1:
            text = f'{minutes}m {secs}s'
        if not standByWanted:
            print('Time under exposure: ', text)
        else:
            print('Time waiting for next exposure: ', text)
        return


def waitForExposureReadySS(init, final):
    setSSDelay(init, final, standByWanted=True)


def waitForExposureEndSS(init, final):
    setSSDelay(init, final, standByWanted=False)
