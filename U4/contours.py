"""
Contour Finder
"""

import cv2
import utils
from typing import Dict, List
from ImageStore import ImageStore

imageStats: Dict[str, List[str]] = {}


def drawContours(name, originalImage):
    print(f'(drawContours) Drawing Contours for {name} {originalImage.shape}')

    contours, hierarchy = utils.findContours(originalImage)
    ImageStore.add(f'{name} shape contours',
                   utils.drawContours(originalImage, contours))
