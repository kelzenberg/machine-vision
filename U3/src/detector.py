"""
Image Detector
"""

import cv2
import utils
from numpy import uint8, zeros as nzeros, full as nfull
from typing import Dict, List
from ImageStore import ImageStore

imageStats: Dict[str, List[str]] = {}


def analyzeImage(name, image):
    print(f'(analyzeImage) Analyzing {name} {image.shape}')

    mask = ImageStore.add('mask threshold', utils.runThreshold(image, 8))
    mask = ImageStore.add('mask erosion', utils.runErosion(mask))
    # mask = ImageStore.add('mask closing', utils.runClosing(mask)) # TODO: fill inside holes -> needed?

    maskArea = cv2.countNonZero(mask)
    imageStats[name] = [f'Mask area: {maskArea}px']

    grayImage = ImageStore.add('gray median', utils.runMedian(image))
    grayImage = ImageStore.add(
        'gray offset', utils.runOffset(image, grayImage))
    grayImage = ImageStore.add('gray masked', utils.runMask(grayImage, mask))

    mean = cv2.mean(grayImage, mask=mask)[0]
    threshold = 70
    thresholdPercentage = (threshold * mean) / 100.0
    imageStats[name].append(f'Mask gray mean: {round(mean, 3)}')
    imageStats[name].append(
        f'Error threshold: {round(thresholdPercentage, 3)} ({threshold}%)')

    grayMask = ImageStore.add(
        'gray threshold', utils.runThreshold(grayImage, thresholdPercentage))
    grayMask = ImageStore.add('gray detect error', utils.runFill(grayMask))
    grayMask = ImageStore.add('gray closing', utils.runClosing(grayMask, 1))
    # TODO: fill inside 1px errors -> utils.runClosing above correct?

    errorArea = cv2.countNonZero(grayMask)
    imageStats[name].append(f'Error area: {errorArea}px')
    errorPercentage = (errorArea / maskArea) * 100.0
    imageStats[name].append(
        f'Faulty area to mask: {round(errorPercentage,4)}%')

    imageWithoutError = cv2.cvtColor(cv2.bitwise_or(
        image, image, mask=cv2.bitwise_not(grayMask)), cv2.COLOR_GRAY2BGR)
    redImage = nfull(imageWithoutError.shape, (0, 0, 255), dtype=uint8)

    redMask = ImageStore.add(
        'gray marked red', utils.runMask(redImage, grayMask))
    imageWithoutError = ImageStore.add(
        'gray with error cut', imageWithoutError)

    grayImage = ImageStore.add('gray with error marked',
                               redMask + imageWithoutError)
