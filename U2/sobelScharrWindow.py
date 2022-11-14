from cv2 import Sobel
from Window import Window
from Images import Images
from TrackbarValues import TrackbarValues
from utils import runWithThreshold

SobelScharrWindow = None
thresholdTrackbar = 'Threshold: '
thresholdValueRange = (0, 256)
displayTrackbar = 'Display Image: '
displayValueRange = (0, 4)

"""
Sobel & Scharr Utils
"""


def updateDisplay():
    match TrackbarValues.displayValue:
        case 0:
            SobelScharrWindow.show('Filtered', Images.filtered)
        case 1:
            SobelScharrWindow.show('Binary', Images.binary)
        case 2:
            SobelScharrWindow.show('GradientX', Images.gradientX)
        case 3:
            SobelScharrWindow.show('GradientY', Images.gradientY)
        case 4:
            SobelScharrWindow.show('SumXY', Images.sumXY)
        case _:
            return


def updateSobelScharrWindow():
    match TrackbarValues.operator:
        case 0:
            TrackbarValues.updateThreshold(0)
            SobelScharrWindow.setTrackbar(
                thresholdTrackbar, TrackbarValues.threshold)

            TrackbarValues.updateDisplayValue(0)
            SobelScharrWindow.setTrackbar(
                displayTrackbar, TrackbarValues.displayValue)
        case 1:
            runWithThreshold('sobel')
        case 2:
            runWithThreshold('scharr')
        case _:
            pass

    updateDisplay()


"""
Trackbar Functions
"""


def thresholdOnChange(value):
    if TrackbarValues.threshold == value:
        return

    print(f'(thresholdOnChange) {TrackbarValues.threshold} to {value}')
    TrackbarValues.updateThreshold(value)

    updateSobelScharrWindow()


def displayValueOnChange(value):
    if TrackbarValues.displayValue == value:
        return

    print(f'(displayValueOnChange) {TrackbarValues.displayValue} to {value}')
    TrackbarValues.updateDisplayValue(value)

    updateSobelScharrWindow()


"""
Window Functions
"""


def createSobelScharrWindow():
    global SobelScharrWindow

    if SobelScharrWindow != None:
        SobelScharrWindow.destroy()

    SobelScharrWindow = Window('Operator Sobel & Scharr', scale=0.5, offset=(
        round(Images.filtered.shape[0]*0.4), 0))
    SobelScharrWindow.addTrackbar(
        thresholdTrackbar, thresholdValueRange, thresholdOnChange)
    SobelScharrWindow.addTrackbar(
        displayTrackbar, displayValueRange, displayValueOnChange)


createSobelScharrWindow()
SobelScharrWindow.show('Images.filtered', Images.filtered)
