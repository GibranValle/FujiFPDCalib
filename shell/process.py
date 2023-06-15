import subprocess
import time

import win32gui as w
import win32con as c
import util.location as loc
import pyautogui as pg


def openChrome():
    if process_exists('chrome.exe'):
        return openWindow('Chrome')
    openApp('Chrome')


def closeChrome():
    name = 'chrome.exe'
    closeApp(name)


def openRU():
    if process_exists('RuPcTool.exe'):
        return openWindow('RU PC-TOOL')
    openApp('RUPCTOOL')


def closeRU():
    name = 'RuPcTool.exe'
    closeApp(name)


def openMUTLMouse():
    if process_exists('MUTL.exe'):
        return openWindow('PC-MUTL')
    #openRU
    #click MCU0 row
    #click MUTL
    openRU()
    x, y = loc.MCU0()
    if x <= 0 and y <= 0:
        return
    pg.moveTo(x, y, duration=0.5)
    pg.click(x, y)

    x, y = loc.mutl()
    if x <= 0 and y <= 0:
        return
    pg.moveTo(x, y, duration=0.5)
    pg.click(x, y)
    time.sleep(0.5)
    if process_exists('MUTL.exe'):
        return openWindow('PC-MUTL')


def openCalibrationMenuMouse():
    if process_exists('MUTL.exe'):
        openWindow('MCU0')

        x, y = loc.calibration()
        if x > 0 and y > 0:
            pg.moveTo(x, y, duration=0.5)
            pg.click(x, y)
            return

        x, y = loc.right()
        if x > 0 and y > 0:
            pg.moveTo(x, y, duration=0.5)
            pg.click(x, y)
            x, y = loc.calibration()
            if x > 0 and y > 0:
                pg.moveTo(x, y, duration=0.5)
                pg.click(x, y)
                return

    else:
        openMUTLMouse()

        x, y = loc.right()
        if x <= 0 and y <= 0:
            return
        pg.moveTo(x, y, duration=0.5)
        pg.click(x, y)

        x, y = loc.calibration()
        if x <= 0 and y <= 0:
            return
        pg.moveTo(x, y, duration=0.5)
        pg.click(x, y)


def openCalibrationOptionalMenuMouse():
    if process_exists('MUTL.exe'):
        openWindow('MCU0')

        x, y = loc.calibrationOptional()
        if x > 0 and y > 0:
            pg.moveTo(x, y, duration=0.5)
            pg.click(x, y)
            return

        x, y = loc.right()
        if x > 0 and y > 0:
            pg.moveTo(x, y, duration=0.5)
            pg.click(x, y)
            x, y = loc.calibrationOptional()
            if x > 0 and y > 0:
                pg.moveTo(x, y, duration=0.5)
                pg.click(x, y)
                return

    else:
        openMUTLMouse()

        x, y = loc.right()
        if x <= 0 and y <= 0:
            return
        pg.moveTo(x, y, duration=0.5)
        pg.click(x, y)

        x, y = loc.calibrationOptional()
        if x <= 0 and y <= 0:
            return
        pg.moveTo(x, y, duration=0.5)
        pg.click(x, y)


def startShadingCalib():
    openCalibrationOptionalMenuMouse()
    x, y = loc.shading()
    if x <= 0 and y <= 0:
        return
    pg.moveTo(x, y, duration=0.5)
    pg.click(x, y)


def startUniformityCalib():
    openCalibrationOptionalMenuMouse()
    x, y = loc.shading()
    if x <= 0 and y <= 0:
        return
    pg.moveTo(x, y, duration=0.5)
    pg.click(x, y)


def openMCU():
    if process_exists('MUTL.exe'):
        return openWindow('PC-MUTL')
    openApp('MCU')


def closeMUTL():
    name = 'MUTL.exe'
    closeApp(name)


# __________________________________________________________________
def openWindow(name):
    def handler(hwnd, active):
        if w.IsWindowVisible(hwnd):
            wname = w.GetWindowText(hwnd)
            if active in wname:
                w.SetForegroundWindow(hwnd)
                w.ShowWindow(hwnd, c.SW_MAXIMIZE)
    w.EnumWindows(handler, name)


def scanWindows():
    file = open("windowNames.txt", "w")
    def handler(hwnd, param):
        if w.IsWindowVisible(hwnd):
            wname = w.GetWindowText(hwnd)
            size = len(wname)
            if size > 0:
                file.writelines(wname+'\n')
    w.EnumWindows(handler, None)
    file.close()


def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call)
    # print(output)
    output = output.decode('latin-1')
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    #print(last_line)
    # print(last_line)
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())


def openApp(appName):
    try:
        if appName == 'RUPCTOOL':
            route = 'C:\Program Files\Fujifilm\FCR\TOOL\RuPcTool\\'
            exe = 'RuPcTool'
            args = ''
            subprocess.Popen(route + exe + args)

        elif appName == 'Chrome':
            route = 'C:\Program Files\Google\Chrome\Application\\'
            exe = 'chrome'
            args = ''
            subprocess.Popen(route + exe + args)

        elif appName == 'MU':
            route = 'C:\Program Files\FujiFilm\FCR\TOOL\MUTL\\'
            exe = 'MUTL'
            args = ' /IP:192.168.0.100 /RUNAME:MU0 /TYPE:FDR-2500A'
            subprocess.Popen(route + exe + args)

        elif appName == 'MCU':
            route = 'C:\Program Files\FujiFilm\FCR\TOOL\MUTL\\'
            exe = 'MUTL'
            args = ' /IP:192.168.0.101 /RUNAME:MCU0 /TYPE:FDR-3000 /FCR:C:\Program Files\FujiFilm\FCR\FDR-3000DRL\SYSTEM\\192.168.0.101'
            subprocess.Popen(route + exe + args)

        elif appName == 'PING':
            route = 'C:\Windows\System32\\'
            exe = 'PING'
            args = ' 192.168.0.2 /t'
            subprocess.Popen(route + exe + args)

    except FileNotFoundError:
        print('File not found')


def closeApp(appName):
    if process_exists(appName):
        subprocess.call(["taskkill", "/F", "/IM", appName],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def getMacList():
    call = 'getmac'
    output = subprocess.check_output(call)
    output = output.decode('latin-1').strip().split('\r\n')
    macs = output[2:]
    macList = []
    for m in macs:
        line = m.strip().split('   ')
        mac = line[0]
        macList.append(mac.replace('-',':')) if mac != 'N/A' else 0
    text = '\n'.join(macList)
    return text


def getMac(ip):
    call = 'arp', '-a'
    output = subprocess.check_output(call)
    output = output.decode('latin-1').strip().split('\r\n')
    lines = output[3:]
    for item in lines:
        line = []
        subarray = item.strip().split(' ')
        for subitem in subarray:
            line.append(subitem) if len(subitem) > 0 else 0
        if line[0] == ip:
            return line[1].replace('-',':')
    return 'IP address not found!'


def saveMACs():
    other = getMacList()
    mcu = getMac('19.168.0.101')
    f = open('macList.txt', 'w')
    f.writelines('LOCAL:\n')
    f.writelines(other+'\n')
    f.writelines('MCU0:\n')
    f.writelines(mcu)
    f.close()