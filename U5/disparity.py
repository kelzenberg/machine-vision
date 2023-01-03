"""
Disparity
"""

import cv2
from numpy import float32
from ImageStore import ImageStore


def configureSBM(sbm):
    preFilterType = cv2.getTrackbarPos('preFilterType', 'Optional Trackbars')
    preFilterSize = cv2.getTrackbarPos(
        'preFilterSize', 'Optional Trackbars') * 2 + 5
    preFilterCap = cv2.getTrackbarPos('preFilterCap', 'Optional Trackbars')
    textureThreshold = cv2.getTrackbarPos(
        'textureThreshold', 'Optional Trackbars')
    uniquenessRatio = cv2.getTrackbarPos(
        'uniquenessRatio', 'Optional Trackbars')
    speckleRange = cv2.getTrackbarPos('speckleRange', 'Optional Trackbars')
    speckleWindowSize = cv2.getTrackbarPos(
        'speckleWindowSize', 'Optional Trackbars') * 2
    disp12MaxDiff = cv2.getTrackbarPos('disp12MaxDiff', 'Optional Trackbars')
    minDisparity = cv2.getTrackbarPos('minDisparity', 'Optional Trackbars')

    sbm.setPreFilterType(preFilterType)
    sbm.setPreFilterSize(preFilterSize)
    sbm.setPreFilterCap(preFilterCap)
    sbm.setTextureThreshold(textureThreshold)
    sbm.setUniquenessRatio(uniquenessRatio)
    sbm.setSpeckleRange(speckleRange)
    sbm.setSpeckleWindowSize(speckleWindowSize)
    sbm.setDisp12MaxDiff(disp12MaxDiff)
    sbm.setMinDisparity(minDisparity)

    return sbm


def findDisparities(left, right, disparity, blockSize):
    leftName, leftImage = left
    rightName, rightImage = right
    print(
        f'(findDisparities) Find disparities between {leftName} and {rightName}')

    stereoBM = cv2.StereoBM_create(disparity, blockSize=blockSize)
    stereoBM = configureSBM(stereoBM)

    minDisparity = cv2.getTrackbarPos('minDisparity', 'Optional Trackbars')
    computed = stereoBM.compute(leftImage, rightImage).astype(float32)
    computed = (computed/16.0 - minDisparity) / \
        disparity  # normalize to 255 gray values
    ImageStore.updateByName('disparity', computed)
