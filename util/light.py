# LIGHT ALGORITH TO KNOW IF X RAY IS READY TO CONTINUE
from readConfigFile import getThreshold
from util.serialCOM import readADC
from util.RepeatTimer import RepeatTimer

count = 0
timer = None
isWaiting = False
initial = 0
final = 0
onCount = 0
offCount = 0


def measure(message, initValue, finalValue):
    # args not used but needed for class
    global count, isWaiting, final, initial, onCount, offCount
    value = readADC()
    minutes = count / 60
    secs = count % 60
    fullMessage = f'\r{message} {int(minutes)}min {int(secs)}sec + {value}'
    print(fullMessage)

    if count == final:
        endLightDelay()
    elif final > initial:
        count += 1
    else:
        count -= 1

    if value > getThreshold():
        onCount += 1
        print("LIGHT IS ON")
    else:
        print("LIGHT IS OFF")
        offCount += 1


def setValues(initialValue, finalValue):
    global initial, final, count
    initial = initialValue
    final = finalValue
    count = initialValue


# Exportables
def setLightDelay(message, initValue, finalValue, lightCountBreak=100, darkCountBreak=100):
    global timer, isWaiting
    setValues(initValue, finalValue)
    timer = RepeatTimer(0.65, measure, args=(message, initValue, finalValue))
    timer.start()
    isWaiting = True
    while isWaiting:
        None
    return


def endLightDelay():
    global timer, isWaiting, final, count, initial
    final = count = initial = 0
    if timer is None:
        return
    timer.cancel()
    isWaiting = False
