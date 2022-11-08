"""
U2 app
"""
import cv2
from utils import showImage, convertToGrayBGR

"""
Load Image
"""

mainImage = cv2.imread('./Stop.jpg')
grayImage = convertToGrayBGR(mainImage)
print('[DEBUG](main) Image loaded.')

mainWindowName = 'Main'
cv2.namedWindow(mainWindowName, cv2.WINDOW_KEEPRATIO)
cv2.moveWindow(mainWindowName, 100, 100)
cv2.setWindowProperty(mainWindowName, cv2.WND_PROP_TOPMOST, 1)


"""
Main function
"""

# Logic goes here

showImage(mainWindowName, grayImage)

print('[DEBUG](main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

print('[DEBUG](main) Closing all windows.')
cv2.destroyAllWindows()
