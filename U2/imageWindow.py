from Window import Window
from images import grayImage
from TrackbarValues import TrackbarValues

"""
Trackbar Functions
"""

operationValueRange = (0, 3)
filterValueRange = (0, 2)

def noopFunc(arg):
    print('(noopFunc)', arg)


def filterOnChange(value):
    if TrackbarValues.filter == value:
        return

    TrackbarValues.filter = value

    match value:
        case 0:
            return
        case 1:
            print(
                f'(filterOnChange): Selected Gaussian (value {value})')
        case _:
            return


"""
Window Functions
"""

ImageWindow = Window('Image', scale=0.2, offset=(0, 0))
ImageWindow.addTrackbar('Operation: ', operationValueRange, noopFunc)
ImageWindow.addTrackbar('Filter: ', filterValueRange, filterOnChange)
ImageWindow.show('grayImage', grayImage)
