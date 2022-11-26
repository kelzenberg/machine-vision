"""
Image Detector
"""

import cv2
import numpy
from Stores.ImageStore import ImageStore

imageDepth = cv2.CV_16S
borderType = cv2.BORDER_REFLECT_101


def runMedian(image):
    return cv2.medianBlur(image.copy(), 51)


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


def runEqualize(image):
    # TODO: unused
    return cv2.equalizeHist(image)


def runBinary(image):
    _, binary = cv2.threshold(image, 10, 512, cv2.THRESH_BINARY)
    return binary


def runErosion(image):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
    return cv2.erode(image, kernel)


def analyzeImage(name, image):
    print(f'(analyzeImage) Analyzing {name} {image.shape}')

    analyzedImage = ImageStore.add('median', runMedian(image))
    analyzedImage = ImageStore.add('sobel', runSobel(analyzedImage))
    analyzedImage = ImageStore.add('opening', runOpening(analyzedImage))
    analyzedImage = ImageStore.add('normal', runNormal(analyzedImage))
    analyzedImage = ImageStore.add('binary', runBinary(analyzedImage))

    return analyzedImage
