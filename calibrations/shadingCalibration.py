from util.serialCOM import communicate, wait4light


def shadingCalib(arduino, exposures=44):
    print("Shading calibration selected")
    print("Estimated waiting time: 30 mins")
    print("Exposures required: "+exposures)
    # exposures loop
    for i in range(1, exposures):
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

        # wait 25 secs or wait light to turn ON
        wait4light(arduino, "Preparing for next exposure...", 25, True)

    print("\nCalibration completed successfully please check AWS")
    print("----------------------------------------------------")
