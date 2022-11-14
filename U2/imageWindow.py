from Window import Window
from Images import Images
from filterWindow import showFilter
from sobelScharrWindow import showOperator
from TrackbarValues import TrackbarValues

operationTrackbar = 'Operator: '
operationValueRange = (0, 3)
filterTrackbar = 'Filter: '
filterValueRange = (0, 2)

"""
Trackbar Functions
"""


def operatorOnChange(value):
    if TrackbarValues.operator == value:
        return

    TrackbarValues.updateOperator(value)
    showOperator()

    match TrackbarValues.operator:
        case 0:
            selection = 'no operator'
        case 1:
            selection = 'Sobel'
        case 2:
            selection = 'Scharr'
        case 3:
            selection = 'Canny'
        case _:
            selection = 'UNKNOWN'

    print(
        f'(operatorOnChange): Selected {selection} ({TrackbarValues.operator})')


def filterOnChange(value):
    if TrackbarValues.filter == value:
        return

    TrackbarValues.updateFilter(value)
    showFilter()

    selection = ''
    match TrackbarValues.filter:
        case 0:
            selection = 'no filter'
        case 1:
            selection = 'Gaussian'
        case 2:
            selection = 'Median'
        case _:
            selection = 'UNKNOWN'

    print(
        f'(filterOnChange): Selected {selection} ({TrackbarValues.filter})')


"""
Window Functions
"""

ImageWindow = Window('Image', scale=0.2, offset=(0, 0))
ImageWindow.addTrackbar(
    operationTrackbar, operationValueRange, operatorOnChange)
ImageWindow.addTrackbar(filterTrackbar, filterValueRange, filterOnChange)
ImageWindow.show('Images.gray', Images.gray)
