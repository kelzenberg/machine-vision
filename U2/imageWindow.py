from Window import Window
from images import grayImage

"""
Trackbar Functions
"""

filterValue = 0

operationValueRange = (0, 3)
filterValueRange = (0, 2)

def noopFunc(arg):
    print('(noopFunc)', arg)


def filterOnChange(value):
    global filterValue
    if filterValue == value:
        return

    filterValue = value
    print('(filterOnChange)', filterValue)

    match filterValue:
        case 1:
            print(filterValue)


"""
Window Functions
"""

ImageWindow = Window('Image', scale=0.2, offset=(0, 0))
ImageWindow.addTrackbar('Operation: ', operationValueRange, noopFunc)
ImageWindow.addTrackbar('Filter: ', filterValueRange, filterOnChange)
ImageWindow.show('grayImage', grayImage)
