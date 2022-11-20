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
Main function
"""

displayValue = 0


def displayOnChange(value):
    global displayValue
    if displayValue == value:
        return

    displayValue = value
    print(f'(displayValueOnChange) {displayValue} to {value}')

    imageName = name
    match displayValue:
        case 1:
            imageName = 'median'
        case 2:
            imageName = 'opening'

    window.show(imageName, ImageStore.get(imageName))


# TODO: run for all images:
name = 'DOW1'
analyzedImage = analyzeImage(name)

window = Window(name)
window.addTrackbar('Display ', (0, 11), displayOnChange)
window.show(name, analyzedImage)

print('(main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

print('(main) Closing all windows.')
cv2.destroyAllWindows()
