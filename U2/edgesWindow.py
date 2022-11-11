from Window import Window
from images import filteredImage, edgesImage
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
            EdgesWindow.show('filteredImage', filteredImage)
            return
        case 1:
            EdgesWindow.show('filteredImage', edgesImage)  # TODO: Sobel operator
            return
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
    round(edgesImage.shape[0]*0.4), 0))
EdgesWindow.addTrackbar(thresholdTrackbar, thresholdValueRange, noopFunc)
EdgesWindow.addTrackbar(displayTrackbar, displayValueRange, noopFunc)
EdgesWindow.show('edgesImage', edgesImage)
