# test started 29/01/2023
# final modification @ 27/03/2023
import os
import threading
import time

import pyautogui
from calibrations.maFullCalib import mAFullCalibration
import util.menus as menu
from util.serialCOM import startListening, endListening, communicate
isRunning = True
offlineMode = False
import shell.process as pro


def error():
    global isRunning
    if not communicate("X"):
        print(' ** PLEASE DISCONNECT DEVICE MANUALLY **')
    isRunning = False
    print("\nPREMATURE CLOSE REQUEST...")
    endListening()


def endMain():
    global isRunning
    isRunning = False
    print(' ** COM DISCONNECTED **')


def createAvailable(init, final):
    available = ['']
    for x in range(init, final + 1):
        available.append(f'{x}')
    return available


# ------------------------------------------- MAIN -------------------------------------------------
def main():
    try:
        global isRunning
        # use threading for SERIAL COMMUNICATION WITH ARDUINO
        serialThread = threading.Thread(target=startListening)
        serialThread.start()

        while isRunning:
            # main Menu level
            mainSelect = input(menu.main())
            os.system('cls')
            if mainSelect == '1':
                isRunning = False

            elif mainSelect == '2':
                while True:
                    subSelect = input(menu.basic())
                    os.system('cls')
                    if menu.runBasic(subSelect) == -1:
                        break

            elif mainSelect == '3':
                while True:
                    subSelect = input(menu.stereoBpy())
                    os.system('cls')
                    if menu.runStereo(subSelect) == -1:
                        break

            elif mainSelect == '4':
                while True:
                    subSelect = input(menu.tomo())
                    os.system('cls')
                    if menu.runTomo(subSelect) == -1:
                        break

            elif mainSelect == '5':
                while True:
                    subSelect = input(menu.ES())
                    os.system('cls')
                    if menu.runES(subSelect) == -1:
                        break

            elif mainSelect == '6':
                mAFullCalibration()
                os.system('cls')

            elif mainSelect == '7':
                while True:
                    subSelect = input(menu.iconTest())
                    os.system('cls')
                    if subSelect == '1':
                        break
                    elif subSelect == '2':
                        while True:
                            finalSelect = input(menu.AWSicons())
                            os.system('cls')
                            if not (2 <= int(finalSelect) <= 6):
                                break
                            x, y = menu.runAWS(finalSelect)
                            if x > 0 and y > 0:
                                print('MOVING CURSOR.... PLEASE WAIT')
                                pyautogui.moveTo(x, y, duration=0.5)
                                os.system('cls')
                            else:
                                print('Icon not found')
                                continue

                    elif subSelect == '3':
                        while True:
                            finalSelect = input(menu.ruIcons())
                            os.system('cls')
                            if not (2 <= int(finalSelect) <= 5):
                                break
                            x, y = menu.runRuIcons(finalSelect)
                            if x > 0 and y > 0:
                                print('MOVING CURSOR.... PLEASE WAIT')
                                pyautogui.moveTo(x, y, duration=0.5)
                                os.system('cls')
                            else:
                                print('Icon not found')
                                continue

                    elif subSelect == '4':
                        while True:
                            finalSelect = input(menu.mutlIcons())
                            os.system('cls')
                            if not (2 <= int(finalSelect) <= 5):
                                break
                            x, y = menu.runMutl(finalSelect)
                            if x > 0 and y > 0:
                                print('MOVING CURSOR.... PLEASE WAIT')
                                pyautogui.moveTo(x, y, duration=0.5)
                                os.system('cls')
                            else:
                                print('Icon not found')
                                continue

                    elif subSelect == '5':
                        while True:
                            finalSelect = input(menu.fpdCalib())
                            os.system('cls')
                            if not (2 <= int(finalSelect) <= 8):
                                break
                            x, y = menu.runfpdCalib(finalSelect)
                            if x > 0 and y > 0:
                                print('MOVING CURSOR.... PLEASE WAIT')
                                pyautogui.moveTo(x, y, duration=0.5)
                                os.system('cls')
                            else:
                                print('Icon not found')
                                continue

                    elif subSelect == '6':
                        while True:
                            finalSelect = input(menu.fpdOptional())
                            os.system('cls')
                            if not (2 <= int(finalSelect) <= 8):
                                break
                            x, y = menu.runOptionalCalib(finalSelect)
                            if x > 0 and y > 0:
                                print('MOVING CURSOR.... PLEASE WAIT')
                                pyautogui.moveTo(x, y, duration=0.5)
                                os.system('cls')
                            else:
                                print('Icon not found')
                                continue
            elif mainSelect == '8':
                while True:
                    0

            elif mainSelect == '9':
                while True:
                    subSelect = input(menu.window())
                    os.system('cls')
                    if menu.runWindow(subSelect) == -1:
                        break

            elif mainSelect == '10':
                print('Please disconnect PACS ethernet cable')
                pro.saveMACs()
                time.sleep(1)
                print('File created successfully!')

        error()
    except KeyboardInterrupt:
        isRunning = False
        print('Closing...')


# ------------------------------------------- MAIN -------------------------------------------------


if __name__ == '__main__':
    print('Opening serial port...')
    main()
