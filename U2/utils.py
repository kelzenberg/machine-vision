"""
Utility functions
"""
import cv2


def showImage(windowName, image):
    print('[DEBUG](showImage) Show image in window:', windowName)
    cv2.imshow(windowName, image)

def convertToGrayBGR(image):
    return cv2.cvtColor(cv2.cvtColor(
    image, cv2.COLOR_RGB2GRAY), cv2.COLOR_GRAY2BGR)