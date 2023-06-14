import subprocess
import time

import win32gui as w
import win32con as c

MU = MCU = RU = PING = ''
windowNames = []


def openMU():
    global windowNames
    if MU != '':
        openWindow('MU')
        return
    for item in windowNames:
        if 'MU' in item:
            openWindow('MU')
            return
    openApp('MU')


def closeMU():
    global windowNames
    if MU != '':
        closeApp('MU')
        return
    for item in windowNames:
        if 'MU' in item:
            closeApp('MU')
            return
    print('NO MU0 OPENED')


def openMCU():
    global windowNames
    if MCU != '':
        openWindow('MCU')
        return
    for item in windowNames:
        if 'MU' in item:
            openWindow('MCU')
            return
    openApp('MCU')


def closeMCU():
    global windowNames
    if MCU != '':
        closeApp('MCU')
        return
    for item in windowNames:
        if 'MU' in item:
            closeApp('MU')
            return
    print('NO MCU0 OPENED')


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
    global windowNames
    file = open("windowNames.txt", "w")

    def handler(hwnd, param):
        if w.IsWindowVisible(hwnd):
            wname = w.GetWindowText(hwnd)
            size = len(wname)
            if size > 0:
                file.writelines(wname+'\n')
                windowNames.append(wname)
    w.EnumWindows(handler, None)
    file.close()
    return windowNames


def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call)
    # print(output)
    output = output.decode('latin-1')
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    print(last_line)
    # print(last_line)
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())


def openApp(appName):
    global RU, MU, MCU, PING
    try:
        if appName == 'RUPCTOOL':
            route = 'C:\Program Files\Fujifilm\FCR\TOOL\RuPcTool\\'
            exe = 'RuPcTool'
            args = ''
            RU = subprocess.Popen(route + exe + args)

        elif appName == 'MU':
            route = 'C:\Program Files\FujiFilm\FCR\TOOL\MUTL\\'
            exe = 'MUTL'
            args = ' /IP:192.168.0.100 /RUNAME:MU0 /TYPE:FDR-2500A'
            MU = subprocess.Popen(route + exe + args)

        elif appName == 'MCU':
            route = 'C:\Program Files\FujiFilm\FCR\TOOL\MUTL\\'
            exe = 'MUTL'
            args = ' /IP:192.168.0.101 /RUNAME:MCU0 /TYPE:FDR-3000'
            MCU = subprocess.Popen(route + exe + args)

        elif appName == 'PING':
            route = 'C:\Windows\System32\\'
            exe = 'PING'
            args = ' 192.168.0.2 /t'
            PING = subprocess.Popen(route + exe + args)
    except FileNotFoundError:
        print('File not found')


def closeApp(appName):
    global RU, MU, MCU, PING
    try:
        if appName == 'RUPCTOOL':
            RU.terminate()

        elif appName == 'MU':
            MU.terminate()

        elif appName == 'MCU':
            MCU.terminate()

        elif appName == 'PING':
            PING.terminate()
    except AttributeError:
        print('error')


