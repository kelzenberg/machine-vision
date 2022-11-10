from Window import Window
from images import grayImage

"""
Trackbar Functions
"""

filterValue = 0


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
ImageWindow.addTrackbar('Operation: ', 0, 3, noopFunc)
ImageWindow.addTrackbar('Filter: ', 0, 2, filterOnChange)
ImageWindow.show('grayImage', grayImage)
