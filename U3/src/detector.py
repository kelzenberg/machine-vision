"""
Image Detector
"""

import cv2
from Stores.ImageStore import ImageStore


def runMedian(image):
    return cv2.medianBlur(image.copy(), 5)


def runOpening(image):
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, (5, 5))


def analyzeImage(name):
    global STEPS
    image = ImageStore.get(name)
    print(f'(analyzeImage) Analyzing {name} {image.shape}')

    analyzedImage = ImageStore.add('median', runMedian(image))
    analyzedImage = ImageStore.add('opening', runOpening(analyzedImage))

    return analyzedImage
