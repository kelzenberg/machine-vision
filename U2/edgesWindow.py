import imageWindow
import filterWindow
from Window import Window
from edgesTrackbars import noopFunc as noop3

window = Window('Edges', filterWindow.window.image, scale=0.4,
                     offset=(0, round(imageWindow.window.preview.shape[1]/1.25)))
window.addTrackbar('Threshold: ', 0, 255, noop3)
window.addTrackbar('Display Image: ', 0, 5, noop3)
window.show()
