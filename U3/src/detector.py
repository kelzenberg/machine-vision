"""
Image Detector
"""

import cv2
from numpy import uint8, zeros as nzeros, full as nfull
from typing import Dict, List
from Stores.ImageStore import ImageStore

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
    outputImage = nzeros(image.shape)
    return cv2.normalize(image, outputImage, alpha=0, beta=100, norm_type=cv2.NORM_MINMAX) + offset


imageStats: Dict[str, List[str]] = {}


def analyzeImage(name, image):
    print(f'(analyzeImage) Analyzing {name} {image.shape}')

    mask = ImageStore.add('mask threshold', runThreshold(image, 8))
    mask = ImageStore.add('mask erosion', runErosion(mask))
    # mask = ImageStore.add('mask closing', runClosing(mask)) # TODO: fill inside holes -> needed?

    maskArea = cv2.countNonZero(mask)
    imageStats[name] = [f'Mask area: {maskArea}px']

    grayImage = ImageStore.add('gray median', runMedian(image))
    grayImage = ImageStore.add('gray offset', runOffset(image, grayImage))
    grayImage = ImageStore.add('gray masked', runMask(grayImage, mask))

    mean = cv2.mean(grayImage, mask=mask)[0]
    threshold = 70
    thresholdPercentage = (threshold * mean) / 100.0
    imageStats[name].append(f'Mask gray mean: {round(mean, 3)}')
    imageStats[name].append(
        f'Error threshold: {round(thresholdPercentage, 3)} ({threshold}%)')

    grayMask = ImageStore.add(
        'gray threshold', runThreshold(grayImage, thresholdPercentage))
    grayMask = ImageStore.add('gray detect error', runFill(grayMask))
    grayMask = ImageStore.add('gray closing', runClosing(grayMask, 1))
    # TODO: fill inside 1px errors -> runClosing above correct?

    errorArea = cv2.countNonZero(grayMask)
    imageStats[name].append(f'Error area: {errorArea}px')
    errorPercentage = (errorArea / maskArea) * 100.0
    imageStats[name].append(
        f'Faulty area to mask: {round(errorPercentage,4)}%')

    imageWithoutError = cv2.cvtColor(cv2.bitwise_or(
        image, image, mask=cv2.bitwise_not(grayMask)), cv2.COLOR_GRAY2BGR)
    redImage = nfull(imageWithoutError.shape, (0, 0, 255), dtype=uint8)

    redMask = ImageStore.add('gray marked red', runMask(redImage, grayMask))
    imageWithoutError = ImageStore.add(
        'gray with error cut', imageWithoutError)

    grayImage = ImageStore.add('gray with error marked',
                               redMask + imageWithoutError)
