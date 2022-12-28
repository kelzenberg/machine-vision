"""
Contour Finder
"""

import cv2
import utils
from typing import Dict, List
from ImageStore import ImageStore

imageStats: Dict[str, List[str]] = {}


"""
Draw Features of Contours
"""


def drawCenterOfMass(name, image, contour):
    print(
        f'(drawCenterOfMass) Drawing Center of Mass for {name} {image.shape}')
    return cv2.circle(image, utils.centerOfMass(contour), radius=utils.lineThickness, color=utils.blue, thickness=-1, lineType=utils.lineType)


def drawMinCircle(name, image, contour):
    print(f'(drawMinCircle) Drawing minimal circle for {name} {image.shape}')
    center, radius = utils.minCircle(contour)
    return cv2.circle(image, center, radius, color=utils.yellow, thickness=utils.lineThickness, lineType=utils.lineType)


def drawFeatures(name, image, contour):
    tempImage = drawCenterOfMass(name, image, contour)
    tempImage = drawMinCircle(name, tempImage, contour)
    tempImage = utils.drawContours(
        tempImage, contour, thickness=utils.lineThickness)
    return tempImage


"""
Find & draw Contours
"""


def drawContour(name, image):
    print(f'(drawContour) Drawing Contours for {name} {image.shape}')
    contours, _ = utils.findContours(image)

    tempImage = utils.convertToColor(image)
    for contour in contours:
        tempImage = drawFeatures(name, tempImage, contour)

    ImageStore.updateByName('shape contours', tempImage)


def drawApproxCurves(name, image, epsilon):
    print(f'(drawApproxCurves) Approximate shape for {name} {image.shape}')
    contours, _ = utils.findContours(image)

    tempImage = utils.convertToColor(image)
    for contour in contours:
        curves = utils.approxCurves(contour, float(epsilon))
        tempImage = drawFeatures(name, tempImage, curves)

    ImageStore.updateByName('approx curves', tempImage)


def drawConvexHull(name, image):
    print(f'(drawConvexHull) Find convex hull for {name} {image.shape}')
    contours, _ = utils.findContours(image)

    tempImage = utils.convertToColor(image)
    for contour in contours:
        hull = cv2.convexHull(contour)
        tempImage = drawFeatures(name, tempImage, hull)

    ImageStore.updateByName('convex hull', tempImage)
