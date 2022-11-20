"""
U3 app
"""
import os
import cv2
from glob import glob
from GUI.Window import Window

"""
Load Images
"""
images = {}
globPath = os.path.join(os.path.abspath('./images'), '*.png')

for file in sorted(glob(globPath)):
    image = cv2.imread(file)
    imageName = file.split('/')[-1]
    images[imageName] = image
    print(f'(main) Image loaded: {imageName}')

"""
Main function
"""

print(f'(main) {len(images)} Images loaded')

print('(main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

print('(main) Closing all windows.')
cv2.destroyAllWindows()
