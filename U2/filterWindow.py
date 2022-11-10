from Window import Window
from imageWindow import window as imgWindow

"""
Trackbar Functions
"""

sigmaValue = 0.1


def noopFunc(arg):
    print('(noopFunc)', arg)


def sigmaOnChange(value):
    newValue = (value + 1) / 10

    global sigmaValue
    if sigmaValue == newValue:
        return

    sigmaValue = newValue
    print('(sigma)', sigmaValue)


"""
Window Functions
"""


window = Window('Filter', imgWindow.image,
                offset=(round(imgWindow.preview.shape[0]*1.8), 0))
window.addTrackbar('Sigma: ', 0, 5, sigmaOnChange)
window.addTrackbar('Size: ', 0, 4, noopFunc)
window.show()
