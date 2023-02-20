import serial
import serial.tools.list_ports
from readConfigFile import getPort
import time


def initSerial():
    port = getPort()
    arduino = serial.Serial('COM'+port, 9600)
    return arduino


def advancedSerialInit():
    foundPorts = getPorts()
    connectPort = findItem(foundPorts, "COM1")

    if connectPort != '':
        arduino = serial.Serial(connectPort, 9600)
        print('Connected to '+connectPort)
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

    for i in range(1, timeout*prescale):
        time.sleep(1/prescale)
        if device.in_waiting:
            data = device.readline().decode('ascii').rstrip()
            if data == response:
                dataLost = False
                break
    device.close()
    return dataLost


def lightStatus(message, threshold, timeout, device, prescale=50):
    # TODO MORE GENERIC FORM NOW WORKING WITH "M:000"
    """
    :param message: message string or char to send
    :param threshold: value to compare
    :param timeout: time in secs to listen
    :param device: pyserial object ARDUINO
    """
    lightStatus = 'On'

    if not device.isOpen():
        device.open()
    device.write(f"{message}\n".encode())

    for i in range(1, timeout*prescale):
        time.sleep(1/prescale)
        if device.in_waiting:
            # M1 M10 M100 M1000
            data = device.readline().decode('ascii').rstrip()
            header = data[0]
            value = int(data[2:])
            if value < threshold:
                lightStatus = "Off"
    device.close()
    return lightStatus


def lightValue(message, timeout, device, prescale=50):
    # TODO MORE GENERIC FORM NOW WORKING WITH "M:000"
    """
    :param message: message string or char to send
    :param timeout: time in secs to listen
    :param device: pyserial object ARDUINO
    """
    if not device.isOpen():
        device.open()
    device.write(f"{message}\n".encode())

    for i in range(1, timeout*prescale):
        time.sleep(1/prescale)
        if device.in_waiting:
            # M1 M10 M100 M1000
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
