"""
Contour Finder
"""

import cv2
import utils
from typing import Dict, List
from ImageStore import ImageStore

imageStats: Dict[str, List[str]] = {}
lineThickness = 3


def drawCenterOfMass(name, image, contour):
    print(
        f'(drawCenterOfMass) Drawing Center of Mass for {name} {image.shape}')

    return cv2.circle(image, utils.centerOfMass(contour), radius=lineThickness, color=utils.blue, thickness=-1)


def drawMinCircle(name, image, contour):
    print(f'(drawMinCircle) Drawing minimal circle for {name} {image.shape}')

    center, radius = cv2.minEnclosingCircle(contour)

    return cv2.circle(image, tuple(int(point) for point in center), int(radius), color=utils.yellow, thickness=lineThickness, lineType=utils.lineType)


def drawContour(name, image):
    print(f'(drawContours) Drawing Contours for {name} {image.shape}')

    contours, _ = utils.findContours(image)

    tempImage = cv2.cvtColor(image.copy(), cv2.COLOR_GRAY2BGR)
    for contour in contours:
        tempImage = drawCenterOfMass(name, tempImage, contour)
        tempImage = drawMinCircle(name, tempImage, contour)
        tempImage = utils.drawContours(
            tempImage, contour, thickness=lineThickness)

    ImageStore.updateByName('shape contours', tempImage)


def approxCurves(name, image, epsilon):
    print(f'(approxCurves) Approximate shape for {name} {image.shape}')

    contours, _ = utils.findContours(image)

    tempImage = cv2.cvtColor(image.copy(), cv2.COLOR_GRAY2BGR)
    for contour in contours:
        curves = utils.approxCurves(contour, float(epsilon))
        tempImage = drawCenterOfMass(name, tempImage, curves)
        tempImage = drawMinCircle(name, tempImage, curves)
        tempImage = utils.drawContours(
            tempImage, curves, thickness=lineThickness)

    ImageStore.updateByName('approx curves', tempImage)


def convexHull(name, image):
    print(f'(convexHull) Find convex hull for {name} {image.shape}')
    contours, _ = utils.findContours(image)

    tempImage = cv2.cvtColor(image.copy(), cv2.COLOR_GRAY2BGR)
    for contour in contours:
        hull = cv2.convexHull(contour)
        tempImage = drawCenterOfMass(name, tempImage, hull)
        tempImage = drawMinCircle(name, tempImage, hull)
        tempImage = utils.drawContours(
            tempImage, hull, thickness=lineThickness)

    ImageStore.updateByName('convex hull', tempImage)
