from numpy import interp, arange
from Window import Window
from images import grayImage, filteredImage
from TrackbarValues import TrackbarValues
from utils import runGaussian, runMedian

sigmaTrackbar = 'Sigma: '
sigmaValueRange = (0, 60)
kernelTrackbar = 'Kernal Size: '
kernelSizeRange = (0, 5)

"""
Filter Utils
"""


def resetSigmaValue():
    TrackbarValues.updateSigma(0)
    FilterWindow.setTrackbar(sigmaTrackbar, 0)


def updateSigmaValue(value):
    TrackbarValues.updateSigma(value)
    TrackbarValues.updateKernel(1)  # needed for sigma
    FilterWindow.setTrackbar(kernelTrackbar, TrackbarValues.kernel)


def updateKernelValue(value):
    TrackbarValues.updateKernel(value)
    TrackbarValues.updateSigma(0)  # needed to not overwrite kernel
    FilterWindow.setTrackbar(sigmaTrackbar, TrackbarValues.sigma)


def showFilter():
    match TrackbarValues.filter:
        case 0:  # no Filter = reset Image
            FilterWindow.show('grayImage', grayImage)
            return
        case 1:
            FilterWindow.show('guassian', runGaussian())
            return
        case 2:
            resetSigmaValue()  # prevent sigma effect on Median filter
            FilterWindow.show('median', runMedian())
            return
        case _:
            return


"""
Trackbar Functions
"""


def sigmaOnChange(value):
    if TrackbarValues.filter == 2:
        resetSigmaValue()  # prevent sigma effect on Median filter
        return

    if value == 0:
        print(f'(sigmaOnChange) off')
        updateSigmaValue(0)
        FilterWindow.show('grayImage', grayImage)
        return

    valueRange = arange(sigmaValueRange[0]+1, sigmaValueRange[1]+1)
    mappedRange = interp(valueRange, (valueRange.min(),
                         valueRange.max()), (0.1, 6.0))
    mappedValue = round(mappedRange[value - 1], 1)

    if TrackbarValues.sigma == mappedValue:
        return

    print(f'(sigmaOnChange) {TrackbarValues.sigma} to {mappedValue}')
    updateSigmaValue(mappedValue)

    showFilter()


def kernelSizeOnChange(value):
    if value == 0:
        print(f'(kernelSizeOnChange) off')
        updateKernelValue(0)
        FilterWindow.show('grayImage', grayImage)
        return

    mappedValue = arange(1, 10, 2)[value - 1]

    if TrackbarValues.kernel == mappedValue:
        return

    print(f'(kernelSizeOnChange) {TrackbarValues.kernel} to {mappedValue}')
    updateKernelValue(mappedValue)

    showFilter()


"""
Window Functions
"""

FilterWindow = Window('Filter', scale=0.2, offset=(
    0, round(filteredImage.shape[1]*0.175)))
FilterWindow.addTrackbar(sigmaTrackbar, sigmaValueRange, sigmaOnChange)
FilterWindow.addTrackbar(kernelTrackbar, kernelSizeRange, kernelSizeOnChange)
FilterWindow.show('filteredImage', filteredImage)
