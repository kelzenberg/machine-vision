"""
Disparity
"""

import cv2
from ImageStore import ImageStore


def findDisparities(left, right, disparity, blockSize):
    leftName, leftImage = left
    rightName, rightImage = right
    print(
        f'(findDisparities) Find disparities between {leftName} and {rightName}')

    stereoBM = cv2.StereoBM_create(disparity, blockSize=blockSize)
    disparity = stereoBM.compute(leftImage, rightImage)
    ImageStore.updateByName('disparity', disparity)
