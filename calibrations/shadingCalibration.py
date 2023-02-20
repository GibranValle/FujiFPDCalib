import time


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