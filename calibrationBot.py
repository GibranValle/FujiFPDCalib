# test started 29/01/2023
# final modification @ 27/03/2023
import os
import threading
from util.menus import mainMenu, handswitchMenu, handswitchSelection, mouseMenu, mouseOptions
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
    offlineMode = False
    print("OPENING SERIAL PORT... PLEASE WAIT")
    # use threading for SERIAL COMMUNICATION WITH ARDUINO
    serialThread = threading.Thread(target=startListening)
    serialThread.start()
    os.system('cls')
    if getSerialError():
        print('Continue in offline Mode: ')
        select = input('[y/n]: ')
        if select == 'y' or select == 'Y':
            offlineMode = True

    while isRunning:
        if offlineMode:
            print('FPD Calibration helper by Gibran Valle FFMX [OFFLINE MODE]')
            print('Available emulator modes:')
            print(' 1) Mouse (M) [DEVELOPMENT]')
            print(' 0) Exit')
            select = input('Selected option: ')
            if select == '1':
                mouseMenu()
                mouseOptions()
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
                handswitchMenu()
                handswitchSelection(timer=True)
            elif select == '2':  # HandSwitch Smart
                handswitchMenu()
                handswitchSelection(timer=False)
            elif select == '3':  # Mouse
                mouseMenu()
                mouseOptions()
            elif select == '4':  # HSS+M
                # TODO
                print('NOT IMPLEMENTED YET')
            elif select == '0':
                isRunning = False
                error()
                endListening()
# ------------------------------------------- MAIN -------------------------------------------------


if __name__ == '__main__':
    main()
