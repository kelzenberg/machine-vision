import cv2
from TrackbarValues import TrackbarValues
from images import grayImage, filteredImage

"""
Utility functions
"""


def runGaussian():
    global filteredImage
    filteredImage = cv2.GaussianBlur(grayImage.copy(), (TrackbarValues.kernel*20+1,
                                     TrackbarValues.kernel*20+1), TrackbarValues.sigma, borderType=cv2.BORDER_REFLECT_101)
    return filteredImage
