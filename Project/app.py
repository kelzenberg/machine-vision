"""
Project App
"""

import cv2
from VideoThreader import VideoThreader
from detector import detectUpperBody
from WindowThreader import WindowThreader
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
    WindowThread.stop()
    cv2.destroyAllWindows()
    exit()


VideoThread = VideoThreader(src=0).start()

WindowThread = WindowThreader('Live Detection Feed', scale=0.75, image=VideoThread.getLatestFrame()).start()
WindowThread.addTrackbar('Scale Factor ', (0, 49), onChange, 'SCALEFACTOR')
WindowThread.setTrackbar('Scale Factor ', 5)
WindowThread.addTrackbar('Min Neighbors ', (0, 9), onChange, 'MINNEIGHBORS')
WindowThread.setTrackbar('Min Neighbors ', 5)
WindowThread.addTrackbar('Min Size X ', (0, 499), onChange, 'MINSIZEX')
WindowThread.setTrackbar('Min Size X ', 40)
WindowThread.addTrackbar('Min Size Y ', (0, 499), onChange, 'MINSIZEY')
WindowThread.setTrackbar('Min Size Y ', 80)

print("\n\n---> Press 'ESC' to exit.")
print('---> Awaiting input...\n\n')

while True:
    detected = detectUpperBody(
        VideoThread.getLatestFrame(),
        scaleFactor=TRACKBAR['SCALEFACTOR'],
        minNeighbors=TRACKBAR['MINNEIGHBORS'],
        minSize=(TRACKBAR['MINSIZEX'], TRACKBAR['MINSIZEY'])
    )
    WindowThread.setImage(detected)

    key = cv2.waitKey(1)
    if key == 27:  # key "ESC"
        break
    if VideoThread.stopped:  # if Video feed stopped
        break
    if WindowThread.stopped:  # if Window showing stopped
        break

exitProgram()
