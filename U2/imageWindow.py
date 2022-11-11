from Window import Window
from images import grayImage
from TrackbarValues import TrackbarValues

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

    match value:
        case 0:
            return
        case 1:
            print(
                f'(filterOnChange): Selected Gaussian (value {value})')
        case _:
            return

    TrackbarValues.updateFilter(value)


"""
Window Functions
"""

ImageWindow = Window('Image', scale=0.2, offset=(0, 0))
ImageWindow.addTrackbar(operationTrackbar, operationValueRange, noopFunc)
ImageWindow.addTrackbar(filterTrackbar, filterValueRange, filterOnChange)
ImageWindow.show('grayImage', grayImage)
