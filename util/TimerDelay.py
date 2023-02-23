from util.RepeatTimer import RepeatTimer

count = 0
timer = None
isWaiting = False


def display(message, initValue, finalValue):
    global count, isWaiting
    minutes = int(count / 60)
    secs = count % 60
    fullMessage = f'\r{message} {minutes}min {secs}sec'
    if finalValue == count:
        resetCounter()
        endTimerDelay()
        isWaiting = False
        return print(fullMessage)

    if initValue > finalValue:
        count -= 1
    else:
        count += 1
    print(fullMessage, end='')


def setInitialValue(value):
    global count
    count = value


def resetCounter():
    global count
    count = 0


def setTimerDelay(message, initValue, finalValue):
    global timer
    setInitialValue(initValue)
    timer = RepeatTimer(1, display, args=(message, initValue, finalValue))


def startTimerDelay():
    global timer, isWaiting
    if timer is None:
        return
    timer.start()
    isWaiting = True
    while isWaiting:
        None
    return


def endTimerDelay():
    global timer, isWaiting
    if timer is None:
        return
    timer.cancel()
    isWaiting = False