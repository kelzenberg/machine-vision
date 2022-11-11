import cv2
from numpy import interp, arange
from Window import Window
from images import grayImage, filteredImage
from TrackbarValues import TrackbarValues
from utils import runGaussian

"""
Trackbar Functions
"""
sigmaTrackbar = 'Sigma: '
sigmaValueRange = (0, 60)
kernelTrackbar = 'Kernal Size: '
kernelSizeRange = (0, 5)


def sigmaOnChange(value):
    if value == 0 or TrackbarValues.filter != 1:  # off
        TrackbarValues.updateSigma(0)
        FilterWindow.show('grayImage', grayImage)
        return

    valueRange = arange(sigmaValueRange[0]+1, sigmaValueRange[1]+1)
    mappedRange = interp(valueRange, (valueRange.min(),
                         valueRange.max()), (0.1, 6.0))
    mappedValue = round(mappedRange[value - 1], 1)

    if TrackbarValues.sigma == mappedValue:
        return

    print(f'(sigmaOnChange) {TrackbarValues.sigma} to {mappedValue}')
    TrackbarValues.updateSigma(mappedValue)
    FilterWindow.setTrackbar(kernelTrackbar, TrackbarValues.kernel)

    FilterWindow.show('guassian', runGaussian())


def kernelSizeOnChange(value):
    if value == 0 or TrackbarValues.filter != 1:  # off
        TrackbarValues.updateKernel(0)
        FilterWindow.show('grayImage', grayImage)
        return

    mappedValue = arange(1, 10, 2)[value - 1]

    if TrackbarValues.kernel == mappedValue:
        return

    print(f'(kernelSizeOnChange) {TrackbarValues.kernel} to {mappedValue}')
    TrackbarValues.updateKernel(mappedValue)
    FilterWindow.setTrackbar(sigmaTrackbar, TrackbarValues.sigma)

    FilterWindow.show('guassian', runGaussian())


"""
Window Functions
"""

FilterWindow = Window('Filter', scale=0.2, offset=(
    0, round(filteredImage.shape[1]*0.175)))
FilterWindow.addTrackbar(sigmaTrackbar, sigmaValueRange, sigmaOnChange)
FilterWindow.addTrackbar(kernelTrackbar, kernelSizeRange, kernelSizeOnChange)
FilterWindow.show('filteredImage', filteredImage)
