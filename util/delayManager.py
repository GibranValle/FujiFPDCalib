import time
from util.compareImgs import isStandBy


def keyboardDelay(init, final):
    count = range(init, final + 1)
    if init > final:
        count = reversed(count)
    for c in count:
        time.sleep(1)
        try:
            minutes = int(c/60)
            secs = c % 60
            print(f'\rTYPE CTRL + C TO STOP | Waited: {minutes}min {secs}sec up to {final}s', end='')
        except KeyboardInterrupt:
            print('\rKEY PRESSED... STOPING')
            break
    print(f'\rWaited: {minutes}min {secs}sec')


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


def waitForExposureReady(init, final, timer):
    setSSDelay(init, final, timer, standByWanted=True)


def waitForExposureEnd(init, final, timer):
    setSSDelay(init, final, timer, standByWanted=False)