from Window import Window
from Images import Images
from TrackbarValues import TrackbarValues

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
            EdgesWindow.show('Images.filtered', Images.filtered)
        case 1:
            # TODO: Sobel operator
            EdgesWindow.show('Images.edges', Images.edges)
        case _:
            return


"""
Trackbar Functions
"""


def noopFunc(arg):
    print('(noopFunc)', arg)


"""
Window Functions
"""

EdgesWindow = Window('Edges', scale=0.5, offset=(
    round(Images.edges.shape[0]*0.4), 0))
EdgesWindow.addTrackbar(thresholdTrackbar, thresholdValueRange, noopFunc)
EdgesWindow.addTrackbar(displayTrackbar, displayValueRange, noopFunc)
EdgesWindow.show('Images.edges', Images.edges)
