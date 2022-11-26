"""
U3 app
"""

import cv2
from glob import glob
from os import path as ospath
from Window import Window
from ImageStore import ImageStore
from detector import analyzeImage, imageStats

"""
Load Images
"""
imageCounter = 0
globPath = ospath.join(ospath.abspath('./images'), '*.png')

for file in sorted(glob(globPath)):
    image = cv2.imread(file)
    imageName = file.split('/')[-1].split('.')[0]
    ImageStore.add(imageName, cv2.cvtColor(image, cv2.COLOR_RGB2GRAY))
    imageCounter += 1
    print(f'(main) Image loaded: {imageName}')

"""
Trackbar functions
"""

TRACKBAR = {'IMAGE': -1, 'STEP': 0}


def imageOnChange(value):
    prev = TRACKBAR['IMAGE']
    if prev == value:
        return

    print(f'(imageOnChange) {prev} to {value}')
    TRACKBAR['IMAGE'] = value

    [imageName, image] = ImageStore.getByPosition(value)

    analyzeImage(imageName, image)
    stepOnChange(TRACKBAR['STEP'])


def stepOnChange(value):
    prev = TRACKBAR['STEP']
    if prev != value:
        print(f'(stepOnChange) {prev} to {value}')

    TRACKBAR['STEP'] = value

    [imageName, image] = ImageStore.getByPosition(
        TRACKBAR['IMAGE'] if value == 0  # show original Image
        else value + imageCounter - 1)

    window.show(imageName, image)


"""
Main function
"""

window = Window('Main')
window.addTrackbar(
    'Image Select ', (0, imageCounter - 1), imageOnChange)
# TODO: replace max value with max amount of steps
window.addTrackbar('Step ', (0, 11), stepOnChange)

imageOnChange(0)  # to trigger first image generation

print('(main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

[print('(main) Image Stats ({0}):\n       {1}'.format(name, "\n       ".join(prints)))
 for [name, prints] in sorted(imageStats.items())]

print('(main) Closing all windows.')
cv2.destroyAllWindows()
