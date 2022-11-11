from Window import Window
from images import grayImage
from filterWindow import showFilter
from TrackbarValues import TrackbarValues

"""
Trackbar Functions
"""

operationTrackbar = 'Operator: '
operationValueRange = (0, 3)
filterTrackbar = 'Filter: '
filterValueRange = (0, 2)


def noopFunc(arg):
    print('(noopFunc)', arg)


def filterOnChange(value):
    if TrackbarValues.filter == value:
        return

    TrackbarValues.updateFilter(value)
    showFilter()

    match TrackbarValues.filter:
        case 0:
            print(f'(filterOnChange): Selected no filter ({value})')
            return
        case 1:
            print(f'(filterOnChange): Selected Gaussian ({value})')
            return
        case 2:
            print(f'(filterOnChange): Selected Median ({value})')
            return
        case _:
            print(f'(filterOnChange): Selected UNKNOWN ({value})')
            return


"""
Window Functions
"""

ImageWindow = Window('Image', scale=0.2, offset=(0, 0))
ImageWindow.addTrackbar(operationTrackbar, operationValueRange, noopFunc)
ImageWindow.addTrackbar(filterTrackbar, filterValueRange, filterOnChange)
ImageWindow.show('grayImage', grayImage)
