"""
Utility functions
"""
import cv2


def showImage(windowName, image):
    print('[DEBUG](showImage) Show image in window:', windowName)
    cv2.imshow(windowName, image)
