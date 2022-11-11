from Window import Window
from Images import Images
from filterWindow import showFilter
from edgesWindow import showOperator
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
            print(f'(operatorOnChange): Selected no operator ({value})')
            return
        case 1:
            print(f'(operatorOnChange): Selected Sobel ({value})')
            return
        case _:
            print(f'(operatorOnChange): Selected UNKNOWN ({value})')
            return


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
ImageWindow.addTrackbar(
    operationTrackbar, operationValueRange, operatorOnChange)
ImageWindow.addTrackbar(filterTrackbar, filterValueRange, filterOnChange)
ImageWindow.show('Images.gray', Images.gray)
