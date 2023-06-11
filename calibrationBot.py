# test started 29/01/2023
# final modification @ 27/03/2023
import os
import threading
import pyautogui
from calibrations.maFullCalib import mAFullCalibration
import util.menus as menu
from util.serialCOM import startListening, endListening, communicate
isRunning = True
offlineMode = False


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
    mainAVL = createAvailable(2, 9)
    basicAVL = stereoAVL = ruIconsAVL = mutlIcons = createAvailable(2, 5)
    tomoAVL = createAvailable(2, 3)
    ESAVL = createAvailable(2, 2)
    iconAVL = AWSAVL = createAvailable(2, 6)
    fpdAVL = fpdOptAVL = createAvailable(2, 8)

    try:
        global isRunning
        # use threading for SERIAL COMMUNICATION WITH ARDUINO
        serialThread = threading.Thread(target=startListening)
        serialThread.start()

        while isRunning:
            # main Menu level
            mainSelect = input(menu.main())
            os.system('cls')
            if mainSelect not in mainAVL:
                continue

            subSelect = ''
            if mainSelect == '2':
                while subSelect != '1':
                    subSelect = input(menu.basic())
                    os.system('cls')
                    if subSelect not in basicAVL:
                        continue
                    menu.runBasic(subSelect)

            if mainSelect == '3':
                while subSelect != '1':
                    subSelect = input(menu.stereoBpy())
                    os.system('cls')
                    if subSelect not in stereoAVL:
                        continue
                    menu.runStereo(subSelect)

            if mainSelect == '4':
                while subSelect != '1':
                    subSelect = input(menu.tomo())
                    os.system('cls')
                    if subSelect not in tomoAVL:
                        continue
                    menu.runTomo(subSelect)

            if mainSelect == '5':
                while subSelect != '1':
                    subSelect = input(menu.ES())
                    os.system('cls')
                    if subSelect not in ESAVL:
                        continue
                    menu.runES(subSelect)

            if mainSelect == '6':
                mAFullCalibration()
                os.system('cls')

            if mainSelect == '7':
                finalSelect = ''
                while subSelect != '1':
                    subSelect = input(menu.iconTest())
                    os.system('cls')
                    if subSelect not in iconAVL:
                        continue

                    if subSelect == '2':
                        while finalSelect != '1':
                            finalSelect = input(menu.AWSicons())
                            os.system('cls')
                            if finalSelect not in AWSAVL:
                                continue
                            x, y = menu.runAWS(finalSelect)
                            if x > 0 and y > 0:
                                pyautogui.moveTo(x, y, duration=0.5)

                    if subSelect == '3':
                        while finalSelect != '1':
                            finalSelect = input(menu.ruIcons())
                            os.system('cls')
                            if finalSelect not in ruIconsAVL:
                                continue
                            x, y = menu.runRuIcons(finalSelect)
                            if x > 0 and y > 0:
                                pyautogui.moveTo(x, y, duration=0.5)

                    if subSelect == '4':
                        while finalSelect != '1':
                            finalSelect = input(menu.mutlIcons())
                            os.system('cls')
                            if finalSelect not in mutlIcons:
                                continue
                            x, y = menu.runMutl(finalSelect)
                            if x > 0 and y > 0:
                                pyautogui.moveTo(x, y, duration=0.5)

                    if subSelect == '5':
                        while finalSelect != '1':
                            finalSelect = input(menu.fpdCalib())
                            os.system('cls')
                            if finalSelect not in fpdAVL:
                                continue
                            x, y = menu.runfpdCalib(finalSelect)
                            if x > 0 and y > 0:
                                pyautogui.moveTo(x, y, duration=0.5)

                    if subSelect == '6':
                        while finalSelect != '1':
                            finalSelect = input(menu.fpdOptional())
                            os.system('cls')
                            if finalSelect not in fpdOptAVL:
                                continue
                            x, y = menu.runOptionalCalib(finalSelect)
                            if x > 0 and y > 0:
                                pyautogui.moveTo(x, y, duration=0.5)

        error()
    except KeyboardInterrupt:
        isRunning = False
        print('Closing...')


# ------------------------------------------- MAIN -------------------------------------------------


if __name__ == '__main__':
    print('Opening serial port...', end='')
    main()
