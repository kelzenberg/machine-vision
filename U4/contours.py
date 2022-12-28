"""
Contour Finder
"""

import cv2
import utils
from typing import Dict, List
from ImageStore import ImageStore

imageStats: Dict[str, List[str]] = {}


def drawFeatures(name, image, contour):
    tempImage = drawCenterOfMass(name, image, contour)
    tempImage = drawMinCircle(name, tempImage, contour)
    tempImage = utils.drawContours(
        tempImage, contour, thickness=utils.lineThickness)
    return tempImage


def drawCenterOfMass(name, image, contour):
    print(
        f'(drawCenterOfMass) Drawing Center of Mass for {name} {image.shape}')
    return cv2.circle(image, utils.centerOfMass(contour), radius=utils.lineThickness, color=utils.blue, thickness=-1)


def drawMinCircle(name, image, contour):
    print(f'(drawMinCircle) Drawing minimal circle for {name} {image.shape}')
    center, radius = cv2.minEnclosingCircle(contour)
    centerPoint = tuple(int(point) for point in center)
    circleRadius = int(radius)

    return cv2.circle(image, centerPoint, circleRadius, color=utils.yellow, thickness=utils.lineThickness, lineType=utils.lineType)


def drawContour(name, image):
    print(f'(drawContours) Drawing Contours for {name} {image.shape}')
    contours, _ = utils.findContours(image)

    tempImage = utils.convertToColor(image)
    for contour in contours:
        tempImage = drawFeatures(name, tempImage, contour)

    ImageStore.updateByName('shape contours', tempImage)


def approxCurves(name, image, epsilon):
    print(f'(approxCurves) Approximate shape for {name} {image.shape}')
    contours, _ = utils.findContours(image)

    tempImage = utils.convertToColor(image)
    for contour in contours:
        curves = utils.approxCurves(contour, float(epsilon))
        tempImage = drawFeatures(name, tempImage, curves)

    ImageStore.updateByName('approx curves', tempImage)


def convexHull(name, image):
    print(f'(convexHull) Find convex hull for {name} {image.shape}')
    contours, _ = utils.findContours(image)

    tempImage = utils.convertToColor(image)
    for contour in contours:
        hull = cv2.convexHull(contour)
        tempImage = drawFeatures(name, tempImage, hull)

    ImageStore.updateByName('convex hull', tempImage)
