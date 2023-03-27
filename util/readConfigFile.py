import os

path = os.getcwd()
parent = os.path.dirname(path)


def readIni():
    file = open(f'{path}/setup.ini', 'r')
    readData = {}
    lines = file.readlines()

    for i, val in enumerate(lines):
        splited = lines[i].rstrip().split("=")
        name = splited[0]
        try:
            value = int(splited[1])
        except ValueError:
            value = splited[1]
        readData[name] = value

    return readData


def editValue(key, newValue):
    file = open(f'{path}/setup.ini', 'r+')
    lines = file.readlines()
    for i, line in enumerate(lines):
        print(len(line))
        if key in line:
            name = line.split('=')[0]
            lines[i] = f'{name}={newValue}\n'
    separator = ''
    text = separator.join(lines)
    file.seek(0)
    file.write(text)
    file.close()


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


def getCalcTime():
    data = readIni()
    duration = data['CALCULATION_TIME']
    return duration