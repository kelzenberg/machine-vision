from Window import Window
from images import edgesImage

"""
Trackbar Functions
"""

tresholdValueRange = (0, 255)
displayValueRange = (0, 5)


def noopFunc(arg):
    print('(noopFunc)', arg)


"""
Window Functions
"""

EdgesWindow = Window('Edges', scale=0.5, offset=(
    round(edgesImage.shape[0]*0.4), 0))
EdgesWindow.addTrackbar('Threshold: ', tresholdValueRange, noopFunc)
EdgesWindow.addTrackbar('Display Image: ', displayValueRange, noopFunc)
EdgesWindow.show('edgesImage', edgesImage)
