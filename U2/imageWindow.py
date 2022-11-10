import cv2
from utils import convertToGrayBGR
from Window import Window

"""
Load Image
"""

mainImage = cv2.imread('./Stop.jpg')
grayImage = convertToGrayBGR(mainImage)
print('(main) Image loaded.')

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


"""
Window Functions
"""

window = Window('Image', grayImage)
window.addTrackbar('Operation: ', 0, 3, noopFunc)
window.addTrackbar('Filter: ', 0, 2, filterOnChange)
window.show()
