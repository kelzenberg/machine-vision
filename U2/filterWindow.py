from numpy import interp, arange
from Window import Window
from images import grayImage, filteredImage
from TrackbarValues import TrackbarValues
from utils import runGaussian

"""
Trackbar Functions
"""

sigmaValueRange = (0, 60)
kernelSizeRange = (0, 5)


def sigmaOnChange(value):
    if value == 0 or TrackbarValues.filter != 1:  # off
        TrackbarValues.sigma = 0
        FilterWindow.show('grayImage', grayImage)
        return

    valueRange = arange(sigmaValueRange[0]+1, sigmaValueRange[1]+1)
    mappedRange = interp(valueRange, (valueRange.min(),
                         valueRange.max()), (0.1, 6.0))
    mappedValue = round(mappedRange[value - 1], 1)

    if TrackbarValues.sigma == mappedValue:
        return

    TrackbarValues.kernel = 1
    TrackbarValues.sigma = mappedValue
    print('(sigmaOnChange)', TrackbarValues.sigma)
    FilterWindow.show('guassian', runGaussian())


def kernelSizeOnChange(value):
    if value == 0 or TrackbarValues.filter != 1:  # off
        TrackbarValues.kernel = 0
        FilterWindow.show('grayImage', grayImage)
        return

    mappedValue = arange(1, 10, 2)[value - 1]
    print('foo', TrackbarValues.kernel, mappedValue)

    if TrackbarValues.kernel == mappedValue:
        return

    TrackbarValues.sigma = 0
    TrackbarValues.kernel = mappedValue
    print('(kernelSizeOnChange)', TrackbarValues.kernel)
    FilterWindow.show('guassian', runGaussian())


"""
Window Functions
"""

FilterWindow = Window('Filter', scale=0.2, offset=(
    0, round(filteredImage.shape[1]*0.175)))
FilterWindow.addTrackbar('Sigma: ', sigmaValueRange, sigmaOnChange)
FilterWindow.addTrackbar('Kernal Size: ', kernelSizeRange, kernelSizeOnChange)
FilterWindow.show('filteredImage', filteredImage)
