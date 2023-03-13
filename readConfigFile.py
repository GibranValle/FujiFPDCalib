
file = open('setup.ini', 'r')
readData = {}


def readIni():
    lines = file.readlines()
    size = len(lines)

    for i in range(0, size):
        splited = lines[i].rstrip().split("=")
        name = splited[0]
        try:
            value = int(splited[1])
        except ValueError:
            value = splited[1]
        readData[name] = value

    return readData


def getPortName():
    data = readIni()
    port = data['COMNAME']
    return str(port)


def getShort():
    data = readIni()
    duration = data['SHORT_SHOT']
    return duration


def getLong():
    data = readIni()
    duration = data['LONG_SHOT']
    return duration


def getUltraLong():
    data = readIni()
    duration = data['ULTRA_LONG_SHOT']
    return duration


def getThreshold():
    data = readIni()
    value = data['THRESHOLD']
    return value


def getLowThreshold():
    data = readIni()
    value = data['THRESHOLD']
    return value


def getMaxCount():
    data = readIni()
    value = data['COUNT_TO_CONTINUE']
    return value


def getCountDown():
    data = readIni()
    value = data['COUNTDOWN']
    return value


def isEchoEnable():
    data = readIni()
    value = data['ECHO']
    boolValue = True if value else False
    return boolValue
