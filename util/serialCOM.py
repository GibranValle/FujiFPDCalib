import serial
import serial.tools.list_ports
from readConfigFile import getPort, getThreshold
import time


def initSerial():
    port = getPort()
    arduino = serial.Serial('COM' + port, 9600)
    return arduino


def advancedSerialInit():
    foundPorts = getPorts()
    connectPort = findItem(foundPorts, "COM1")

    if connectPort != '':
        arduino = serial.Serial(connectPort, 9600)
        print('Connected to ' + connectPort)
    else:
        print('Connection Issue')


def communicate(message, response, timeout, device, prescale=20):
    """
    :param message: message string or char to send
    :param response: return if matching response
    :param timeout: time in secs to listen
    :param device: pyserial object ARDUINO
    """
    dataLost = True

    if not device.isOpen():
        device.open()
    device.write(f"{message}\n".encode())

    for i in range(1, timeout * prescale):
        time.sleep(1 / prescale)
        if device.in_waiting:
            data = device.readline().decode('ascii').rstrip()
            if data == response:
                dataLost = False
                break
    device.close()
    return dataLost


def wait4light(arduino, message, waitTime, litWanted=True, samples=5):
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
            isLit = isLightOn(arduino, getThreshold())
            litCount = litCount + 1 if isLit else litCount
        ratio = litCount / (samples+1)
        if litWanted and ratio >= 0.8:
            isReady += 1
        if not litWanted and ratio <= 0.4:
            isReady += 1


def isLightOn(arduino, threshold):
    """
    :param arduino: value to compare
    :param threshold: value to compare
    """
    status = True if lightValue(1, arduino) > threshold else False
    return status


def lightValue(timeout, device, prescale=100):
    # TODO MORE GENERIC FORM NOW WORKING WITH "M:000"
    """
    :param timeout: time in secs to listen
    :param device: pyserial object ARDUINO
    """
    if not device.isOpen():
        device.open()
    device.write("M\n".encode())

    for i in range(1, timeout * prescale):
        time.sleep(1 / prescale)
        if device.in_waiting:
            # M:1 M:10 M:100 M:1000
            data = device.readline().decode('ascii').rstrip()
            header = data[0]
            value = int(data[2:])
            device.close()
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
