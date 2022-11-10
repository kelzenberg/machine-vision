from Window import Window
from images import filteredImage

"""
Trackbar Functions
"""

sigmaValue = 0.1
sigmaValueRange = (0, 60)
kernelSizeRange = (0, 5)


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

FilterWindow = Window('Filter', scale=0.2, offset=(
    0, round(filteredImage.shape[1]*0.175)))
FilterWindow.addTrackbar('Sigma: ', sigmaValueRange, sigmaOnChange)
FilterWindow.addTrackbar('Kernal Size: ', kernelSizeRange, kernelSizeOnChange)
FilterWindow.show('filteredImage', filteredImage)
