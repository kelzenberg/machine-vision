from Window import Window
from images import grayImage
from filterWindow import FilterWindow
from TrackbarValues import TrackbarValues
from utils import runGaussian

"""
Trackbar Functions
"""

operationTrackbar = 'Operation: '
operationValueRange = (0, 3)
filterTrackbar = 'Filter: '
filterValueRange = (0, 2)


def noopFunc(arg):
    print('(noopFunc)', arg)


def filterOnChange(value):
    if TrackbarValues.filter == value:
        return

    TrackbarValues.updateFilter(value)

    match value:
        case 0:
            print(
                f'(filterOnChange): Selected no filter ({value})')
            FilterWindow.show('grayImage', grayImage)
            return
        case 1:
            print(
                f'(filterOnChange): Selected Gaussian ({value})')
            FilterWindow.show('guassian', runGaussian())
            return
        case _:
            print(
                f'(filterOnChange): Selected UNKNOWN ({value})')
            return


"""
Window Functions
"""

ImageWindow = Window('Image', scale=0.2, offset=(0, 0))
ImageWindow.addTrackbar(operationTrackbar, operationValueRange, noopFunc)
ImageWindow.addTrackbar(filterTrackbar, filterValueRange, filterOnChange)
ImageWindow.show('grayImage', grayImage)
