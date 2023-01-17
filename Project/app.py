"""
Project App
"""

import cv2
from detector import detectUpperBody
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
    # feed = cv2.VideoCapture(0)
    feed = cv2.VideoCapture("./video/test.mp4")

    if not feed.isOpened():
        print("(main) Cannot access camera feed.")
        exitProgram()

    width = int(feed.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(feed.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(feed.get(cv2.CAP_PROP_FPS))
    fourcc = int(feed.get(cv2.CAP_PROP_FOURCC))
    codec = bytes([v & 255 for v in (fourcc, fourcc >> 8,
                  fourcc >> 16, fourcc >> 24)]).decode() # Source: https://stackoverflow.com/a/71838016
    backendAPI = feed.getBackendName()
    print(f'(main) Video Feed loaded: {width}x{height} @ {fps}fps ({codec}) - via {backendAPI}')

    return feed


def retrieveFrame(feed):
    retrieved, frame = feed.read()
    if not retrieved:
        print("(main) Cannot receive next frame.")
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
mainWindow = Window('Live Detection Feed', scale=0.5)
mainWindow.addTrackbar('Foo ', (0, 1), defaultOnChange)

print("\n\n---> Press 'ESC' to exit.")
print('---> Awaiting input...\n\n')

while True:
    frame = retrieveFrame(feed)
    # detected = detectUpperBody(frame)
    mainWindow.show('Live Detection Feed', frame)

    key = cv2.waitKey(1)
    if key == 27:  # key "ESC"
        break

exitProgram()
