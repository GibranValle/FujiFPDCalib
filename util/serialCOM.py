import serial
import serial.tools.list_ports
from readConfigFile import getPort, getThreshold
import time

# global variables for SERIAL COM
arduino = None
buffer = ''
isListening = True
isEcho = False
response = ''


def startListening():
    global arduino, isListening, buffer, isEcho, response

    try:
        arduino = serial.Serial(f"COM{getPort()}", 9600)
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
            print(f"data: {response}") if isEcho else 0

        if not arduino.isOpen():
            print(f" *** ARDUINO IS NO LONGER CONNECTED IN COM{getPort()} *** ")
            return


def addBuffer(message):
    global buffer
    buffer = message


def communicate(message, expectedResponse):
    global response
    comError = True
    addBuffer(message)
    time.sleep(0.2)
    if response == expectedResponse:
        comError = False
        response = ''
        return comError
    return comError


def wait4light(message, waitTime, litWanted=True, samples=5):
    """
    Count ratio of sensed light
    :param litWanted: if true will break if ratio is 1
    :param waitTime: in secs
    :param arduino: serial device
    :param message: stand-by message during waiting
    :param samples: number of samples per sec
    """
    isReady = 0
    for j in reversed(range(0, waitTime)):
        if isReady >= 2:
            print(f"\rWaited time={j}s", end='')
            print(f"\rReady to continue light ratio={round(ratio, 2)}")
            break
        litCount = 1
        print(f"\r{message}" + str(waitTime-j)+' s', end='')
        for k in range(samples):
            time.sleep(1 / samples)
            isLit = isLightOn(getThreshold())
            litCount = litCount + 1 if isLit else litCount
        ratio = litCount / (samples+1)
        if litWanted and ratio >= 0.8:
            isReady += 1
        if not litWanted and ratio <= 0.4:
            isReady += 1


def isLightOn(threshold):
    """
    :param arduino: value to compare
    :param threshold: value to compare
    """
    status = True if lightValue(1) > threshold else False
    return status


def lightValue(timeout, prescale=100):
    # TODO MORE GENERIC FORM NOW WORKING WITH "M:000"
    """
    :param timeout: time in secs to listen
    :param device: pyserial object ARDUINO
    """
    global device
    device.write("M\n".encode())
    for i in range(1, timeout * prescale):
        time.sleep(1 / prescale)
        if device.in_waiting:
            # M:1 M:10 M:100 M:1000
            data = device.readline().decode('ascii').rstrip()
            header = data[0]
            value = int(data[2:])
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
    connectPort = findItem(foundPorts, "COM1")

    if connectPort != '':
        arduino = serial.Serial(connectPort, 9600)
        print('Connected to ' + connectPort)
    else:
        print('Connection Issue')


def enableSerialEcho():
    global isEcho
    isEcho = True


def disableSerialEcho():
    global isEcho
    isEcho = False

