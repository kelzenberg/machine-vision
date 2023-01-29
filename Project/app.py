"""
Project App
"""

import cv2
from VideoThreader import VideoThreader
from RecorderThreader import RecorderThreader
from detector import prepareForClassifier, drawResults, detectUpperBody, detectFace
from Window import Window


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
    RecorderThread.stop(reason='app-shutdown')
    VideoThread.stop(reason='app-shutdown')
    cv2.destroyAllWindows()
    exit()


VideoThread = VideoThreader(src=0).start()
RecorderThread = RecorderThreader(inputSize=VideoThread.getFrameSize())
mainWindow = Window('Live Detection Feed', scale=0.75)
mainWindow.addTrackbar('Scale Factor ', (0, 49), onChange, 'SCALEFACTOR')
mainWindow.setTrackbar('Scale Factor ', 5)
mainWindow.addTrackbar('Min Neighbors ', (0, 9), onChange, 'MINNEIGHBORS')
mainWindow.setTrackbar('Min Neighbors ', 5)
mainWindow.addTrackbar('Min Size X ', (0, 499), onChange, 'MINSIZEX')
mainWindow.setTrackbar('Min Size X ', 40)
mainWindow.addTrackbar('Min Size Y ', (0, 499), onChange, 'MINSIZEY')
mainWindow.setTrackbar('Min Size Y ', 80)

print("\n\n---> Press 'ESC' to exit.")
print('---> Awaiting input...\n\n')

while True:
    gray, preview = prepareForClassifier(VideoThread.getLatestFrame())

    detectedBodies = detectUpperBody(
        gray,
        scaleFactor=TRACKBAR['SCALEFACTOR'],
        minNeighbors=TRACKBAR['MINNEIGHBORS'],
        minSize=(TRACKBAR['MINSIZEX'], TRACKBAR['MINSIZEY'])
    )
    preview = drawResults(preview, detectedBodies, 'upper body')

    detectedFaces = detectFace(
        gray,
        scaleFactor=TRACKBAR['SCALEFACTOR'],
        minNeighbors=TRACKBAR['MINNEIGHBORS'],
        minSize=(TRACKBAR['MINSIZEX'], TRACKBAR['MINSIZEY'])
    )
    preview = drawResults(preview, detectedFaces, 'face')

    isRecordingFeed = RecorderThread.isRecording()
    hasDetectedObjects = len(detectedBodies) > 0 or len(detectedFaces) > 0

    if hasDetectedObjects:
        RecorderThread.updateImage(preview)
        if not isRecordingFeed:
            RecorderThread = RecorderThread.start()

    previewMessage = 'Live Detection Feed' if not isRecordingFeed else 'Live Detection Feed - RECORDING'
    mainWindow.show(previewMessage, preview)

    key = cv2.waitKey(1)
    if key == 27:  # key "ESC"
        break
    if VideoThread.hasStopped():  # if Video feed stopped
        break

exitProgram()
