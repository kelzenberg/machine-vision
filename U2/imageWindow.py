from Window import Window
from Images import Images
from TrackbarValues import TrackbarValues
from filterWindow import updateFilterWindow
from sobelScharrWindow import SobelScharrWindow, updateSobelScharrWindow, createSobelScharrWindow
from cannyWindow import CannyWindow, updateCannyWindow, createCannyWindow

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

    match TrackbarValues.operator:
        case 0:
            selection = 'No Operator'
            if CannyWindow != None:
                CannyWindow.destroy()
            createSobelScharrWindow()
            updateSobelScharrWindow()
        case 1:
            selection = 'Sobel'
            if CannyWindow != None:
                CannyWindow.destroy()
            createSobelScharrWindow()
            updateSobelScharrWindow()
        case 2:
            selection = 'Scharr'
            if CannyWindow != None:
                CannyWindow.destroy()
            createSobelScharrWindow()
            updateSobelScharrWindow()
        case 3:
            selection = 'Canny'
            if SobelScharrWindow != None:
                SobelScharrWindow.destroy()
            createCannyWindow()
            updateCannyWindow()
        case _:
            selection = 'UNKNOWN'

    print(
        f'(operatorOnChange): Selected {selection} ({TrackbarValues.operator})')


def filterOnChange(value):
    if TrackbarValues.filter == value:
        return

    TrackbarValues.updateFilter(value)

    selection = ''
    match TrackbarValues.filter:
        case 0:
            selection = 'No Filter'
        case 1:
            selection = 'Gaussian'
        case 2:
            selection = 'Median'
        case _:
            selection = 'UNKNOWN'

    print(
        f'(filterOnChange): Selected {selection} ({TrackbarValues.filter})')

    updateFilterWindow()


"""
Window Functions
"""

ImageWindow = Window('Image', scale=0.2, offset=(0, 0))
ImageWindow.addTrackbar(
    operationTrackbar, operationValueRange, operatorOnChange)
ImageWindow.addTrackbar(filterTrackbar, filterValueRange, filterOnChange)
ImageWindow.show('Images.gray', Images.gray)
