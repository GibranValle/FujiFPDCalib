import serial
import time
from variables import THRESHOLD


def initSerial():
    arduino = serial.Serial('COM2', 9600)
    return arduino


def pixedDefectCalib(arduino):
    print("Pixel defect calibration selected")
    print("Estimated waiting time: 5 mins")
    print("Exposures required: 1")
    print("Request for exposure 1 of 1\n")
    # send message

    if not arduino.isOpen():
        arduino.open()

    arduino.write("E\n".encode())
    # wait 5 secs and stop
    for i in range(1, 5):
        if i == 3:
            arduino.write("X\n".encode())
        if arduino.in_waiting:
            data = arduino.readline().decode('ascii')
            print(data, end='')
        time.sleep(1)

    arduino.close()
    print("\nPlease verify AWS")
    print("__________________________________________________________")


def shadingCalib(arduino):
    exposures = 44
    prescaler = 20
    exposureDuration = 10
    print("Shading calibration selected")
    print("Estimated waiting time: 20 mins")
    print("Exposures required: 44")

    if not arduino.isOpen():
        arduino.open()

    for e in range(1, 44):
        print(f"\nRequest exposure {e} of {exposures}")
        # start exposure
        arduino.write("I\n".encode())
        isCounting = False
        isError = False
        count = 0
        string = ''

        for i in range(1, exposureDuration * prescaler):
            data = ''
            if isCounting:
                count += 1
                print("\r"+str(int(count/10))+"s", end='')

            if i == exposureDuration * prescaler * 0.9:
                # end exposure
                arduino.write("X\n".encode())

            if i > exposureDuration * prescaler * 0.9 and string == '':
                print("\nCommunication error, please verify connection")
                isError = True
                break

            if arduino.in_waiting:
                data = arduino.readline().decode('ascii')
                string += data
                if data == "N\r\n":
                    print("Handswitch emulator is asking for next exposure")
                    break
                elif data == "W\r\n":
                    isCounting = True
                else:
                    if isCounting:
                        print("\n"+data, end='')
                        isCounting = False
                    else:
                        print(data, end='')

            time.sleep(1/20)

        if isError:
            break

    arduino.close()
    print("\nPlease verify AWS")
    print("__________________________________________________________")


def uniformityCalib():
    print("X-Ray Uniformity calibration selected")
    print("Estimated waiting time: 10 mins")
    print("Exposures required: 7min")


def mAVerification():
    print("mA verification selected")
    # serialCommunication("E1D320P0A1")


def testCommunication(arduino):
    print("Communication test selected")
    if not arduino.isOpen():
        arduino.open()
    arduino.write("T\n".encode())
    for i in range(1, 100):
        time.sleep(0.01)
        if arduino.in_waiting:
            data = arduino.readline().decode('ascii')
            if data == "T\r\n":
                print("TEST SUCCESSFULLY")
            else:
                print("ERROR!")
            break
    arduino.close()


def ADCtest(arduino):
    print("ADC Reading test selected")
    if not arduino.isOpen():
        arduino.open()
    arduino.write("M\n".encode())
    for i in range(1, 100):
        time.sleep(0.01)
        if arduino.in_waiting:
            data = arduino.readline().decode('ascii')
            subdata = data[2:].replace("\r\n", "")
            value = int(subdata)
            print(value)
            if value > THRESHOLD:
                print("LIGHT IS ON")
            else:
                print("LIGHT IS OFF")
            break
    arduino.close()
