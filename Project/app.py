"""
Project App
"""

import cv2
from glob import glob
from os import path as ospath

from Window import Window
from ImageStore import ImageStore


"""
Load Video Feed
"""


def loadVideoFeed():
    pass


"""
Trackbar functions
"""

TRACKBAR = {'FOO': -1}


def defaultOnChange(value):
    prev = TRACKBAR['FOO']
    if prev == value:
        return

    print(f'(defaultOnChange) changed from {prev} to {value}')
    TRACKBAR['FOO'] = value

    pass


"""
Main function
"""

mainWindow = Window('Live Feed', scale=0.3)
mainWindow.addTrackbar('Foo ', (0, 1), defaultOnChange)

print("\n\n---> Press 'ESC' to exit.")
print('---> Awaiting input...\n\n')

while True:
    key = cv2.waitKey(0)
    if key == 27:  # key "ESC"
        break

print('(main) Closing all windows.')
cv2.destroyAllWindows()
