"""
Image Detector
"""

import utils
from cv2 import countNonZero, mean as cvmean
from typing import Dict, List
from ImageStore import ImageStore

imageStats: Dict[str, List[str]] = {}


def analyzeImage(name, originalImage):
    print(f'(analyzeImage) Analyzing {name} {originalImage.shape}')

    mask = ImageStore.add(
        'mask threshold', utils.runThreshold(originalImage, 20))
    filledInv = ImageStore.add(
        'mask filled inverted', utils.runFillInv(mask, 0))
    mask = ImageStore.add('mask threshold w/o filled',
                          utils.runOr(mask, filledInv))
    mask = ImageStore.add('mask erosion', utils.runErosion(mask, 15))

    maskArea = countNonZero(mask)
    imageStats[name] = [f'Mask area: {maskArea}px']

    grayImage = ImageStore.add(
        'gray median', utils.runMedian(originalImage, 51))
    grayImage = ImageStore.add(
        'gray minus median w/ offset', utils.runOffset(originalImage, grayImage, 100))
    grayImage = ImageStore.add('gray masked', utils.runMask(grayImage, mask))

    mean = cvmean(grayImage, mask=mask)[0]
    threshold = 70
    thresholdPercentage = (threshold * mean) / 100.0
    imageStats[name].append(f'Mask gray mean: {round(mean, 3)}')
    imageStats[name].append(
        f'Error threshold: {round(thresholdPercentage, 3)} ({threshold}%)')

    grayMask = ImageStore.add(
        'gray threshold', utils.runThreshold(grayImage, thresholdPercentage))
    grayMask = ImageStore.add(
        'gray error filled inverted', utils.runFillInv(grayMask))
    grayMask = ImageStore.add('gray closing', utils.runClosing(grayMask, 3))

    errorArea = countNonZero(grayMask)
    imageStats[name].append(f'Error area: {errorArea}px')
    errorPercentage = (errorArea / maskArea) * 100.0
    imageStats[name].append(
        f'Faulty area to mask: {round(errorPercentage,4)}%')

    [imageWithoutError, coloredMask, coloredError] = utils.colorMask(
        originalImage, grayMask)
    ImageStore.add('gray w/o error', imageWithoutError)
    ImageStore.add('gray error marked', coloredMask)
    ImageStore.add('gray with error marked', coloredError)
