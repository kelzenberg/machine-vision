"""
Disparity
"""

import cv2
from numpy import float32
from ImageStore import ImageStore


def findDisparities(left, right, matcher, numDisparities, blockSize, preFilterSize, preFilterCap, textureThreshold, minDisparity):
    leftName, leftImage = left
    rightName, rightImage = right

    print(
        f'(findDisparities) Find Disparities ({leftName} -> {rightName}):\n\
                  [Matcher: {"SGBM" if matcher == 1 else "BM"}] [Disparity: {numDisparities}] [BlockSize: {blockSize}]\n\
                  [PreFilterSize: {preFilterSize}] [PreFilterCap: {preFilterCap}]\n\
                  [TextureThreshold: {textureThreshold}] [MinDisparity: {minDisparity}]')

    blockMatcher = None

    if matcher == 1:  # use SGBM
        blockMatcher = cv2.StereoSGBM_create(
            minDisparity=minDisparity, numDisparities=numDisparities, blockSize=blockSize, preFilterCap=preFilterCap)
    else:  # use default BM
        blockMatcher = cv2.StereoBM_create(
            numDisparities=numDisparities, blockSize=blockSize)
        blockMatcher.setPreFilterSize(preFilterSize)
        blockMatcher.setPreFilterCap(preFilterCap)
        blockMatcher.setTextureThreshold(textureThreshold)
        blockMatcher.setMinDisparity(minDisparity)

    computed = blockMatcher.compute(leftImage, rightImage)

    # normalize to 255 gray values
    computed = (computed.astype(float32)/16.0 - minDisparity) / numDisparities

    ImageStore.updateByName('disparity', computed)
