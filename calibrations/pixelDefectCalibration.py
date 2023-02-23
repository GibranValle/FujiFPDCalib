from util.serialCOM import wait4light


def pixedDefectCalib(arduino, exposures=1):
    print("Pixel defect calibration selected")
    print("Estimated waiting time: 5 mins")
    print("Exposures required: "+exposures)
    # exposures loop
    print(f"\nRequesting exposure {i} of {exposures}")
    dataLost = communicate("S", "S", 1, arduino)
    if dataLost:
        print("Communication error")
        return

    # wait 10 secs OR wait light to turn off
    wait4light(arduino, "Under exposure...", 10, False)

    print("\nRequesting end of exposure\n")
    dataLost = communicate("X", "X", 1, arduino)
    if dataLost:
        print("Communication error")
        return
    print("Exposure done")

    print("\nCalibration completed successfully please check AWS")
    print("----------------------------------------------------")
