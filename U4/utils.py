"""
Image Utils
"""

import cv2
from typing import Tuple
from numpy import intp

lineType = cv2.LINE_AA
lineThickness = 3

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
yellow = (0, 255, 255)
purple = (255, 0, 255)


def convertToColor(image):
    return cv2.cvtColor(image.copy(), cv2.COLOR_GRAY2BGR)


def findContours(image):
    return cv2.findContours(cv2.bitwise_not(image), mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)


def approxCurves(contour, epsilon):
    return cv2.approxPolyDP(contour, epsilon, True)


def centerOfMass(contour):
    moment = cv2.moments(contour, binaryImage=True)
    centerOfMass = (int(moment['m10']/moment['m00']),
                    int(moment['m01']/moment['m00']))
    return centerOfMass


def minCircle(contour):
    center, radius = cv2.minEnclosingCircle(contour)
    return (tuple(int(point) for point in center), int(radius))


def minAreaRect(contour):
    box = cv2.minAreaRect(contour)
    return intp(cv2.boxPoints(box))


def boundingBox(contour):
    box = cv2.boundingRect(contour)  # returns [x, y, width, height]
    start = box[:2]
    end = [xy+wh for xy, wh in zip(start, box[-2:])]
    return (start, end)


def drawContours(image, contours, color=red, thickness=2):
    # correct non-array contours --> see https://stackoverflow.com/a/41880357
    tempContours = [contours] if not isinstance(contours, Tuple) else contours

    return cv2.drawContours(image, tempContours, contourIdx=-1, color=color, thickness=thickness, lineType=lineType)
