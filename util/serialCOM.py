import time
import serial
import serial.tools.list_ports
from util.readConfigFile import getPortName

arduino = None
buffer = ''
isListening = True
response = ''
waitingResponse = False
offline = False


def startListening():
    global arduino, isListening, buffer, response, waitingResponse, offline
    from calibrationBot import endMain
    try:
        arduino = advancedSerialInit()
        if not arduino.isOpen():
            arduino.open()
        time.sleep(1.5)

    except AttributeError:
        offline = True
        return

    except serial.serialutil.SerialException:
        offline = True
        endMain()
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
            if response != '':
                waitingResponse = False


def endListening():
    global isListening
    isListening = False
    try:
        arduino.close()
        time.sleep(2)
        print(' -- PROGRAM ABORTION SUCCESSFULLY -- ')
    except AttributeError:
        print(' -- ABORTION ANORMALLY --')
        return


def write2Read(message):
    global buffer, waitingResponse, response
    waitingResponse = True
    buffer = message
    while waitingResponse:
        pass
    return response


def communicate(message):
    global offline
    if offline:
        return True
    res = write2Read(message)
    if res == message:
        return True
    print(" *** COMMUNICATION ERROR ***")
    return False


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
    portName = getPortName()
    foundPorts = getPorts()
    connectPort = findItem(foundPorts, portName)
    if connectPort != '':
        return serial.Serial(connectPort, 9600)
