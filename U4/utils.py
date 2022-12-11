"""
Image Utils
"""

import cv2

lineType = cv2.LINE_AA

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
yellow = (0, 255, 255)
purple = (255, 0, 255)


def findContours(image):
    return cv2.findContours(cv2.bitwise_not(image), mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)


def drawContours(image, contours):
    return cv2.drawContours(cv2.cvtColor(image.copy(), cv2.COLOR_GRAY2BGR), contours, contourIdx=-1, color=red, thickness=2, lineType=lineType)


def polyCurves(curve, epsilon):
    return cv2.approxPolyDP(curve, epsilon, True)
