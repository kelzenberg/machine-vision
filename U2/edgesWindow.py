from Window import Window
from images import edgesImage

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
EdgesWindow.addTrackbar('Threshold: ', 0, 255, noopFunc)
EdgesWindow.addTrackbar('Display Image: ', 0, 5, noopFunc)
EdgesWindow.show('edgesImage', edgesImage)
