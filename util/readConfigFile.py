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


def getMACalibDuration():
    data = readIni()
    duration = data['MA_FULL_CALIB_DURATION']
    return duration


def getCountDown():
    data = readIni()
    value = data['COUNTDOWN']
    return value


def getCalcTime():
    data = readIni()
    duration = data['CALCULATION_TIME']
    return duration


def isSerialEchoEnable():
    data = readIni()
    value = data['ECHO']
    boolValue = True if value else False
    return boolValue


def getSerialDemo():
    data = readIni()
    serial = data['DEMO_SERIAL']
    return serial
