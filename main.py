# test started 29/01/2023
# final modification @ 29/01/2023
# Press Mayús+F10 to execute it or replace it with your code.

import serial
import time
import pyautogui

# print(pyautogui.size())
# pyautogui.typewrite(["win"])
# time.sleep(0.5)
# pyautogui.typewrite("rupctool")
# pyautogui.hotkey("altleft", "tab")
# time.sleep(0.5)
# pyautogui.hotkey("altleft", "tab")
# time.sleep(0.5)
# pyautogui.hotkey("altleft", "tab")
# time.sleep(0.5)
# pyautogui.hotkey("altleft", "tab")
# time.sleep(0.5)
# pyautogui.hotkey("altleft", "tab")
# time.sleep(0.5)
# pyautogui.moveTo(100, 100, duration=1)
# pyautogui.moveTo(1800, 100, duration=1)
# pyautogui.moveTo(1800, 900, duration=1)
# pyautogui.moveTo(100, 900, duration=1)
# pyautogui.click(100, 100)


def serialCommunication(message):
    isListening = True
    print('opening serial port...\n')
    arduino = serial.Serial('COM8', 9600, timeout=30)
    if arduino.isOpen():
        arduino.close()
    arduino.open()
    # need to wait 1.5 for port preparation;
    time.sleep(1.5)
    arduino.write(message.encode())
    # end message
    arduino.write("\n".encode())
    while isListening:
        while arduino.in_waiting:
            data = arduino.readline().decode('ascii')
            if data == "T\n":
                print("ok... closing port")
                isListening = False
            else:
                print(data)
    arduino.close()


def text(minutes, exposures, name):
    print(f'Starting, {name} calibration')
    print(f'estimated time: {minutes}min.')
    if exposures == 0:
        print('no exposure is required')
    print('please wait...')


def fullCalibration():
    print('starting full calibration...')
    offsetCalib()
    defectCalib()
    pixedDefectCalib()
    shadingCalib()
    uniformityCalib()

def offsetCalib():
    text(7, 0, 'offset')


def defectCalib():
    text(3, 0, 'defect')


def pixedDefectCalib():
    text(3, 1, 'pixel-defect')
    serialCommunication("O4")


def shadingCalib():
    text(20, 44, 'shading')
    serialCommunication("O5")


def uniformityCalib():
    text(10, 7, 'x-ray uniformity')
    serialCommunication("O6")


def mAVerification():
    text(5, 1, 'mA Verification')
    serialCommunication("O8")


isRunning = True
while isRunning:
    print('\nAutomatic MG FPD Calibration script by Gibran Valle FFMX\n')
    print('Available options')
    print(' 1) Full calibration\n 2) Offset \n 3) Defect')
    print(' 4) Pixel-defect \n 5) Shading \n 6) X-ray uniformity')
    print(' 7) Test communication')
    print(' 8) mA Verification')
    print(' 0) Exit program\n')
    selection = input('selected: ')

    if selection == '1':
        fullCalibration()
    elif selection == '2':
        offsetCalib()
    elif selection == '3':
        defectCalib()
    elif selection == '4':
        pixedDefectCalib()
    elif selection == '5':
        shadingCalib()
    elif selection == '6':
        uniformityCalib()
    elif selection == '7':
        serialCommunication("O7")
    elif selection == '8':
        mAVerification()
    elif selection == '0':
        isRunning = False
