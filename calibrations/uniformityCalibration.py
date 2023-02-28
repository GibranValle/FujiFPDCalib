from util.serialCOM import communicate


def uniformityCalib(arduino, exposures=7):
    print("X-Ray Uniformity calibration selected")
    print("Estimated waiting time: 10 mins")
    print("Exposures required: "+exposures)
    # exposures loop
    for i in range(1, exposures):
        print(f"\nRequesting exposure {i} of {exposures}")
        comError = communicate("S")
        if comError:
            return

        # wait 10 secs OR wait light to turn off
        wait4light(arduino, "Under exposure...", 10, False)

        print("\nRequesting end of exposure\n")
        comError = communicate("X")
        if comError:
            return
        print("Exposure done")

        # wait 25 secs or wait light to turn ON
        wait4light(arduino, "Preparing for next exposure...", 25, True)
    print("Calibration completed successfully please check AWS")
    print("----------------------------------------------------")


