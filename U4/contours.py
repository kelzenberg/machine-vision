"""
Contour Finder
"""

import cv2
import utils
from typing import Dict, List
from ImageStore import ImageStore

imageStats: Dict[str, List[str]] = {}


def drawContour(name, image):
    print(f'(drawContours) Drawing Contours for {name} {image.shape}')

    contours, hierarchy = utils.findContours(image)

    ImageStore.updateByName(f'{name} shape contours',
                            utils.drawContours(image, contours))


def approxCurves(name, image, epsilon):
    print(f'(approxCurves) Approximate shape for {name} {image.shape}')

    contours, hierarchy = utils.findContours(image)
    contour = contours[0]
    curves = utils.polyCurves(contour, float(epsilon/100.0))

    ImageStore.updateByName(f'{name} shape curves',
                            utils.drawContours(image, curves))


def centerOfMass(contour):
    moment = cv2.moments(contour, binaryImage=True)
    centerOfMass = (int(moment['m10']/moment['m00']),
                    int(moment['m01']/moment['m00']))
    return centerOfMass
