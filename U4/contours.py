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

    contours, _ = utils.findContours(image)

    ImageStore.updateByName('shape contours', utils.drawContours(
        image.copy(), contours, thickness=5))


def approxCurves(name, image, epsilon):
    print(f'(approxCurves) Approximate shape for {name} {image.shape}')

    contours, _ = utils.findContours(image)

    tempImage = image.copy()
    for contour in contours:
        curves = utils.approxCurves(contour, float(epsilon))
        tempImage = utils.drawContours(tempImage, curves, thickness=5)

    ImageStore.updateByName('approx curves', tempImage)


def convexHull(name, image):
    print(f'(convexHull) Find convex hull for {name} {image.shape}')
    contours, _ = utils.findContours(image)

    tempImage = image.copy()
    for contour in contours:
        hull = cv2.convexHull(contour)
        tempImage = utils.drawContours(tempImage, hull, thickness=5)

    ImageStore.updateByName('convex hull', tempImage)


def centerOfMass(contour):
    moment = cv2.moments(contour, binaryImage=True)
    centerOfMass = (int(moment['m10']/moment['m00']),
                    int(moment['m01']/moment['m00']))
    return centerOfMass
