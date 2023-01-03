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
Trackbar functions
"""

TRACKBAR = {'IMAGE': -1, 'DISPARITY': 0, 'BLOCKSIZE': 0}


def leftImageOnChange(value):
    prev = TRACKBAR['IMAGE']
    if prev == value:
        return

    # print(f'(leftImageOnChange) {prev} to {value}')
    TRACKBAR['IMAGE'] = value

    [baseImageName, baseImage] = ImageStore.getByPosition(0)
    [dispImageName, dispImage] = ImageStore.getByPosition(value + 1)

    # Do something with the image
    findDisparities((baseImageName, baseImage), (dispImageName,
                    dispImage), TRACKBAR['DISPARITY'], TRACKBAR['BLOCKSIZE'])

    leftImageWindow.show(dispImageName, dispImage)

    disparityImage = ImageStore.getByName('disparity')
    disparityWindow.show('disparity', disparityImage, withText=False)


def disparityOnChange(value):
    prev = TRACKBAR['DISPARITY']
    if prev == value:
        return

    # print(f'(disparityOnChange) {prev} to {value}')
    TRACKBAR['DISPARITY'] = value

    [baseImageName, baseImage] = ImageStore.getByPosition(0)
    [dispImageName, dispImage] = ImageStore.getByPosition(
        TRACKBAR['IMAGE'] + 1)

    findDisparities((baseImageName, baseImage), (dispImageName,
                    dispImage), value, TRACKBAR['BLOCKSIZE'])

    disparityImage = ImageStore.getByName('disparity')
    disparityWindow.show('disparity', disparityImage, withText=False)


def blockSizeOnChange(value):
    prev = TRACKBAR['BLOCKSIZE']
    if prev == value:
        return

    # print(f'(blockSizeOnChange) {prev} to {value}')
    TRACKBAR['BLOCKSIZE'] = value

    [baseImageName, baseImage] = ImageStore.getByPosition(0)
    [dispImageName, dispImage] = ImageStore.getByPosition(
        TRACKBAR['IMAGE'] + 1)

    findDisparities((baseImageName, baseImage), (dispImageName,
                    dispImage), TRACKBAR['DISPARITY'], value)

    disparityImage = ImageStore.getByName('disparity')
    disparityWindow.show('disparity', disparityImage, withText=False)


"""
Main function
"""

mainWindow = Window('Main', scale=0.3)
mainWindow.addTrackbar('Left Image ',
                       (0, imageCounter - 2), leftImageOnChange)
mainWindow.addTrackbar('Disparity ', (0, 30), disparityOnChange)
mainWindow.addTrackbar('Block Size ', (0, 20), blockSizeOnChange)
[baseImageName, baseImage] = ImageStore.getByPosition(0)
mainWindow.show(baseImageName, baseImage)

leftImageWindow = Window('Left Image', scale=0.3, offset=(0, 455))
disparityWindow = Window('Disparity', offset=(420, 0))

leftImageOnChange(0)  # to trigger first image generation

print('(main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

[print('(main) Image Stats ({0}):\n       {1}'.format(name, "\n       ".join(prints)))
 for [name, prints] in sorted(imageStats.items())]

print('(main) Closing all windows.')
cv2.destroyAllWindows()
