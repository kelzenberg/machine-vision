"""
U4 app
"""

import cv2
from typing import Dict, List
from glob import glob
from os import path as ospath
from Window import Window
from ImageStore import ImageStore

imageStats: Dict[str, List[str]] = {}

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

TRACKBAR = {'IMAGE': -1}


def leftImageOnChange(value):
    prev = TRACKBAR['IMAGE']
    if prev == value:
        return

    # print(f'(leftImageOnChange) {prev} to {value}')
    TRACKBAR['IMAGE'] = value

    [imageName, image] = ImageStore.getByPosition(value + 1)

    # Do something with the image

    leftImageWindow.show(imageName, image)


"""
Main function
"""

mainWindow = Window('Main', scale=0.3)
mainWindow.addTrackbar('Left Image Select ',
                       (0, imageCounter - 2), leftImageOnChange)
[imageName, image] = ImageStore.getByPosition(0)
mainWindow.show(imageName, image)

leftImageWindow = Window('Left Image', scale=0.3, offset=(0, 400))

leftImageOnChange(0)  # to trigger first image generation

print('(main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

[print('(main) Image Stats ({0}):\n       {1}'.format(name, "\n       ".join(prints)))
 for [name, prints] in sorted(imageStats.items())]

print('(main) Closing all windows.')
cv2.destroyAllWindows()
