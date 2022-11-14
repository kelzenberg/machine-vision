from Window import Window
from Images import Images
from TrackbarValues import TrackbarValues
from utils import runSobel

thresholdTrackbar = 'Threshold: '
thresholdValueRange = (0, 255)
displayTrackbar = 'Display Image: '
displayValueRange = (0, 5)

"""
Edges Utils
"""


def showOperator():
    match TrackbarValues.operator:
        case 0:  # no Operator = show Filter only
            EdgesWindow.show('Reset to Filtered', Images.filtered)
        case 1:
            EdgesWindow.show('Sobel', runSobel())
        case _:
            return


"""
Trackbar Functions
"""


def thresholdOnChange(value):
    if TrackbarValues.threshold == value:
        return

    print(f'(thresholdOnChange) {TrackbarValues.threshold} to {value}')
    TrackbarValues.updateThreshold(value)

    showOperator()


def noopFunc(arg):
    print('(noopFunc)', arg)


"""
Window Functions
"""

EdgesWindow = Window('Edges', scale=0.5, offset=(
    round(Images.edges.shape[0]*0.4), 0))
EdgesWindow.addTrackbar(
    thresholdTrackbar, thresholdValueRange, thresholdOnChange)
EdgesWindow.addTrackbar(displayTrackbar, displayValueRange, noopFunc)
EdgesWindow.show('Images.edges', Images.edges)
