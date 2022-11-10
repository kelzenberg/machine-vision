import cv2
from utils import convertToGrayBGR
from Window import Window
from imageTrackbars import noopFunc as noop1, filterOnChange

"""
Load Image
"""

mainImage = cv2.imread('./Stop.jpg')
grayImage = convertToGrayBGR(mainImage)
print('(main) Image loaded.')

window = Window('Image', grayImage)
window.addTrackbar('Operation: ', 0, 3, noop1)
window.addTrackbar('Filter: ', 0, 2, filterOnChange)
window.show()
