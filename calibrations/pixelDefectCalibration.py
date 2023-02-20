import time


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