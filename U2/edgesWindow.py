from Window import Window
from images import edgesImage

thresholdTrackbar = 'Threshold: '
thresholdValueRange = (0, 255)
displayTrackbar = 'Display Image: '
displayValueRange = (0, 5)

"""
Trackbar Functions
"""


def noopFunc(arg):
    print('(noopFunc)', arg)


"""
Window Functions
"""

EdgesWindow = Window('Edges', scale=0.5, offset=(
    round(edgesImage.shape[0]*0.4), 0))
EdgesWindow.addTrackbar(thresholdTrackbar, thresholdValueRange, noopFunc)
EdgesWindow.addTrackbar(displayTrackbar, displayValueRange, noopFunc)
EdgesWindow.show('edgesImage', edgesImage)
