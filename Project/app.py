"""
Project App
"""

import cv2
from VideoThreader import VideoThreader
from DetectorThreader import DetectorThreader
from detector import detectUpperBody, upperBodyClassifier
from Window import Window
from ImageStore import ImageStore


"""
Trackbar functions
"""

TRACKBAR = {'SCALEFACTOR': 1.05, 'MINNEIGHBORS': 5,
            'MINSIZEX': 40, 'MINSIZEY': 80}


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


def exitProgram():
    print('(main) Closing all windows.')
    VideoThread.stop()
    DetectorThread.stop()
    cv2.destroyAllWindows()
    exit()


mainWindow = Window('Live Detection Feed', scale=0.75)
mainWindow.addTrackbar('Scale Factor ', (0, 49), onChange, 'SCALEFACTOR')
mainWindow.setTrackbar('Scale Factor ', 5)
mainWindow.addTrackbar('Min Neighbors ', (0, 9), onChange, 'MINNEIGHBORS')
mainWindow.setTrackbar('Min Neighbors ', 5)
mainWindow.addTrackbar('Min Size X ', (0, 499), onChange, 'MINSIZEX')
mainWindow.setTrackbar('Min Size X ', 40)
mainWindow.addTrackbar('Min Size Y ', (0, 499), onChange, 'MINSIZEY')
mainWindow.setTrackbar('Min Size Y ', 80)


VideoThread = VideoThreader(src=0).start()
DetectorThread = DetectorThreader(
    classifier=upperBodyClassifier,
    classifierConfig={
        'scaleFactor': TRACKBAR['SCALEFACTOR'],
        'minNeighbors': TRACKBAR['MINNEIGHBORS'],
        'minSize': (TRACKBAR['MINSIZEX'], TRACKBAR['MINSIZEY'])
    },
    image=VideoThread.getLatestFrame()).start()

print("\n\n---> Press 'ESC' to exit.")
print('---> Awaiting input...\n\n')

while True:
    DetectorThread.setImage(VideoThread.getLatestFrame())

    preview = DetectorThread.getPreview()
    if preview is None:
        # loop until Detector finished first preview image generation
        continue

    mainWindow.show('Live Detection Feed', preview)

    key = cv2.waitKey(1)
    if key == 27:  # key "ESC"
        break
    if VideoThread.stopped:  # if Video feed stopped
        break
    if DetectorThread.stopped:  # if Detector stopped
        break

exitProgram()
