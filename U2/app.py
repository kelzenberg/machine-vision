"""
U2 app
"""
import cv2
from Window import Window
from utils import convertToGrayBGR

"""
Load Image
"""

mainImage = cv2.imread('./Stop.jpg')
grayImage = convertToGrayBGR(mainImage)
print('[DEBUG](main) Image loaded.')


"""
Main function
"""

imageWindow = Window('Image', grayImage)
imageWindow.show()

print('[DEBUG](main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

print('[DEBUG](main) Closing all windows.')
cv2.destroyAllWindows()
