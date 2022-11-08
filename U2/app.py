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


def noopFunc(arg):
    print('(noopFunc)', arg)


imageWindow.addTrackbar('Test', 0, 5, noopFunc)

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
