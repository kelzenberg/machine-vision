"""
U4 app
"""

from typing import Dict, List
import cv2
from glob import glob
from os import path as ospath
from Window import Window
from ImageStore import ImageStore
from contours import drawContour, approxCurves,convexHull, imageStats

"""
Load Images
"""
imageCounter = 0
globPath = ospath.join(ospath.abspath('./images'), '*.png')

for file in sorted(glob(globPath)):
    image = cv2.imread(file)
    imageName = file.split('/')[-1].split('.')[0]
    ImageStore.updateByName(imageName, cv2.cvtColor(image, cv2.COLOR_RGB2GRAY))
    imageCounter += 1
    print(f'(main) Image loaded: {imageName}')

"""
Trackbar functions
"""

TRACKBAR = {'IMAGE': -1, 'STEP': 0, 'EPSILON': 0}


def imageOnChange(value):
    prev = TRACKBAR['IMAGE']
    if prev == value:
        return

    print(f'(imageOnChange) {prev} to {value}')
    TRACKBAR['IMAGE'] = value

    [imageName, image] = ImageStore.getByPosition(value)

    drawContour(imageName, image)
    approxCurves(imageName, image, TRACKBAR['EPSILON'])
    convexHull(imageName, image)

    stepOnChange(TRACKBAR['STEP'])
    epsilonOnChange(TRACKBAR['EPSILON'])


def stepOnChange(value):
    prev = TRACKBAR['STEP']
    if prev != value:
        print(f'(stepOnChange) {prev} to {value}')

    TRACKBAR['STEP'] = value

    [imageName, image] = ImageStore.getByPosition(
        TRACKBAR['IMAGE'] if value == 0 else value + imageCounter - 1)

    window.show(imageName, image)


def epsilonOnChange(value):
    if TRACKBAR['STEP'] != 2:  # skip if approxCurves (step 2) is not shown
        return

    prev = TRACKBAR['EPSILON']
    if prev != value:
        print(f'(epsilonOnChange) {prev} to {value}')

    TRACKBAR['EPSILON'] = value

    # get original image for approx curves
    [imageName, image] = ImageStore.getByPosition(TRACKBAR['IMAGE'])
    approxCurves(imageName, image, value)

    stepOnChange(TRACKBAR['STEP'])


"""
Main function
"""

window = Window('Main')
window.addTrackbar('Image Select ', (0, imageCounter - 1), imageOnChange)
window.addTrackbar('Step ', (0, 10), stepOnChange)
window.addTrackbar('Epsilon ', (0, 180), epsilonOnChange)

imageOnChange(0)  # to trigger first image generation

print('(main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

[print('(main) Image Stats ({0}):\n       {1}'.format(name, "\n       ".join(prints)))
 for [name, prints] in sorted(imageStats.items())]

print('(main) Closing all windows.')
cv2.destroyAllWindows()
