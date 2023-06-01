from util.location import isStandby, isExposing, isBlocked, okExposure, MU0, MCU0, install, new, left, right, \
    calibration, calibrationOptional, offset, defect, defectSolid, pixelDefect, shading, sensitivity, uniformity
import pyautogui


def main():
    isRunning = True
    while isRunning:
        print('MOVE CURSOR BOT MENU')
        print(' 1) Stand by')
        print(' 2) Exposure')
        print(' 3) Blocked')
        print(' 4) Ok')

        #RUPC TOOL
        print(' RUPCTools')
        print(' a) MU0')
        print(' b) MCU0')
        print(' c) Install')
        print(' d) New')

        # MUTL
        print(' MUTL')
        print(' e) left')
        print(' f) right')
        print(' g) calibration')
        print(' h) calibration (Opt)')

        # CALIBRATION
        print(' CALIBRATION')
        print(' i) Offset')
        print(' j) Defect')
        print(' k) Defect-Solid')
        print(' l) Pixel Defect')
        print(' m) Shading')
        print(' n) Uniformity')
        print(' o) Sensitivity')

        select = input('Selection: ')

        x, y = 0, 0
        if select == '1':
            x, y = isStandby()

        if select == '2':
            x, y = isExposing()

        if select == '3':
            x, y = isBlocked()

        if select == '4':
            x, y = okExposure()

        if select == 'a':
            x, y = MU0()

        if select == 'b':
            x, y = MCU0()

        if select == 'c':
            x, y = install()

        if select == 'd':
            x, y = new()

        if select == 'e':
            x, y = left()

        if select == 'f':
            x, y = right()

        if select == 'g':
            x, y = calibration()

        if select == 'h':
            x, y = calibrationOptional()

        if select == 'i':
            x, y = offset()

        if select == 'j':
            x, y = defect()

        if select == 'k':
            x, y = defectSolid()

        if select == 'l':
            x, y = pixelDefect()

        if select == 'm':
            x, y = shading()

        if select == 'n':
            x, y = uniformity()

        if select == 'o':
            x, y = sensitivity()

        if select == '0':
            isRunning = False

        if x == -1:
            return
        pyautogui.moveTo(x, y, duration=0.5)


if __name__ == '__main__':
    main()
