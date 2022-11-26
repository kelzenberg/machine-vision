"""
Image Utils
"""

import cv2

imageDepth = cv2.CV_16S
borderType = cv2.BORDER_REFLECT_101


def runThreshold(image, min):
    _, threshold = cv2.threshold(image, min, 256, cv2.THRESH_BINARY)
    return threshold


def runClosing(image, size=20):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))
    return cv2.erode(cv2.dilate(image, kernel), kernel)


def runErosion(image):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
    return cv2.erode(image, kernel)


def runFill(image):
    [_, image, _, _] = cv2.floodFill(image.copy(), None, (0, 0), 255)
    return cv2.bitwise_not(image)


def runMedian(image):
    return cv2.medianBlur(image, 51)


def runOffset(originalImage, substrate, offset=100):
    return (originalImage - substrate) + offset


def runMask(image, mask):
    return cv2.bitwise_and(image, image, mask=mask)
