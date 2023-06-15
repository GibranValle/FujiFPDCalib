import os

from calibrations.exposureCalibration import defectSolidCalib, pixedDefectCalib, shadingCalib, uniformityCalib,\
    defectSolidStereoCalib, defectSolidTomoCalib, defectSolidBpyCalib, uniformityCalibStereo, uniformityCalibBpy, \
    uniformityCalibTomo, uniformityCalibES
import util.location as loc
import shell.process as pro


def generateMenu(options):
    menu = ''
    for index, option in enumerate(options):
        if index != 0 and index != (len(options) - 1):
            menu += f' {index}) {option}\n'
            continue
        elif index == (len(options) - 1):
            menu += f'{option}'
        else:
            menu += f'{option}\n'
    return menu


def main():
    options = [
        '\rAvailable emulator modes:',
        'EXIT',
        'Basic FPD',
        'Stereo Bpy FPD',
        'Tomo FPD',
        'ES FPD',
        'mA full Calibration',
        'IconLocation[Test]',
        'Automatic HS',
        'Window',
        'Save MAC list',
        'selection: '
    ]
    return generateMenu(options)


def basic():
    options = [
        'Basic FPD options:',
        'RETURN TO MAIN MENU',
        'Defect-solid',
        'Pixel-defect',
        'Shading',
        'X-ray uniformity',
        'selection: '
    ]
    return generateMenu(options)


def runBasic(option):
    if option == '1':
        return -1
    elif option == '2':
        defectSolidCalib()
    elif option == '3':
        pixedDefectCalib()
    elif option == '4':
        shadingCalib()
    elif option == '5':
        uniformityCalib()
    else:
        return


def stereoBpy():
    options = [
        'Stereo Bpy FPD options:',
        'RETURN TO MAIN MENU',
        'Defect-solid (Stereo)',
        'Defect-solid (Bpy)',
        'X-ray uniformity (Stereo)',
        'X-ray uniformity (Bpy)',
        'selection: '
    ]
    return generateMenu(options)


def runStereo(option):
    if option == '2':
        defectSolidStereoCalib()
    elif option == '3':
        defectSolidBpyCalib()
    elif option == '4':
        uniformityCalibStereo()
    elif option == '5':
        uniformityCalibBpy()
    else:
        return


def tomo():
    options = [
        'Tomo FPD options:',
        'RETURN TO MAIN MENU',
        'Defect-solid',
        'X-ray uniformity',
        'selection: '
    ]
    return generateMenu(options)


def runTomo(option):
    if option == '2':
        defectSolidTomoCalib()
    elif option == '3':
        uniformityCalibTomo()
    else:
        return


def ES():
    options = [
        'ES FPD options:',
        'RETURN TO MAIN MENU',
        'X-ray uniformity',
        'selection: '
    ]
    return generateMenu(options)


def runES(option):
    if option == '2':
        uniformityCalibES()
    else:
        return


def iconTest():
    options = [
        'Icon identification options:',
        'RETURN TO MAIN MENU',
        'AWS status icons',
        'RUPCTools icons',
        'MUTL icons',
        'FPD Calib icons',
        'FPD Calib Opt icons',
        'selection: '
    ]
    return generateMenu(options)


def AWSicons():
    options = [
        'AWS icon options:',
        'RETURN TO MAIN MENU',
        'Stand by',
        'Blocked',
        'Ok red',
        'Calib button',
        'Field calib button',
        'selection: '
    ]
    return generateMenu(options)


def runAWS(option):
    if option == '2':
        return loc.stdbyIcon()
    elif option == '3':
        return loc.blockedIcon()
    elif option == '4':
        return loc.okExposure()
    elif option == '5':
        return loc.calib_button()
    elif option == '6':
        return loc.fieldCalib()
    else:
        return print('Option not found')



def ruIcons():
    options = [
        'RUPCTools icon options:',
        'RETURN TO MAIN MENU',
        'MU0',
        'MCU0',
        'New',
        'Install',
        'selection: '
    ]
    return generateMenu(options)


def runRuIcons(option):
    if option == '2':
        return loc.MU0()
    elif option == '3':
        return loc.MCU0()
    elif option == '4':
        return loc.new()
    elif option == '5':
        return loc.install()
    else:
        return -1, -1


def mutlIcons():
    options = [
        'MUTL icon options:',
        'RETURN TO MAIN MENU',
        'calibration',
        'calibration (opt)',
        'left',
        'right',
        'selection: '
    ]
    return generateMenu(options)


def runMutl(option):
    if option == '2':
        return loc.calibration()
    elif option == '3':
        return loc.calibrationOptional()
    elif option == '4':
        return loc.left()
    elif option == '5':
        return loc.right()
    else:
        return -1, -1


def fpdCalib():
    options = [
        'MUTL icon options:',
        'RETURN TO MAIN MENU',
        'offset',
        'defect',
        'defect solid',
        'pixel defect',
        'shading',
        'uniformity',
        'sensitivity',
        'selection: '
    ]
    return generateMenu(options)


def runfpdCalib(option):
    if option == '2':
        return loc.offset()
    elif option == '3':
        return loc.defect()
    elif option == '4':
        return loc.defectSolid()
    elif option == '5':
        return loc.pixelDefect()
    elif option == '6':
        return loc.shading()
    elif option == '7':
        return loc.uniformity()
    elif option == '8':
        return loc.sensitivity()
    else:
        return -1, -1


def fpdOptional():
    options = [
        'MUTL icon options:',
        'RETURN TO MAIN MENU',
        'defect solid stereo',
        'defect solid biopsy',
        'defect solid tomo',
        'x-ray uniformity stereo',
        'x-ray uniformity biopsy',
        'x-ray uniformity tomo',
        'x-ray uniformity ES',
        'selection: '
    ]
    return generateMenu(options)


def runOptionalCalib(option):
    if option == '2':
        return loc.defectSolidStereo()
    elif option == '3':
        return loc.defectSolidBpy()
    elif option == '4':
        return loc.defectSolidTomo()
    elif option == '5':
        return loc.uniformityStereo()
    elif option == '6':
        return loc.uniformityBpy()
    elif option == '7':
        return loc.uniformityTomo()
    elif option == '8':
        return loc.uniformityES()
    else:
        return -2, -2


def window():
    options = [
        'Window options:',
        'RETURN TO MAIN MENU',
        'open RU',
        'close RU',
        'open MCU [MOUSE]',
        'open MCU [IN DEVELOPMENT]',
        'close MCU',
        'open calibration menu [MOUSE]',
        'open calibration (optional) menu [MOUSE]',
        'Start Shading calibration [Mouse]',
        'Start Uniformity calibration [Mouse]',
        'selection: '
    ]
    return generateMenu(options)


def runWindow(option):
    if option == '1':
        return -1
    elif option == '2':
        return pro.openRU()
    elif option == '3':
        return pro.closeRU()
    elif option == '4':
        return pro.openMUTLMouse()
    elif option == '6':
        return pro.closeMUTL()
    elif option == '7':
        return pro.closeMUTL()
    elif option == '8':
        return pro.openCalibrationMenuMouse()
    elif option == '9':
        return pro.openCalibrationOptionalMenuMouse()
    elif option == '10':
        return pro.startShadingCalib()
    elif option == '11':
        return pro.startUniformityCalib()
    else:
        return -1
