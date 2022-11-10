"""
U2 app
"""
import cv2
from Window import Window
from imageTrackbars import noopFunc as noop1
from filterTrackbars import noopFunc as noop2
from utils import convertToGrayBGR

"""
Load Image
"""

mainImage = cv2.imread('./Stop.jpg')
grayImage = convertToGrayBGR(mainImage)
print('(main) Image loaded.')


"""
Main function
"""

imageWindow = Window('Image', grayImage)
imageWindow.addTrackbar('Operation: ', 0, 3, noop1)
imageWindow.addTrackbar('Filter: ', 0, 2, noop1)
imageWindow.show()

filterWindow = Window('Filter', imageWindow.image,
                      offset=(round(imageWindow.preview.shape[0]*1.8), 0))
filterWindow.addTrackbar('Sigma: ', 0, 255, noop2)
filterWindow.addTrackbar('Size: ', 0, 4, noop2)
filterWindow.show()

edgesWindow = Window('Edges', filterWindow.image, scale=0.4,
                     offset=(0, round(imageWindow.preview.shape[1]/1.5)))
edgesWindow.show()

print('(main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

print('(main) Closing all windows.')
cv2.destroyAllWindows()
