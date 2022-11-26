"""
Image Detector
"""

import cv2
import numpy
from Stores.ImageStore import ImageStore

imageDepth = cv2.CV_16S
borderType = cv2.BORDER_REFLECT_101


def runThreshold(image):
    _, threshold = cv2.threshold(image, 8, 256, cv2.THRESH_BINARY)
    return threshold


def runClosing(image):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20))
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


def runSobel(image):
    gradientX = cv2.convertScaleAbs(
        cv2.Sobel(image, imageDepth, 1, 0, borderType))
    gradientY = cv2.convertScaleAbs(
        cv2.Sobel(image, imageDepth, 0, 1, borderType))
    return cv2.addWeighted(gradientX, 0.5, gradientY, 0.5, 0)


def runOpening(image):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
    return cv2.dilate(cv2.erode(image, kernel), kernel)


def runNormal(image):
    offset = 100
    outputImage = numpy.zeros(image.shape)
    return cv2.normalize(image, outputImage, alpha=0, beta=100, norm_type=cv2.NORM_MINMAX) + offset


def analyzeImage(name, image):
    print(f'(analyzeImage) Analyzing {name} {image.shape}')

    mask = ImageStore.add('mask threshold', runThreshold(image))
    mask = ImageStore.add('mask erosion', runErosion(mask))
    # mask = ImageStore.add('mask closing', runClosing(mask)) # TODO: to clean inside -> needed?

    grayImage = ImageStore.add('gray median', runMedian(image))
    grayImage = ImageStore.add('gray offset', runOffset(image, grayImage))
    grayImage = ImageStore.add('gray masked', runMask(grayImage, mask))
    print(f'(analyzeImage) {name} gray mean: {cv2.mean(grayImage, mask=mask)[0]}')

    mask = ImageStore.add('mask fill outside', runFill(mask))

    # grayImage = ImageStore.add('opening', runOpening(grayImage))
    # grayImage = ImageStore.add('normal', runNormal(grayImage))
