"""
Disparity
"""

import cv2
from numpy import float32
from ImageStore import ImageStore


def findDisparities(left, right, disparity, blockSize):
    leftName, leftImage = left
    rightName, rightImage = right
    print(
        f'(findDisparities) Find disparities between {leftName} and {rightName}')

    stereoBM = cv2.StereoBM_create(disparity, blockSize=blockSize)
    # stereoBM.setPreFilterSize(5)
    # stereoBM.setTextureThreshold(100)

    minDisparity = 0
    computed = stereoBM.compute(leftImage, rightImage).astype(float32)
    computed = (computed/16.0 - minDisparity)/disparity # normalize to 255 gray values
    ImageStore.updateByName('disparity', computed)
