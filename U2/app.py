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
print('(main) Image loaded.')


"""
Main function
"""

imageWindow = Window('Image', grayImage)
imageWindow.show()
filterWindow = Window('Filter', imageWindow.image,
                      offset=(round(imageWindow.preview.shape[0]*1.8), 0))
filterWindow.show()

print('(main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

print('(main) Closing all windows.')
cv2.destroyAllWindows()
