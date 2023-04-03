import time
from util.compareImgs import isStandBy


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
            text = f'\r*PRESS CTRL + C TO ABORT* |{message}{secs}s'
            if minutes >= 1:
                text = f'\r*PRESS CTRL + C TO ABORT* |{message}{minutes}m {secs}s'
            print(text, end='')
            time.sleep(1)

        minutes = int(passed / 60)
        secs = passed % 60
        text = f'\nTotal waited: {secs}s'
        if minutes >= 1:
            text = f'\nTotal waited: {minutes}m {secs}s'
        print(text)
    except KeyboardInterrupt:
        print('\nABORTING COUNTDOWN....')
        return


def setSSDelay(init, final, timer, standByWanted=True):
    counter = init
    offset = 1 if final > init else -1
    for i in range(init, final):
        counter += offset
        if not timer:
            status = isStandBy()
            if standByWanted:
                if status:
                    print("\n\n ** MU0 IS READY TO CONTINUE... ABORTING COUNTDOWN **")
                    break
                else:
                    print(f'\rWaiting for exposure ready signal{counter}s up to {final}s', end='')
            else:
                if not status:
                    print("\n\n ** MU0 IS READY TO CONTINUE... ABORTING COUNTDOWN **")
                    break
                else:
                    print(f'\rWaiting for exposure end{counter}s up to {final}s', end='')
        else:
            keyboardDelay(init, final)
        time.sleep(1)
        return


def waitForExposureReady(init, final, timer, message=''):
    setSSDelay(init, final, timer, standByWanted=True)


def waitForExposureEnd(init, final, timer, message=''):
    setSSDelay(init, final, timer, standByWanted=False)
