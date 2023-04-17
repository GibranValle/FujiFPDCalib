# test started 29/01/2023
# final modification @ 27/03/2023
import os
import threading
from util.menus import mainMenu, handswitchMenu, handswitchSelection, mouseMenu, mouseOptions, offlineMenu
from util.readConfigFile import getSerialDemo
from util.serialCOM import startListening, endListening, getSerialError, communicate

isRunning = True


def error():
    global isRunning
    if not communicate("X"):
        print(' ** PLEASE DISCONNECT DEVICE MANUALLY **')
    isRunning = False
    print("\nPREMATURE CLOSE REQUEST...")
    endListening()
# ------------------------------------------- MAIN -------------------------------------------------


def main():
    global isRunning
    isSelected = False
    serialDemo = getSerialDemo()
    offlineMode = False
    print("OPENING SERIAL PORT... PLEASE WAIT")
    # use threading for SERIAL COMMUNICATION WITH ARDUINO
    serialThread = threading.Thread(target=startListening)
    serialThread.start()
    os.system('cls')
    if getSerialError() and not serialDemo:
        print('Continue in offline Mode: ')
        select = input('[y/n]: ')
        if select == 'y' or select == 'Y':
            offlineMode = True

    while isRunning:
        if offlineMode:
            select = offlineMenu()
            if select == '1':
                mouseMenu()
                mouseOptions()
            elif select == '0':
                print("\nFINISHING...")
                isRunning = False
                return

        else:
            if getSerialError() and not serialDemo:
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
            elif select == '0':
                os.system('cls')
                isRunning = False
                error()
                endListening()
            else:
                os.system('cls')
# ------------------------------------------- MAIN -------------------------------------------------


if __name__ == '__main__':
    main()
