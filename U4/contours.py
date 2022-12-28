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


def drawMinArea(name, image, contour):
    print(f'(drawMinArea) Drawing minimal area for {name} {image.shape}')
    box = utils.minAreaRect(contour)
    return utils.drawContours(image, box, color=utils.purple, thickness=utils.lineThickness)


def drawBoundingBox(name, image, contour):
    print(f'(drawBoundingBox) Drawing bounding box for {name} {image.shape}')
    start, end = utils.boundingBox(contour)
    return cv2.rectangle(image, start, end, color=utils.green, thickness=utils.lineThickness, lineType=utils.lineType)


def drawFeatures(name, image, contour):
    tempImage = drawCenterOfMass(name, image, contour)
    tempImage = drawMinCircle(name, tempImage, contour)
    tempImage = drawMinArea(name, image, contour)
    tempImage = drawBoundingBox(name, image, contour)
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
    contourAreas = []
    for contour in contours:
        contourAreas.append(f'{cv2.contourArea(contour)}')
        tempImage = drawFeatures(name, tempImage, contour)

    areaStrings = "px, ".join(contourAreas) if len(
        contourAreas) > 1 else f'{contourAreas[0]}px'
    imageStats[name] = [f'Contour area(s): {areaStrings}']

    ImageStore.updateByName('shape contours', tempImage)


def drawConvexHull(name, image):
    print(f'(drawConvexHull) Find convex hull for {name} {image.shape}')
    contours, _ = utils.findContours(image)

    tempImage = utils.convertToColor(image)
    hullAreas = []
    for contour in contours:
        hull = cv2.convexHull(contour)
        hullAreas.append(f'{cv2.contourArea(hull)}')
        tempImage = drawFeatures(name, tempImage, hull)

    areaStrings = "px, ".join(hullAreas) if len(
        hullAreas) > 1 else f'{hullAreas[0]}px'
    imageStats[name].append(f'Convex hull area(s): {areaStrings}')

    ImageStore.updateByName('convex hull', tempImage)


def drawApproxCurves(name, image, epsilon):
    print(f'(drawApproxCurves) Approximate shape for {name} {image.shape}')
    contours, _ = utils.findContours(image)

    tempImage = utils.convertToColor(image)
    curvesAreas = []
    for contour in contours:
        curves = utils.approxCurves(contour, float(epsilon))
        curvesAreas.append(f'{cv2.contourArea(curves)}')
        tempImage = drawFeatures(name, tempImage, curves)

    areaStrings = "px, ".join(curvesAreas) if len(
        curvesAreas) > 1 else f'{curvesAreas[0]}px'
    imageStats[name].append(
        f'Approx Curves area(s)\n          for Epsilon {epsilon}: {areaStrings}')

    ImageStore.updateByName('approx curves', tempImage)
