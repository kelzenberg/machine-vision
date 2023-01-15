"""
Project App
"""

import cv2
from glob import glob
from os import path as ospath

from Window import Window
from ImageStore import ImageStore


"""
Utils
"""


def exitProgram():
    global feed
    if feed:
        print('(main) Stopping video feed.')
        feed.release()

    print('(main) Closing all windows.')
    cv2.destroyAllWindows()
    exit()


"""
Video Feed
"""


def loadVideoFeed():
    feed = cv2.VideoCapture(0)
    if not feed.isOpened():
        print("Cannot access camera feed.")
        exitProgram()
    return feed


def retrieveFrame(feed):
    retrieved, frame = feed.read()
    if not retrieved:
        print("Cannot receive next frame.")
        exitProgram()
    return frame


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


feed = loadVideoFeed()
mainWindow = Window('Live Feed', scale=0.5)
mainWindow.addTrackbar('Foo ', (0, 1), defaultOnChange)

print("\n\n---> Press 'ESC' to exit.")
print('---> Awaiting input...\n\n')

while True:
    frame = retrieveFrame(feed)
    mainWindow.show('Live Feed', frame)

    key = cv2.waitKey(1)
    if key == 27:  # key "ESC"
        break

exitProgram()
