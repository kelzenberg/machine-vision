import imageWindow
import filterWindow
from Window import Window

"""
Trackbar Functions
"""


def noopFunc(arg):
    print('(noopFunc)', arg)


"""
Window Functions
"""

window = Window('Edges', filterWindow.window.image, scale=0.4,
                offset=(0, round(imageWindow.window.preview.shape[1]/1.25)))
window.addTrackbar('Threshold: ', 0, 255, noopFunc)
window.addTrackbar('Display Image: ', 0, 5, noopFunc)
window.show()
