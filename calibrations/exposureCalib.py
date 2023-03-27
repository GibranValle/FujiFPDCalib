def initMessage(calibName, minutes):
    print(f"{calibName} calibration selected")
    print(f"Estimated waiting time: {minutes} mins")
    print("----------------------------------------------------")


def exposureMessage(current, exposures):
    print(f"<-- Requesting exposure {current} of {exposures} -->", end='')


def endMessage():
    print("Calibration completed successfully please check AWS")
    print("----------------------------------------------------")
