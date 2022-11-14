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


def runSobel():
    _, threshold = cv2.threshold(Images.filtered.copy(
    ), TrackbarValues.threshold, 255, cv2.THRESH_BINARY)
    gradientX = cv2.convertScaleAbs(
        cv2.Sobel(threshold, cv2.CV_64F, 1, 0, borderType=cv2.BORDER_REFLECT_101))
    Images.updateGradientX(gradientX)
    gradientY = cv2.convertScaleAbs(
        cv2.Sobel(threshold, cv2.CV_64F, 0, 1, borderType=cv2.BORDER_REFLECT_101))
    Images.updateGradientY(gradientY)
    gradient = cv2.addWeighted(gradientX, 0.5, gradientY, 0.5, 0)
    Images.updateGradientXY(gradient)
    Images.updateEdges(gradient)
    return Images.edges
