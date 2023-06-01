# test started 29/01/2023
# final modification @ 27/03/2023
import os
import threading

from util.location import isBlocked, isExposing, isStandby
from util.menus import mainMenu, handswitchMenu, handswitchSelection, mouseMenu, mouseOptions, offlineMenu
from util.serialCOM import startListening, endListening, getSerialError, communicate

isRunning = True
offlineMode = False


def error():
    global isRunning
    if not communicate("X"):
        print(' ** PLEASE DISCONNECT DEVICE MANUALLY **')
    isRunning = False
    print("\nPREMATURE CLOSE REQUEST...")
    endListening()


def getOfflineMode():
    global offlineMode
    return offlineMode


def setOfflineMode(state):
    global offlineMode
    offlineMode = state
    return offlineMode


def getTestSS():
    x, y = isBlocked()
    if x > 0 and y > 0:
        print('isBlocking')

    x, y = isExposing()
    if x > 0 and y > 0:
        print('isExposing')

    x, y = isStandby()
    if x > 0 and y > 0:
        print('isStandby')


# ------------------------------------------- MAIN -------------------------------------------------


def main():
    print("OPENING SERIAL PORT... PLEASE WAIT", end='\n')
    global isRunning
    isSelected = False
    # use threading for SERIAL COMMUNICATION WITH ARDUINO
    serialThread = threading.Thread(target=startListening)
    serialThread.start()
    os.system('cls')
    if getSerialError():
        setOfflineMode(True)

    while isRunning:
        if offlineMode:
            select = offlineMenu()
            if select == '1':
                mouseMenu()
                mouseOptions()
            elif select == '2':
                getTestSS()
            elif select == '0':
                print("\nFINISHING...")
                isRunning = False
                return

        else:
            if getSerialError():
                print(' ** Verify connection with handswitch emulator **')
                break
            select = mainMenu()
            if select == '1':  # HandSwitch with Timer
                isSelected = True
                os.system('cls')
                while isSelected:
                    handswitchMenu()
                    isSelected = handswitchSelection()
            elif select == '2':  # Mouse
                isSelected = True
                os.system('cls')
                while isSelected:
                    mouseMenu()
                    isSelected = mouseOptions()
            elif select == '3':  # HSS+M
                os.system('cls')
                # TODO
                print('NOT IMPLEMENTED YET')
                return
                handswitchMenu()
                handswitchSelection(mouse=True)
            elif select == '4':
                os.system('cls')
                getTestSS()
            elif select == '0':
                os.system('cls')
                isRunning = False
                error()
                endListening() if getOfflineMode() else 0
            else:
                os.system('cls')
# ------------------------------------------- MAIN -------------------------------------------------


if __name__ == '__main__':
    main()
