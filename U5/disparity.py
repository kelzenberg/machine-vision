"""
Disparity
"""

import cv2
from numpy import float32
from ImageStore import ImageStore


def findDisparities(left, right, numDisparities, blockSize, preFilterSize, preFilterCap, textureThreshold, minDisparity):
    leftName, leftImage = left
    rightName, rightImage = right

    print(
        f'(findDisparities) Find disparities between {leftName} and {rightName}')
    print(
        f'(findDisparities) With options:\n      disparity: {numDisparities}\n      blockSize: {blockSize}\n      preFilterSize: {preFilterSize}\n      preFilterCap: {preFilterCap}\n      textureThreshold: {textureThreshold}\n      minDisparity: {minDisparity}')

    stereoBM = cv2.StereoBM_create(
        numDisparities=numDisparities, blockSize=blockSize)
    stereoBM.setPreFilterSize(preFilterSize)
    stereoBM.setPreFilterCap(preFilterCap)
    stereoBM.setTextureThreshold(textureThreshold)
    stereoBM.setMinDisparity(minDisparity)

    computed = stereoBM.compute(leftImage, rightImage)
    # normalize to 255 gray values
    computed = (computed.astype(float32)/16.0 - minDisparity) / numDisparities

    ImageStore.updateByName('disparity', computed)
