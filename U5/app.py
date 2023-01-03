"""
U5 app
"""

import cv2
from typing import Dict, List
from glob import glob
from os import path as ospath

from Window import Window
from ImageStore import ImageStore
from disparity import findDisparities

imageStats: Dict[str, List[str]] = {}

"""
Load Images
"""
imageCounter = 0
globPath = ospath.join(ospath.abspath('./images'), '*.png')

for file in sorted(glob(globPath)):
    baseImage = cv2.imread(file)
    baseImageName = file.split('/')[-1].split('.')[0]
    ImageStore.updateByName(baseImageName, cv2.cvtColor(
        baseImage, cv2.COLOR_RGB2GRAY))
    imageCounter += 1
    print(f'(main) Image loaded: {baseImageName}')


"""
Utils functions
"""


def showDisparities():
    right = ImageStore.getByPosition(0)
    left = ImageStore.getByPosition(TRACKBAR['IMAGE'] + 1)

    findDisparities(
        left,
        right,
        disparity=TRACKBAR['DISPARITY'],
        blockSize=TRACKBAR['BLOCKSIZE'],
        preFilterSize=TRACKBAR['PREFILTERSIZE'],
        preFilterCap=TRACKBAR['PREFILTERCAP'],
        textureThreshold=TRACKBAR['TEXTURETHRESHOLD'],
        minDisparity=TRACKBAR['MINDISPARITY']
    )

    disparityImage = ImageStore.getByName('disparity')
    disparityWindow.show('disparity', disparityImage, withText=False)


"""
Trackbar functions
"""

TRACKBAR = {'IMAGE': -1, 'DISPARITY': 16, 'BLOCKSIZE': 5, 'PREFILTERSIZE': 5,
            'PREFILTERCAP': 5, 'TEXTURETHRESHOLD': 10, 'MINDISPARITY': 5}


def leftImageOnChange(value):
    prev = TRACKBAR['IMAGE']
    if prev == value:
        return

    # print(f'(leftImageOnChange) {prev} to {value}')
    TRACKBAR['IMAGE'] = value

    leftImageName, leftImage = ImageStore.getByPosition(value + 1)
    leftImageWindow.show(leftImageName, leftImage)

    showDisparities()


def disparityOnChange(value):
    valueInRange = (value + 1) * 16

    prev = TRACKBAR['DISPARITY']
    if prev == valueInRange:
        return

    # print(f'(disparityOnChange) {prev} to {valueInRange}')
    TRACKBAR['DISPARITY'] = valueInRange

    showDisparities()


def blockSizeOnChange(value):
    valueInRange = (value * 2) + 5

    prev = TRACKBAR['BLOCKSIZE']
    if prev == valueInRange:
        return

    # print(f'(blockSizeOnChange) {prev} to {valueInRange}')
    TRACKBAR['BLOCKSIZE'] = valueInRange

    showDisparities()


def filterSizeOnChange(value):
    valueInRange = (value * 2) + 5

    prev = TRACKBAR['PREFILTERSIZE']
    if prev == valueInRange:
        return

    # print(f'(filterSizeOnChange) {prev} to {valueInRange}')
    TRACKBAR['PREFILTERSIZE'] = valueInRange

    showDisparities()


def filterCapOnChange(value):
    prev = TRACKBAR['PREFILTERCAP']
    if prev == value:
        return

    # print(f'(filterCapOnChange) {prev} to {value}')
    TRACKBAR['PREFILTERCAP'] = value

    showDisparities()


def tThresholdOnChange(value):
    prev = TRACKBAR['TEXTURETHRESHOLD']
    if prev == value:
        return

    # print(f'(tThresholdOnChange) {prev} to {value}')
    TRACKBAR['TEXTURETHRESHOLD'] = value

    showDisparities()


def minDisparityOnChange(value):
    prev = TRACKBAR['MINDISPARITY']
    if prev == value:
        return

    # print(f'(minDisparityOnChange) {prev} to {value}')
    TRACKBAR['MINDISPARITY'] = value

    showDisparities()


"""
Main function
"""

mainWindow = Window('Main', scale=0.3)
mainWindow.addTrackbar('Left Image ', (0, imageCounter - 2), leftImageOnChange)
mainWindow.addTrackbar('Disparity ', (0, 30), disparityOnChange)
mainWindow.addTrackbar('Block Size ', (0, 20), blockSizeOnChange)
baseImageName, baseImage = ImageStore.getByPosition(0)
mainWindow.show(baseImageName, baseImage)

leftImageWindow = Window('Left Image', scale=0.3, offset=(0, 455))
dispImageName, dispImage = ImageStore.getByPosition(1)
leftImageWindow.show(dispImageName, dispImage)

disparityWindow = Window('Disparity', offset=(420, 0))
disparityWindow.addTrackbar('PreFilterSize', (2, 25), filterSizeOnChange)
disparityWindow.addTrackbar('PreFilterCap', (5, 62), filterCapOnChange)
disparityWindow.addTrackbar('TextureThreshold', (10, 100), tThresholdOnChange)
disparityWindow.addTrackbar('MinDisparity', (5, 25), minDisparityOnChange)

leftImageOnChange(0)


print('(main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

[print('(main) Image Stats ({0}):\n       {1}'.format(name, "\n       ".join(prints)))
 for [name, prints] in sorted(imageStats.items())]

print('(main) Closing all windows.')
cv2.destroyAllWindows()
