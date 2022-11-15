from Window import Window
from Images import Images
from TrackbarValues import TrackbarValues
from utils import runWithThreshold

DoGWindow = None
sigmaLTrackbar = 'Sigma L: '
sigmaLValueRange = (0, 600)
sigmaHTrackbar = 'Sigma H: '
sigmaHValueRange = (0, 600)
thresholdTrackbar = 'Threshold: '
thresholdValueRange = (0, 255)
displayTrackbar = 'Display Image: '
displayValueRange = (0, 4)

"""
DoG Utils
"""


def updateDisplay():
    match TrackbarValues.displayValue:
        case 0:
            DoGWindow.setTrackbar(thresholdTrackbar, 0)
            DoGWindow.show('Filtered', Images.filtered)
        case 1:
            DoGWindow.setTrackbar(thresholdTrackbar, 0)
            DoGWindow.show('Lowpass1', Images.lowpass1)
        case 2:
            DoGWindow.setTrackbar(thresholdTrackbar, 0)
            DoGWindow.show('Lowpass2', Images.lowpass2)
        case 3:
            DoGWindow.setTrackbar(thresholdTrackbar, 0)
            DoGWindow.show('Difference', Images.difference)
        case 4:
            DoGWindow.show('Binary', Images.binary)
        case _:
            return


def updateDoGWindow():
    match TrackbarValues.operator:
        case 0:
            TrackbarValues.updateThreshold(0)
            DoGWindow.setTrackbar(
                thresholdTrackbar, TrackbarValues.threshold)

            TrackbarValues.updateDisplayValue(0)
            DoGWindow.setTrackbar(
                displayTrackbar, TrackbarValues.displayValue)
        case 4:
            # TODO: runDoG()
            pass
        case _:
            pass

    updateDisplay()


"""
Trackbar Functions
"""


def sigmaLOnChange(value):
    if TrackbarValues.sigmaL == value:
        return

    print(f'(sigmaLOnChange) {TrackbarValues.sigmaL} to {value}')
    TrackbarValues.updateSigmaL(value)

    updateDoGWindow()


def sigmaHOnChange(value):
    if TrackbarValues.sigmaH == value:
        return

    print(f'(sigmaHOnChange) {TrackbarValues.sigmaH} to {value}')
    TrackbarValues.updateSigmaH(value)

    updateDoGWindow()


def thresholdOnChange(value):
    if TrackbarValues.threshold == value:
        return

    print(f'(thresholdOnChange) {TrackbarValues.threshold} to {value}')
    TrackbarValues.updateThreshold(value)

    updateDoGWindow()


def displayValueOnChange(value):
    if TrackbarValues.displayValue == value:
        return

    print(f'(displayValueOnChange) {TrackbarValues.displayValue} to {value}')
    TrackbarValues.updateDisplayValue(value)

    updateDoGWindow()


"""
Window Functions
"""


def createDoGWindow():
    global DoGWindow

    if DoGWindow != None:
        DoGWindow.destroy()

    DoGWindow = Window('Operator DoG', scale=0.5, offset=(
        round(Images.filtered.shape[0]*0.4), 0))
    DoGWindow.addTrackbar(
        sigmaLTrackbar, sigmaLValueRange, sigmaLOnChange)
    DoGWindow.addTrackbar(
        sigmaHTrackbar, sigmaHValueRange, sigmaHOnChange)
    DoGWindow.addTrackbar(
        thresholdTrackbar, thresholdValueRange, thresholdOnChange)
    DoGWindow.addTrackbar(
        displayTrackbar, displayValueRange, displayValueOnChange)
    return DoGWindow
