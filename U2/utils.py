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
    gradientX = cv2.convertScaleAbs(cv2.Sobel(
        Images.filtered.copy(), cv2.CV_16S, 1, 0, borderType=cv2.BORDER_REFLECT_101))
    gradientY = cv2.convertScaleAbs(cv2.Sobel(
        Images.filtered.copy(), cv2.CV_16S, 0, 1, borderType=cv2.BORDER_REFLECT_101))
    gradient = cv2.addWeighted(gradientX, 0.5, gradientY, 0.5, 0)
    Images.updateEdges(gradient)
    return Images.edges
