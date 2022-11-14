from Window import Window
from Images import Images
from TrackbarValues import TrackbarValues
from utils import runWithThreshold

thresholdTrackbar = 'Threshold: '
thresholdValueRange = (0, 257)
displayTrackbar = 'Display Image: '
displayValueRange = (0, 4)

"""
Edges Utils
"""


def showDisplayValue():
    if TrackbarValues.operator == 0:  # no Operator = show Filter only
        TrackbarValues.updateThreshold(0)
        EdgesWindow.setTrackbar(
            thresholdTrackbar, TrackbarValues.threshold)
        TrackbarValues.updateDisplayValue(0)
        EdgesWindow.setTrackbar(
            displayTrackbar, TrackbarValues.displayValue)
        EdgesWindow.show('Reset to Filtered', Images.filtered)

    match TrackbarValues.displayValue:
        case 0:  # show Filtered only
            EdgesWindow.show('Reset to Filtered', Images.filtered)
        case 1:
            EdgesWindow.show('Binary', Images.binary)
        case 2:
            EdgesWindow.show('GradientX', Images.gradientX)
        case 3:
            EdgesWindow.show('GradientY', Images.gradientY)
        case 4:
            EdgesWindow.show('SumXY', Images.sumXY)
        case _:
            return


def showOperator():
    match TrackbarValues.operator:
        case 1:
            runWithThreshold('sobel')
        case 2:
            runWithThreshold('scharr')
        case _:
            pass

    showDisplayValue()


"""
Trackbar Functions
"""


def thresholdOnChange(value):
    if TrackbarValues.threshold == value:
        return

    print(f'(thresholdOnChange) {TrackbarValues.threshold} to {value}')
    TrackbarValues.updateThreshold(value)

    showOperator()


def displayValueOnChange(value):
    if TrackbarValues.displayValue == value:
        return

    print(f'(displayValueOnChange) {TrackbarValues.displayValue} to {value}')
    TrackbarValues.updateDisplayValue(value)

    showOperator()


"""
Window Functions
"""

EdgesWindow = Window('Edges', scale=0.5, offset=(
    round(Images.edges.shape[0]*0.4), 0))
EdgesWindow.addTrackbar(
    thresholdTrackbar, thresholdValueRange, thresholdOnChange)
EdgesWindow.addTrackbar(
    displayTrackbar, displayValueRange, displayValueOnChange)
EdgesWindow.show('Images.edges', Images.edges)
