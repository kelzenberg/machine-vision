import cv2
from TrackbarValues import TrackbarValues
from Images import Images

"""
Utility functions
"""

borderType = cv2.BORDER_REFLECT_101


def runGaussian():
    multiplier = 2
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
        cv2.Sobel(image, cv2.CV_16S, 1, 0, borderType))
    gradientY = cv2.convertScaleAbs(
        cv2.Sobel(image, cv2.CV_16S, 0, 1, borderType))
    sumXY = cv2.addWeighted(gradientX, 0.5, gradientY, 0.5, 0)
    return [gradientX, gradientY, sumXY]


def runScharr(image):
    gradientX = cv2.convertScaleAbs(cv2.Scharr(
        image, cv2.CV_16S, 1, 0, borderType))
    gradientY = cv2.convertScaleAbs(cv2.Scharr(
        image, cv2.CV_16S, 0, 1, borderType))
    sumXY = cv2.addWeighted(gradientX, 0.5, gradientY, 0.5, 0)
    return [gradientX, gradientY, sumXY]


def runWithThreshold(opType):
    image = Images.filtered.copy()

    if 0 < TrackbarValues.threshold < 256:
        _, image = cv2.threshold(
            image, TrackbarValues.threshold - 1, 255, cv2.THRESH_BINARY)

    match opType:
        case 'sobel':
            [gradientX, gradientY, sumXY] = runSobel(image)
        case 'scharr':
            [gradientX, gradientY, sumXY] = runScharr(image)

    Images.updateBinary(image)
    Images.updateGradientX(gradientX)
    Images.updateGradientY(gradientY)
    Images.updateSumXY(sumXY)


def runCanny():
    image = Images.filtered.copy()

    if 0 < TrackbarValues.threshold < 301 and 0 < TrackbarValues.threshold2 < 301:
        image = cv2.Canny(image, TrackbarValues.threshold - 1,
                          TrackbarValues.threshold2 - 1)

    Images.updateCanny(image)
