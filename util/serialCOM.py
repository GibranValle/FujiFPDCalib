import time

import serial
import serial.tools.list_ports
from util.readConfigFile import getPortName, isEchoEnable, isSerialSkip
# global variables for SERIAL COM
arduino = None
buffer = ''
isListening = True
response = ''
waitingResponse = False
serialError = False


def getSerialError():
    global serialError
    if isSerialSkip():
        return False
    return serialError


def startListening():
    global serialError
    global arduino, isListening, buffer, response, waitingResponse
    try:
        arduino = advancedSerialInit()
        if arduino.isOpen():
            arduino.close()
        arduino.open()
        if not arduino.isOpen():
            print(" *** SERIAL ERROR, CANNOT OPEN SERIAL PORT ***")
            serialError = True
            return
        time.sleep(1.5)

    except AttributeError:
        print(" *** COM NOT CONNECTED ***")
        serialError = True
        return

    while isListening:
        if not arduino.isOpen():
            print(f" *** ARDUINO IS NO LONGER CONNECTED *** ")
            serialError = True
            break
        # data to send
        if buffer != '':
            arduino.write(f"{buffer}\n".encode())
            buffer = ''
        # data to read
        elif arduino.in_waiting:
            response = arduino.readline().decode('ascii').rstrip()
            print(response) if isEchoEnable() else 0
            if response != '':
                waitingResponse = False


def endListening():
    global isListening
    isListening = False
    try:
        arduino.close()
        time.sleep(2)
    except AttributeError:
        pass


def write2Read(message):
    global buffer, waitingResponse, response
    waitingResponse = True
    buffer = message
    while waitingResponse:
        pass
    return response


def communicate(message):
    res = write2Read(message)
    if res == message:
        comError = False
        return comError
    print(" *** COMMUNICATION ERROR ***")
    comError = True
    return comError


def readADC():
    res = write2Read("M")
    if len(res) > 2:
        value = int(res[2:])
        return value
    return -1


def getPorts():
    ports = serial.tools.list_ports.comports()
    return ports


def findItem(portsFound, matchingText):
    commPort = ''
    numConnections = len(portsFound)
    for i in range(0, numConnections):
        port = portsFound[i]
        strPort = str(port)

        if matchingText in strPort:
            splitPort = strPort.split(' ')
            commPort = splitPort[0]
    return commPort


def advancedSerialInit():
    foundPorts = getPorts()
    connectPort = findItem(foundPorts, getPortName())

    if connectPort != '':
        return serial.Serial(connectPort, 9600)

