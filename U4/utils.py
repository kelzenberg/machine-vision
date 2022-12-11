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
    _, treshold = cv2.threshold(image, 250, 255, cv2.THRESH_BINARY)
    return cv2.findContours(cv2.bitwise_not(treshold), mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)


def drawContours(image, contours):
    tempImage = image
    if (len(image.shape) < 3):
        tempImage = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    return cv2.drawContours(tempImage, contours, contourIdx=-1, color=red, thickness=2, lineType=lineType)


def approxCurves(contour, epsilon):
    return cv2.approxPolyDP(contour, epsilon, True)
