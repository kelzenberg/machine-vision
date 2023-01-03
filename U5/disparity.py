"""
Disparity
"""

import cv2
from numpy import float32
from ImageStore import ImageStore


def findDisparities(left, right, disparity, blockSize, preFilterSize, preFilterCap, textureThreshold, minDisparity):
    leftName, leftImage = left
    rightName, rightImage = right
    print(
        f'(findDisparities) Find disparities between {leftName} and {rightName}')
    print(
        f'(findDisparities) With options:\n      disparity: {disparity}\n      blockSize: {blockSize}\n      preFilterSize: {preFilterSize}\n      preFilterCap: {preFilterCap}\n      textureThreshold: {textureThreshold}\n      minDisparity: {minDisparity}')

    stereoBM = cv2.StereoBM_create(disparity, blockSize=blockSize)
    stereoBM.setPreFilterSize(preFilterSize)
    stereoBM.setPreFilterCap(preFilterCap)
    stereoBM.setTextureThreshold(textureThreshold)
    stereoBM.setMinDisparity(minDisparity)

    computed = stereoBM.compute(leftImage, rightImage).astype(float32)
    computed = (computed/16.0 - minDisparity) / \
        disparity  # normalize to 255 gray values
    ImageStore.updateByName('disparity', computed)
