import cv2
from TrackbarValues import TrackbarValues
from Images import Images

"""
Utility functions
"""


def runGaussian():
    multiplier = 6
    Images.updateFiltered(cv2.GaussianBlur(Images.gray.copy(), (TrackbarValues.kernel * multiplier + 1,
                                                                TrackbarValues.kernel * multiplier + 1), TrackbarValues.sigma, borderType=cv2.BORDER_REFLECT_101))
    return Images.filtered


def runMedian():
    multiplier = 6
    Images.updateFiltered(cv2.medianBlur(
        Images.gray.copy(), TrackbarValues.kernel * multiplier + 1))
    return Images.filtered


def runSobel(image):
    gradientX = cv2.convertScaleAbs(
        cv2.Sobel(image, cv2.CV_64F, 1, 0, borderType=cv2.BORDER_REFLECT_101))
    gradientY = cv2.convertScaleAbs(
        cv2.Sobel(image, cv2.CV_64F, 0, 1, borderType=cv2.BORDER_REFLECT_101))
    sumXY = cv2.addWeighted(gradientX, 0.5, gradientY, 0.5, 0)
    return [gradientX, gradientY, sumXY]


def runSobelWithThreshold():
    image = Images.filtered.copy()

    if 0 < TrackbarValues.threshold < 257:
        _, image = cv2.threshold(
            image, TrackbarValues.threshold, 255, cv2.THRESH_BINARY)

    [gradientX, gradientY, sumXY] = runSobel(image)
    Images.updateBinary(image)
    Images.updateGradientX(gradientX)
    Images.updateGradientY(gradientY)
    Images.updateSumXY(sumXY)
