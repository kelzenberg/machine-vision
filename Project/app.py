"""
Project App
"""

import cv2
from CameraThreader import CameraThreader
from RecorderThreader import RecorderThreader
from ImageWriteTimer import ImageWriteTimer
from Window import Window
from detector import detectUpperBody, detectFace
from utils import drawObjectRegions, getTimeSinceEpoch


"""
Trackbar functions
"""

TRACKBAR = {'SCALEFACTOR': 1.05, 'MINNEIGHBORS': 8,
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
    FaceImageWriter.stop(reason='app-shutdown')
    RecorderThread.stop(reason='app-shutdown')
    CameraThread.stop(reason='app-shutdown')
    print('(main) Closing all windows.')
    cv2.destroyAllWindows()
    exit()


CameraThread = CameraThreader(src=0)
RecorderThread = RecorderThreader(
    inputSize=CameraThread.getFrameSize(),
    fps=6,
    recordingLimitSec=10
)
FaceImageWriter = ImageWriteTimer(type='face', interval=10)
CameraThread = CameraThread.start()

mainWindow = Window('Live Detection Feed', scale=0.75)
mainWindow.addTrackbar('Scale Factor ', (0, 49), onChange, 'SCALEFACTOR')
mainWindow.setTrackbar('Scale Factor ', 5)
mainWindow.addTrackbar('Min Neighbors ', (0, 9), onChange, 'MINNEIGHBORS')
mainWindow.setTrackbar('Min Neighbors ', 8)
mainWindow.addTrackbar('Min Size X ', (0, 499), onChange, 'MINSIZEX')
mainWindow.setTrackbar('Min Size X ', 40)
mainWindow.addTrackbar('Min Size Y ', (0, 499), onChange, 'MINSIZEY')
mainWindow.setTrackbar('Min Size Y ', 80)

print("\n\n---> Press 'ESC' to exit.")
print('---> START DETECTING HUMANS...\n\n')

while True:
    latestFrame = CameraThread.getLatestFrame()

    detectedBodies = detectUpperBody(
        latestFrame,
        scaleFactor=TRACKBAR['SCALEFACTOR'],
        minNeighbors=TRACKBAR['MINNEIGHBORS'],
        minSize=(TRACKBAR['MINSIZEX'], TRACKBAR['MINSIZEY'])
    )
    hasDetectedBodies = len(detectedBodies) > 0

    detectedFaces = detectFace(
        latestFrame,
        scaleFactor=TRACKBAR['SCALEFACTOR'],
        minNeighbors=TRACKBAR['MINNEIGHBORS'],
        minSize=(TRACKBAR['MINSIZEX'], TRACKBAR['MINSIZEY'])
    )
    hasDetectedFaces = len(detectedFaces) > 0

    colorImage, grayImage = drawObjectRegions(
        image=latestFrame,
        detected=[
            {
                'type': 'upper body',
                'objects': detectedBodies,
                'color': (255, 255, 0)
            },
            {
                'type': 'face',
                'objects': detectedFaces,
                'color': (0, 255, 255)
            }
        ]
    )

    RecorderThread.updateImage(colorImage, getTimeSinceEpoch())

    if hasDetectedFaces:
        FaceImageWriter.update(latestFrame, detectedFaces)

    if (hasDetectedBodies or hasDetectedFaces) and not RecorderThread.isRecording():
        RecorderThread = RecorderThread.start()

    showArgs = ['Live Detection Feed', grayImage] if not RecorderThread.isRecording() \
        else ['Live Detection Feed - RECORDING', grayImage, (64, 64, 255)]
    mainWindow.show(*showArgs)

    key = cv2.waitKey(1)
    if key == 27:  # key "ESC"
        break
    if CameraThread.hasStopped():  # if Video feed stopped
        break

exitProgram()
