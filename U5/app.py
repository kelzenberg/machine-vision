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

TRACKBAR = {'MATCHER': 0, 'IMAGE': -1, 'NUMDISPARITIES': 16, 'BLOCKSIZE': 5, 'PREFILTERSIZE': 5,
            'PREFILTERCAP': 5, 'TEXTURETHRESHOLD': 10, 'MINDISPARITY': 5}


def blockMatcherOnChange(value):
    prev = TRACKBAR['MATCHER']
    if prev == value:
        return

    print(
        f'(blockMatcherOnChange) {"SGBM" if prev == 1 else "BM"} to {"SGBM" if value == 1 else "BM"}')
    TRACKBAR['MATCHER'] = value

    showDisparities()


def rightImageOnChange(value):
    prev = TRACKBAR['IMAGE']
    if prev == value:
        return

    # print(f'(rightImageOnChange) {prev} to {value}')
    TRACKBAR['IMAGE'] = value

    rightImageName, rightImage = ImageStore.getByPosition(value + 1)
    rightImageWindow.show(rightImageName, rightImage)

    showDisparities()


def disparityOnChange(value):
    valueInRange = (value + 1) * 16

    prev = TRACKBAR['NUMDISPARITIES']
    if prev == valueInRange:
        return

    # print(f'(disparityOnChange) {prev} to {valueInRange}')
    TRACKBAR['NUMDISPARITIES'] = valueInRange

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
Utils functions
"""

SAVED_CONFIGS: Dict[str, str] = {}


def saveConfig():
    rightImageName, _ = ImageStore.getByPosition(TRACKBAR['IMAGE'] + 1)
    matcher = TRACKBAR['MATCHER']
    numDisparities = TRACKBAR['NUMDISPARITIES']
    blockSize = TRACKBAR['BLOCKSIZE']
    preFilterSize = TRACKBAR['PREFILTERSIZE']
    preFilterCap = TRACKBAR['PREFILTERCAP']
    textureThreshold = TRACKBAR['TEXTURETHRESHOLD']
    minDisparity = TRACKBAR['MINDISPARITY']

    SAVED_CONFIGS[rightImageName] = f'Matcher: {"SGBM" if matcher == 1 else "BM"} \n\
       Disparity: {numDisparities}\n\
       BlockSize: {blockSize}\n\
       PreFilterSize: {preFilterSize}\n\
       PreFilterCap: {preFilterCap}\n\
       TextureThreshold: {textureThreshold}\n\
       MinDisparity: {minDisparity}'

    print(f'(saveConfig) Saved current trackbar config for {rightImageName}')


def showDisparities():
    left = ImageStore.getByPosition(0)
    right = ImageStore.getByPosition(TRACKBAR['IMAGE'] + 1)

    findDisparities(
        left=left,
        right=right,
        matcher=TRACKBAR['MATCHER'],
        numDisparities=TRACKBAR['NUMDISPARITIES'],
        blockSize=TRACKBAR['BLOCKSIZE'],
        preFilterSize=TRACKBAR['PREFILTERSIZE'],
        preFilterCap=TRACKBAR['PREFILTERCAP'],
        textureThreshold=TRACKBAR['TEXTURETHRESHOLD'],
        minDisparity=TRACKBAR['MINDISPARITY']
    )

    disparityImage = ImageStore.getByName('disparity')
    disparityWindow.show('disparity', disparityImage, withText=False)


"""
Main function
"""

leftImageWindow = Window('Left Image', scale=0.3)
leftImageWindow.addTrackbar('Block Matcher ', (0, 1), blockMatcherOnChange)
leftImageWindow.addTrackbar(
    'Right Image ', (0, imageCounter - 2), rightImageOnChange)
leftImageWindow.addTrackbar('#Disparities ', (0, 30), disparityOnChange)
leftImageWindow.addTrackbar('Block Size ', (0, 20), blockSizeOnChange)
baseImageName, baseImage = ImageStore.getByPosition(0)
leftImageWindow.show(baseImageName, baseImage)

rightImageWindow = Window('Right Image', scale=0.3, offset=(0, 485))
rightImageName, rightImage = ImageStore.getByPosition(1)
rightImageWindow.show(rightImageName, rightImage)

disparityWindow = Window('Disparity', offset=(420, 0))
disparityWindow.addTrackbar('PreFilterSize', (2, 25), filterSizeOnChange)
disparityWindow.addTrackbar('PreFilterCap', (5, 62), filterCapOnChange)
disparityWindow.addTrackbar('TextureThreshold', (10, 100), tThresholdOnChange)
disparityWindow.addTrackbar('MinDisparity', (5, 25), minDisparityOnChange)

rightImageOnChange(0)


print("\n\n---> Press 'ESC' to exit or 'P' to save current trackbar config.")
print('---> Awaiting input...\n\n')

while True:
    key = cv2.waitKey(0)
    if key == 112:  # key "P"
        saveConfig()
    if key == 27:  # key "ESC"
        break

[print("(main) Saved trackbar config for right image '{0}':\n       {1}".format(name, prints))
 for [name, prints] in sorted(SAVED_CONFIGS.items())]

print('(main) Closing all windows.')
cv2.destroyAllWindows()
