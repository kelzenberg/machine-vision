import cv2
from TrackbarValues import TrackbarValues
from Images import Images

"""
Utility functions
"""


def runGaussian():
    multiplier = 10
    Images.updateFiltered(cv2.GaussianBlur(Images.gray.copy(), (TrackbarValues.kernel * multiplier + 1,
                                                                TrackbarValues.kernel * multiplier + 1), TrackbarValues.sigma, borderType=cv2.BORDER_REFLECT_101))
    return Images.filtered


def runMedian():
    multiplier = 6
    Images.updateFiltered(cv2.medianBlur(
        Images.gray.copy(), TrackbarValues.kernel * multiplier + 1))
    return Images.filtered
