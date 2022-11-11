import cv2
from TrackbarValues import TrackbarValues
from images import grayImage, filteredImage

"""
Utility functions
"""


def runGaussian():
    multiplier = 10
    global filteredImage
    filteredImage = cv2.GaussianBlur(grayImage.copy(), (TrackbarValues.kernel * multiplier + 1,
                                     TrackbarValues.kernel * multiplier + 1), TrackbarValues.sigma, borderType=cv2.BORDER_REFLECT_101)
    return filteredImage


def runMedian():
    multiplier = 6
    global filteredImage
    filteredImage = cv2.medianBlur(
        grayImage.copy(), TrackbarValues.kernel * multiplier + 1)
    return filteredImage
