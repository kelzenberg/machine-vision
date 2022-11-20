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
globPath = os.path.join(os.path.abspath('./images'), '*.png')

for file in sorted(glob(globPath)):
    image = cv2.imread(file)
    imageName = file.split('/')[-1].split('.')[0]
    ImageStore.add(imageName, cv2.cvtColor(image, cv2.COLOR_RGB2GRAY))
    print(f'(main) Image loaded: {imageName}')

"""
Trackbar functions
"""

TRACKBAR = {'IMAGE': -1, 'DISPLAY': -1}


def selectionOnChange(value):
    stored = TRACKBAR['IMAGE']
    if stored == value:
        return

    print(f'(selectionOnChange) {stored} to {value}')
    TRACKBAR['IMAGE'] = value
    stored = value

    imageName = f'DOW{stored + 1}'
    analyzeImage(imageName)

    displayOnChange(0)
    window.setTrackbar('Display ', 0)
    window.show(imageName, ImageStore.get(imageName))


def displayOnChange(value):
    stored = TRACKBAR['DISPLAY']
    if stored == value:
        return

    print(f'(displayValueOnChange) {stored} to {value}')
    TRACKBAR['DISPLAY'] = value
    stored = value

    displayValue = TRACKBAR['IMAGE']
    imageName = f'DOW{displayValue + 1}'
    match stored:
        case 1:
            imageName = 'median'
        case 2:
            imageName = 'sobel'
        case 3:
            imageName = 'opening'
        case 4:
            imageName = 'normal'
        case 5:
            imageName = 'binary'

    window.show(imageName, ImageStore.get(imageName))


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
