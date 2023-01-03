"""
Disparity
"""

import cv2
from ImageStore import ImageStore


def findDisparities(base, displaced, disparity, blockSize):
    baseName, baseImage = base
    dispName, dispImage = displaced
    print(
        f'(findDisparities) Find disparities between {baseName} and {dispName}')

    stereoBM = cv2.StereoBM_create(64, blockSize=blockSize)
    disparity = stereoBM.compute(baseImage, dispImage)
    ImageStore.updateByName('disparity', disparity)
