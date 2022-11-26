"""
U3 app
"""
import os
import cv2
from glob import glob
from GUI.Window import Window
from Stores.ImageStore import ImageStore
from detector import analyzeImage

"""
Load Images
"""
imageCounter = 0
globPath = os.path.join(os.path.abspath('./images'), '*.png')

for file in sorted(glob(globPath)):
    image = cv2.imread(file)
    imageName = file.split('/')[-1].split('.')[0]
    ImageStore.add(imageName, cv2.cvtColor(image, cv2.COLOR_RGB2GRAY))
    imageCounter += 1
    print(f'(main) Image loaded: {imageName}')

"""
Trackbar functions
"""

TRACKBAR = {'IMAGE': -1, 'STEP': -1}


def imageOnChange(value):
    temp = TRACKBAR['IMAGE']
    if temp == value:
        return

    print(f'(imageOnChange) {temp} to {value}')
    TRACKBAR['IMAGE'] = value

    [imageName, image] = ImageStore.getByPosition(value)
    analyzeImage(imageName, image)

    window.setTrackbar('Step ', 0)
    stepOnChange(0)


def stepOnChange(value):
    if value == 0:
        # show original Image
        imageValue = TRACKBAR['IMAGE']
        [imageName, image] = ImageStore.getByPosition(imageValue)
        window.show(imageName, image)
        return

    temp = TRACKBAR['STEP']
    if temp == value:
        return

    print(f'(stepOnChange) {temp} to {value}')
    TRACKBAR['STEP'] = value

    [imageName, image] = ImageStore.getByPosition(value + imageCounter - 1)

    window.show(imageName, image)


"""
Main function
"""

window = Window('Main')
window.addTrackbar(
    'Image Select ', (0, imageCounter - 1), imageOnChange)
window.addTrackbar('Step ', (0, 10), stepOnChange) # TODO: replace max value with max amount of steps

imageOnChange(0)  # to trigger first image generation

print('(main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

print('(main) Closing all windows.')
cv2.destroyAllWindows()
