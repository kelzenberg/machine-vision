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

TRACKBAR = {'IMAGE': -1, 'DISPLAY': -1}


def selectionOnChange(value):
    temp = TRACKBAR['IMAGE']
    if temp == value:
        return

    print(f'(selectionOnChange) {temp} to {value}')
    TRACKBAR['IMAGE'] = value

    imageName = f'DOW{value + 1}'
    analyzeImage(imageName)

    displayOnChange(0)
    window.setTrackbar('Display ', 0)
    window.show(imageName, ImageStore.getByName(imageName))


def displayOnChange(value):
    temp = TRACKBAR['DISPLAY']
    if temp == value:
        return

    print(f'(displayValueOnChange) {temp} to {value}')
    TRACKBAR['DISPLAY'] = value

    if value == 0:
        # show original Image
        imageValue = TRACKBAR['IMAGE']
        imageName = f'DOW{imageValue + 1}'
        window.show(imageName, ImageStore.getByName(imageName))
        return

    [imageName, image] = ImageStore.getByPosition(value + imageCounter - 1)

    window.show(imageName, image)


"""
Main function
"""

window = Window('Main')
window.addTrackbar(
    'Image Select ', (0, ImageStore.size() - 1), selectionOnChange)
window.addTrackbar('Display ', (0, 11), displayOnChange)

selectionOnChange(0)  # to trigger first image

print('(main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

print('(main) Closing all windows.')
cv2.destroyAllWindows()
