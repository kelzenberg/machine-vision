"""
Image Utils
"""

import cv2

imageDepth = cv2.CV_16S
borderType = cv2.BORDER_REFLECT_101


def runThreshold(image, min=0):
    _, threshold = cv2.threshold(image, min, 256, cv2.THRESH_BINARY)
    return threshold


def runFillInv(image, grayValue=0):
    [_, image, _, _] = cv2.floodFill(
        image.copy(), None, (grayValue, grayValue), 255)
    return cv2.bitwise_not(image)


def runOr(threshold, filled):
    return threshold | filled


def runErosion(image, size=3):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))
    return cv2.erode(image, kernel)


def runMedian(image, size=3):
    return cv2.medianBlur(image, size)


def runOffset(originalImage, substrate, offset=100):
    return (originalImage - substrate) + offset


def runMask(image, mask):
    return cv2.bitwise_and(image, image, mask=mask)


def runClosing(image, size=3):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))
    return cv2.erode(cv2.dilate(image, kernel), kernel)
