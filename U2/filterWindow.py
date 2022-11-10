import cv2
from Window import Window
import imageWindow
from filterTrackbars import noopFunc as noop2, sigmaOnChange

window = Window('Filter', imageWindow.window.image,
                offset=(round(imageWindow.window.preview.shape[0]*1.8), 0))
window.addTrackbar('Sigma: ', 0, 5, sigmaOnChange)
window.addTrackbar('Size: ', 0, 4, noop2)
window.show()
