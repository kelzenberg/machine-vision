from numpy import interp, arange
from Window import Window
from Images import Images
from TrackbarValues import TrackbarValues
from sobelScharrWindow import updateSobelScharrWindow
from cannyWindow import updateCannyWindow
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


def updateFilterWindow():
    match TrackbarValues.filter:
        case 0:  # no Filter = reset Image
            Images.updateFiltered(Images.gray.copy())
            FilterWindow.show('Gray', Images.filtered)
        case 1:
            FilterWindow.show('Gaussian', runGaussian())
        case 2:
            resetSigmaValue()  # prevent sigma effect on Median filter
            FilterWindow.show('Median', runMedian())
        case _:
            pass

    match TrackbarValues.operator:
        case 0:  # no Operator
            updateSobelScharrWindow()
        case 1:
            updateSobelScharrWindow()
        case 2:
            updateSobelScharrWindow()
        case 3:
            updateCannyWindow()
            pass
        case _:
            pass


"""
Trackbar Functions
"""


def sigmaOnChange(value):
    if TrackbarValues.filter == 2:
        resetSigmaValue()  # prevent sigma effect on Median filter
        return

    if value == 0:
        if TrackbarValues.sigma != value:
            print(f'(sigmaOnChange) off')

        updateSigmaValue(0)
        FilterWindow.show('Images.gray', Images.gray)
        return

    valueRange = arange(sigmaValueRange[0]+1, sigmaValueRange[1]+1)
    mappedRange = interp(valueRange, (valueRange.min(),
                         valueRange.max()), (0.1, 6.0))
    mappedValue = round(mappedRange[value - 1], 1)

    if TrackbarValues.sigma == mappedValue:
        return

    print(f'(sigmaOnChange) {TrackbarValues.sigma} to {mappedValue}')
    updateSigmaValue(mappedValue)

    updateFilterWindow()


def kernelSizeOnChange(value):
    if value == 0:
        if TrackbarValues.kernel != value:
            print(f'(kernelSizeOnChange) off')

        updateKernelValue(0)
        FilterWindow.show('Images.gray', Images.gray)
        return

    mappedValue = arange(1, 10, 2)[value - 1]

    if TrackbarValues.kernel == mappedValue:
        return

    print(f'(kernelSizeOnChange) {TrackbarValues.kernel} to {mappedValue}')
    updateKernelValue(mappedValue)

    updateFilterWindow()


"""
Window Functions
"""

FilterWindow = Window('Filter', scale=0.2, offset=(
    0, round(Images.filtered.shape[1]*0.175)))
FilterWindow.addTrackbar(sigmaTrackbar, sigmaValueRange, sigmaOnChange)
FilterWindow.addTrackbar(kernelTrackbar, kernelSizeRange, kernelSizeOnChange)
FilterWindow.show('Images.filtered', Images.filtered)
