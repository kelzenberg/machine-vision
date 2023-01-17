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
    feed = cv2.VideoCapture(0)
    # feed = cv2.VideoCapture("./video/front.png")

    if not feed.isOpened():
        print("(main) Cannot access camera feed.")
        exitProgram()

    width = int(feed.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(feed.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(feed.get(cv2.CAP_PROP_FPS))
    fourcc = int(feed.get(cv2.CAP_PROP_FOURCC))
    codec = bytes([v & 255 for v in (fourcc, fourcc >> 8,
                  fourcc >> 16, fourcc >> 24)]).decode()  # Source: https://stackoverflow.com/a/71838016
    backendAPI = feed.getBackendName()
    print(
        f'(main) Video Feed loaded: {width}x{height} @ {fps}fps ({codec}) - via {backendAPI}')

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

TRACKBAR = {'SCALEFACTOR': 1.05, 'MINNEIGHBORS': 5,
            'MINSIZEX': 150, 'MINSIZEY': 300}


def onChange(value, slot):
    tempValue = value
    match slot:
        case 'SCALEFACTOR':
            tempValue = float(f'1.0{value + 1}'
                              if value + 1 < 10
                              else f'1.{value + 1}')
        case 'MINNEIGHBORS':
            tempValue = value + 1
        case 'MINSIZEX':
            tempValue = value + 1
        case 'MINSIZEY':
            tempValue = value + 1

    prev = TRACKBAR[slot]
    if prev == tempValue:
        return

    print(f"(trackbarOnChange) '{slot}' changed from {prev} to {tempValue}")
    TRACKBAR[slot] = tempValue


"""
Main function
"""


feed = loadVideoFeed()
mainWindow = Window('Live Detection Feed', scale=0.75)
mainWindow.addTrackbar('Scale Factor ', (0, 49), onChange, 'SCALEFACTOR')
mainWindow.setTrackbar('Scale Factor ', 5)
mainWindow.addTrackbar('Min Neighbors ', (0, 9), onChange, 'MINNEIGHBORS')
mainWindow.setTrackbar('Min Neighbors ', 5)
mainWindow.addTrackbar('Min Size X ', (0, 499), onChange, 'MINSIZEX')
mainWindow.setTrackbar('Min Size X ', 150)
mainWindow.addTrackbar('Min Size Y ', (0, 499), onChange, 'MINSIZEY')
mainWindow.setTrackbar('Min Size Y ', 300)

print("\n\n---> Press 'ESC' to exit.")
print('---> Awaiting input...\n\n')

while True:
    frame = retrieveFrame(feed)
    detected = detectUpperBody(
        frame,
        scaleFactor=TRACKBAR['SCALEFACTOR'],
        minNeighbors=TRACKBAR['MINNEIGHBORS'],
        minSize=(TRACKBAR['MINSIZEX'], TRACKBAR['MINSIZEY'])
    )
    mainWindow.show('Live Detection Feed', detected)

    key = cv2.waitKey(1)
    if key == 27:  # key "ESC"
        break

exitProgram()
