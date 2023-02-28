import serial
import serial.tools.list_ports
from readConfigFile import getPortName

# global variables for SERIAL COM
arduino = None
buffer = ''
isListening = True
isEcho = False
response = ''
waitingResponse = False
value = 0
ADCWaiting = False


def startListening():
    global arduino, isListening, buffer, isEcho, response, value, ADCWaiting, waitingResponse

    try:
        arduino = advancedSerialInit()
    except any:
        print(" *** COM NOT CONNECTED ***")

    if not arduino.isOpen():
        arduino.open()
        if not arduino.isOpen():
            print("SERIAL PORT RUNNING...")

    while isListening:
        # data to send
        if buffer != '':
            arduino.write(f"{buffer}\n".encode())
            buffer = ''

        # data to read
        if arduino.in_waiting:
            response = arduino.readline().decode('ascii').rstrip()
            waitingResponse = False
            if response == 'E':
                print("EXPOSURE TIMEOUT")
            elif response[0] == 'M':
                ADCWaiting = False
                value = int(response[2:].rstrip())
            elif response != '' and isEcho:
                print(f"data: {response}")

        if not arduino.isOpen():
            print(f" *** ARDUINO IS NO LONGER CONNECTED *** ")
            return


def add2Buffer(message):
    global buffer
    buffer = message


def overrideResponse():
    global response
    response = 'ERROR'


def communicate(message):
    global response, waitingResponse
    waitingResponse = True
    comError = True
    add2Buffer(message)
    while waitingResponse:
        0
    # timer for duration of exposure
    if response == message:
        comError = False
        response = ''
        return comError
    print(" *** COMMUNICATION ERROR ***")
    return comError


def readADC():
    """
    Response is "M:0000" to "M:0"
    :return: int value of ADC
    """
    global value, ADCWaiting
    ADCWaiting = True
    add2Buffer("M")
    while ADCWaiting:
        0
    return value


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


def enableSerialEcho():
    global isEcho
    isEcho = True


def disableSerialEcho():
    global isEcho
    isEcho = False

