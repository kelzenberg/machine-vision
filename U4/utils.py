"""
Image Utils
"""

import cv2
from typing import Tuple

lineType = cv2.LINE_AA

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
yellow = (0, 255, 255)
purple = (255, 0, 255)


def findContours(image):
    return cv2.findContours(cv2.bitwise_not(image), mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)


def drawContours(image, contours, thickness=2):
    # convert to BGR if Gray, otherwise no contour color
    tempImage = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR) if len(
        image.shape) < 3 else image.copy()

    # correct non-array contours --> see https://stackoverflow.com/a/41880357
    tempContours = [contours] if not isinstance(contours, Tuple) else contours

    return cv2.drawContours(tempImage, tempContours, contourIdx=-1, color=red, thickness=thickness, lineType=lineType)


def approxCurves(contour, epsilon):
    return cv2.approxPolyDP(contour, epsilon, True)
