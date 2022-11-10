from Window import Window
from images import filteredImage

"""
Trackbar Functions
"""

sigmaValue = 0.1


def noopFunc(arg):
    print('(noopFunc)', arg)


def sigmaOnChange(value):
    newValue = (value + 1) / 10

    global sigmaValue
    if sigmaValue == newValue:
        return

    sigmaValue = newValue
    print('(sigma)', sigmaValue)


"""
Window Functions
"""

FilterWindow = Window('Filter', scale=0.2, offset=(0, round(filteredImage.shape[1]*0.175)))
FilterWindow.addTrackbar('Sigma: ', 0, 5, sigmaOnChange)
FilterWindow.addTrackbar('Size: ', 0, 4, noopFunc)
FilterWindow.show('filteredImage', filteredImage)
