"""
Image Utils
"""

import cv2
from numpy import uint8, full as nfull

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


def colorMask(image, mask, color=(0, 0, 255)):
    imageWithoutError = cv2.cvtColor(
        runMask(image, cv2.bitwise_not(mask)), cv2.COLOR_GRAY2BGR)
    plainColor = nfull(imageWithoutError.shape, color, dtype=uint8)
    coloredMask = runMask(plainColor, mask)
    coloredError = coloredMask + imageWithoutError
    return [imageWithoutError, coloredMask, coloredError]
