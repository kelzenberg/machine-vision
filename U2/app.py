"""
U2 app
"""
import cv2
from Window import Window
from imageTrackbars import noopFunc
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
imageWindow.addTrackbar('Operation: ', 0, 3, noopFunc)
imageWindow.addTrackbar('Filter: ', 0, 2, noopFunc)
imageWindow.show()

filterWindow = Window('Filter', imageWindow.image,
                      offset=(round(imageWindow.preview.shape[0]*1.8), 0))
filterWindow.show()

edgesWindow = Window('Edges', filterWindow.image, scale=0.4,
                     offset=(0, round(imageWindow.preview.shape[1]/1.5)))
edgesWindow.show()

print('(main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

print('(main) Closing all windows.')
cv2.destroyAllWindows()
