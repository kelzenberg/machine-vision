"""
Contour Finder
"""

import cv2
import utils
from typing import Dict, List
from ImageStore import ImageStore

imageStats: Dict[str, List[str]] = {}


def drawCenterOfMass(name, image, contour):
    print(
        f'(drawCenterOfMass) Drawing Center of Mass for {name} {image.shape}')

    return cv2.circle(image, utils.centerOfMass(
        contour), radius=5, color=utils.blue, thickness=-1)


def drawContour(name, image):
    print(f'(drawContours) Drawing Contours for {name} {image.shape}')

    contours, _ = utils.findContours(image)

    tempImage = cv2.cvtColor(image.copy(), cv2.COLOR_GRAY2BGR)
    for contour in contours:
        imageCOM = drawCenterOfMass(name, tempImage, contour)
        tempImage = utils.drawContours(imageCOM, contour, thickness=5)

    ImageStore.updateByName('shape contours', tempImage)


def approxCurves(name, image, epsilon):
    print(f'(approxCurves) Approximate shape for {name} {image.shape}')

    contours, _ = utils.findContours(image)

    tempImage = cv2.cvtColor(image.copy(), cv2.COLOR_GRAY2BGR)
    for contour in contours:
        curves = utils.approxCurves(contour, float(epsilon))
        imageCOM = drawCenterOfMass(name, tempImage, curves)
        tempImage = utils.drawContours(imageCOM, curves, thickness=5)

    ImageStore.updateByName('approx curves', tempImage)


def convexHull(name, image):
    print(f'(convexHull) Find convex hull for {name} {image.shape}')
    contours, _ = utils.findContours(image)

    tempImage = cv2.cvtColor(image.copy(), cv2.COLOR_GRAY2BGR)
    for contour in contours:
        hull = cv2.convexHull(contour)
        imageCOM = drawCenterOfMass(name, tempImage, hull)
        tempImage = utils.drawContours(imageCOM, hull, thickness=5)

    ImageStore.updateByName('convex hull', tempImage)
