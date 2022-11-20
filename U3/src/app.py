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

# TODO: run for all images:
name = 'DOW1'
analyzedImage = analyzeImage(name)
window = Window(name)
window.show(name, analyzedImage)

print('(main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

print('(main) Closing all windows.')
cv2.destroyAllWindows()
