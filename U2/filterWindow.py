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


def updateSigma(value):
    TrackbarValues.updateSigma(value)
    FilterWindow.setTrackbar(kernelTrackbar, TrackbarValues.kernel)


def updateKernel(value):
    TrackbarValues.updateKernel(value)
    FilterWindow.setTrackbar(sigmaTrackbar, TrackbarValues.sigma)


def sigmaOnChange(value):
    if value == 0:
        print(f'(sigmaOnChange) off')
        updateSigma(0)
        FilterWindow.show('grayImage', grayImage)
        return

    valueRange = arange(sigmaValueRange[0]+1, sigmaValueRange[1]+1)
    mappedRange = interp(valueRange, (valueRange.min(),
                         valueRange.max()), (0.1, 6.0))
    mappedValue = round(mappedRange[value - 1], 1)

    if TrackbarValues.sigma == mappedValue:
        return

    print(f'(sigmaOnChange) {TrackbarValues.sigma} to {mappedValue}')
    updateSigma(mappedValue)

    if TrackbarValues.filter == 1:
        FilterWindow.show('guassian', runGaussian())


def kernelSizeOnChange(value):
    if value == 0:
        print(f'(kernelSizeOnChange) off')
        updateKernel(0)
        FilterWindow.show('grayImage', grayImage)
        return

    mappedValue = arange(1, 10, 2)[value - 1]

    if TrackbarValues.kernel == mappedValue:
        return

    print(f'(kernelSizeOnChange) {TrackbarValues.kernel} to {mappedValue}')
    updateKernel(mappedValue)

    if TrackbarValues.filter == 1:
        FilterWindow.show('guassian', runGaussian())


"""
Window Functions
"""

FilterWindow = Window('Filter', scale=0.2, offset=(
    0, round(filteredImage.shape[1]*0.175)))
FilterWindow.addTrackbar(sigmaTrackbar, sigmaValueRange, sigmaOnChange)
FilterWindow.addTrackbar(kernelTrackbar, kernelSizeRange, kernelSizeOnChange)
FilterWindow.show('filteredImage', filteredImage)
