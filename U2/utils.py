import cv2
from numpy import zeros
from TrackbarValues import TrackbarValues
from Images import Images

"""
Utility functions
"""

imageDepth = cv2.CV_16S
borderType = cv2.BORDER_REFLECT_101


def runGaussian():
    multiplier = 6
    Images.updateFiltered(cv2.GaussianBlur(Images.gray.copy(), (TrackbarValues.kernel *
                          multiplier + 1, TrackbarValues.kernel * multiplier + 1), TrackbarValues.sigma, borderType))
    return Images.filtered


def runMedian():
    multiplier = 2
    Images.updateFiltered(cv2.medianBlur(
        Images.gray.copy(), TrackbarValues.kernel * multiplier + 1))
    return Images.filtered


def runSobel(image):
    gradientX = cv2.convertScaleAbs(
        cv2.Sobel(image, imageDepth, 1, 0, borderType))
    gradientY = cv2.convertScaleAbs(
        cv2.Sobel(image, imageDepth, 0, 1, borderType))
    maxXY = cv2.max(gradientX, gradientY)
    sumXY = cv2.addWeighted(gradientX, 0.5, gradientY, 0.5, 0)
    return [gradientX, gradientY, maxXY, sumXY]


def runScharr(image):
    gradientX = cv2.convertScaleAbs(cv2.Scharr(
        image, imageDepth, 1, 0, borderType))
    gradientY = cv2.convertScaleAbs(cv2.Scharr(
        image, imageDepth, 0, 1, borderType))
    maxXY = cv2.max(gradientX, gradientY)
    sumXY = cv2.addWeighted(gradientX, 0.5, gradientY, 0.5, 0)
    return [gradientX, gradientY, maxXY, sumXY]


def runWithThreshold(opType):
    image = Images.filtered.copy()

    match opType:
        case 'sobel':
            [gradientX, gradientY, maxXY, sumXY] = runSobel(image)
        case 'scharr':
            [gradientX, gradientY, maxXY, sumXY] = runScharr(image)

    _, binary = cv2.threshold(
        sumXY, TrackbarValues.threshold - 1, 255, cv2.THRESH_BINARY)

    Images.updateGradientX(cv2.bitwise_not(gradientX))
    Images.updateGradientY(cv2.bitwise_not(gradientY))
    Images.updateMaxXY(cv2.bitwise_not(maxXY))
    Images.updateSumXY(cv2.bitwise_not(sumXY))
    Images.updateBinary(cv2.bitwise_not(binary))


def runCanny():
    image = Images.filtered.copy()

    if TrackbarValues.threshold > 0 or TrackbarValues.threshold2 > 0:
        image = cv2.bitwise_not(
            cv2.Canny(image, TrackbarValues.threshold - 1, TrackbarValues.threshold2 - 1))

    Images.updateCanny(image)


def runDoG():
    image = Images.filtered.copy()
    lowpass1 = cv2.GaussianBlur(
        image, (7, 7), TrackbarValues.sigmaL, borderType)
    lowpass2 = cv2.GaussianBlur(
        image, (7, 7), TrackbarValues.sigmaH, borderType)
    outputImage = zeros(image.shape)
    difference = cv2.normalize(cv2.subtract(
        lowpass1, lowpass2), outputImage, alpha=255, beta=0, norm_type=cv2.NORM_MINMAX)
    _, binary = cv2.threshold(
        difference, TrackbarValues.threshold - 1, 255, cv2.THRESH_BINARY)

    Images.updateLowpass1(lowpass1)
    Images.updateLowpass2(lowpass2)
    Images.updateDifference(cv2.bitwise_not(difference))
    Images.updateBinary(cv2.bitwise_not(binary))
