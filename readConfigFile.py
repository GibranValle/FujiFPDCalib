
file = open('setup.ini', 'r')
readData = {}


def readIni():
    lines = file.readlines()
    size = len(lines)

    for i in range(0, size):
        splited = lines[i].rstrip().split("=")
        name = splited[0]
        value = int(splited[1])
        readData[name] = value

    return readData


def getPort():
    data = readIni()
    port = data['COM']
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


def getMaxCount():
    data = readIni()
    value = data['COUNT_TO_CONTINUE']
    return value


def getCountDown():
    data = readIni()
    value = data['COUNTDOWN']
    return value

