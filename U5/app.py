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
disparityRange = (0, 30)
blockSizeRange = (0, 20)

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
Trackbar functions
"""

TRACKBAR = {'IMAGE': -1, 'DISPARITY': 16, 'BLOCKSIZE': 5}


def leftImageOnChange(value):
    prev = TRACKBAR['IMAGE']
    if prev == value:
        return

    # print(f'(leftImageOnChange) {prev} to {value}')
    TRACKBAR['IMAGE'] = value

    [baseImageName, baseImage] = ImageStore.getByPosition(0)
    [dispImageName, dispImage] = ImageStore.getByPosition(value + 1)
    leftImageWindow.show(dispImageName, dispImage)

    findDisparities((dispImageName, dispImage), (baseImageName,
                    baseImage), TRACKBAR['DISPARITY'], TRACKBAR['BLOCKSIZE'])

    disparityImage = ImageStore.getByName('disparity')
    disparityWindow.show('disparity', disparityImage, withText=False)


def disparityOnChange(value):
    valueInRange = (value + 1) * 16

    prev = TRACKBAR['DISPARITY']
    if prev == valueInRange:
        return

    print(f'(disparityOnChange) {prev} to {valueInRange}')
    TRACKBAR['DISPARITY'] = valueInRange

    [baseImageName, baseImage] = ImageStore.getByPosition(0)
    [dispImageName, dispImage] = ImageStore.getByPosition(
        TRACKBAR['IMAGE'] + 1)

    findDisparities((dispImageName, dispImage), (baseImageName,
                    baseImage), valueInRange, TRACKBAR['BLOCKSIZE'])

    disparityImage = ImageStore.getByName('disparity')
    disparityWindow.show('disparity', disparityImage, withText=False)


def blockSizeOnChange(value):
    valueInRange = (value * 2) + 5

    prev = TRACKBAR['BLOCKSIZE']
    if prev == valueInRange:
        return

    print(f'(blockSizeOnChange) {prev} to {valueInRange}')
    TRACKBAR['BLOCKSIZE'] = valueInRange

    [baseImageName, baseImage] = ImageStore.getByPosition(0)
    [dispImageName, dispImage] = ImageStore.getByPosition(
        TRACKBAR['IMAGE'] + 1)

    findDisparities((dispImageName, dispImage), (baseImageName,
                    baseImage), TRACKBAR['DISPARITY'], valueInRange)

    disparityImage = ImageStore.getByName('disparity')
    disparityWindow.show('disparity', disparityImage, withText=False)


"""
Main function
"""

mainWindow = Window('Main', scale=0.3)
mainWindow.addTrackbar('Left Image ', (0, imageCounter - 2), leftImageOnChange)
mainWindow.addTrackbar('Disparity ', disparityRange, disparityOnChange)
mainWindow.addTrackbar('Block Size ', blockSizeRange, blockSizeOnChange)

leftImageWindow = Window('Left Image', scale=0.3, offset=(0, 455))
disparityWindow = Window('Disparity', offset=(420, 0))

trackbarWindow = Window('Optional Trackbars', scale=0.3, offset=(420, 455))
trackbarWindow.addTrackbar('PreFilterType', (1, 1), None)
trackbarWindow.addTrackbar('PreFilterSize', (2, 25), None)
trackbarWindow.addTrackbar('PreFilterCap', (5, 62), None)
trackbarWindow.addTrackbar('TextureThreshold', (10, 100), None)
trackbarWindow.addTrackbar('UniquenessRatio', (15, 100), None)
trackbarWindow.addTrackbar('SpeckleRange', (0, 100), None)
trackbarWindow.addTrackbar('SpeckleWindowSize', (3, 25), None)
trackbarWindow.addTrackbar('Disp12MaxDiff', (5, 25), None)
trackbarWindow.addTrackbar('MinDisparity', (5, 25), None)

[baseImageName, baseImage] = ImageStore.getByPosition(0)
mainWindow.show(baseImageName, baseImage)
leftImageOnChange(0)  # to trigger first image generation

print('(main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

[print('(main) Image Stats ({0}):\n       {1}'.format(name, "\n       ".join(prints)))
 for [name, prints] in sorted(imageStats.items())]

print('(main) Closing all windows.')
cv2.destroyAllWindows()
