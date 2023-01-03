"""
Disparity
"""

import cv2
from numpy import float32
from ImageStore import ImageStore


def configureSBM(sbm):
    windowName = 'Disparity'

    preFilterSize = cv2.getTrackbarPos('preFilterSize', windowName) * 2 + 5
    print('foo', preFilterSize)
    preFilterCap = cv2.getTrackbarPos('preFilterCap', windowName)
    textureThreshold = cv2.getTrackbarPos('textureThreshold', windowName)
    minDisparity = cv2.getTrackbarPos('minDisparity', windowName)

    sbm.setPreFilterSize(preFilterSize)
    sbm.setPreFilterCap(preFilterCap)
    sbm.setTextureThreshold(textureThreshold)
    sbm.setMinDisparity(minDisparity)

    return sbm


def findDisparities(left, right, disparity, blockSize):
    leftName, leftImage = left
    rightName, rightImage = right
    print(
        f'(findDisparities) Find disparities between {leftName} and {rightName}')

    stereoBM = cv2.StereoBM_create(disparity, blockSize=blockSize)
    # stereoBM = configureSBM(stereoBM)

    minDisparity = cv2.getTrackbarPos('minDisparity', 'Optional Trackbars')
    computed = stereoBM.compute(leftImage, rightImage).astype(float32)
    computed = (computed/16.0 - minDisparity) / \
        disparity  # normalize to 255 gray values
    ImageStore.updateByName('disparity', computed)
