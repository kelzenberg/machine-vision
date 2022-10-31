"""U1 app"""
import cv2

mainImage = cv2.imread('./Lena.bmp')
grayImage = cv2.cvtColor(mainImage, cv2.COLOR_RGB2GRAY)
print('[DEBUG](main) Image loaded.')

mainWindowName = 'main'
cv2.namedWindow(mainWindowName, cv2.WINDOW_KEEPRATIO)
cv2.moveWindow(mainWindowName, 100, 100)

rectPoints = [None, None]
color = (0, 0, 255)  # Red in BGR


def showImage(image, windowName=mainWindowName):
    print('[DEBUG](showImage) Show image in window:', windowName)
    cv2.imshow(windowName, image)


def setRectanglePoints(x: int, y: int, slot: int):
    if slot == 0:
        rectPoints[0] = (x, y)
        return
    if slot == 1:
        rectPoints[1] = (x, y)
        return


def drawRectOnImage(image):
    point1 = rectPoints[0]
    point2 = rectPoints[1]

    if point1 != None and point2 != None:
        return cv2.rectangle(image, point1, point2, color, 2)


def onMouse(event: int, x: int, y: int, flags: int, userdata=None):
    if event == 1:  # left-mouse-down
        print('[DEBUG](onMouse) @Left-Click-DOWN:', x, y, flags)
        setRectanglePoints(x, y, slot=0)
        return

    if event == 4:  # left-mouse-up
        print('[DEBUG](onMouse) @Left-Click-UP:', x, y, flags)
        setRectanglePoints(x, y, slot=1)

        BGRGrayImage = cv2.cvtColor(grayImage, cv2.COLOR_GRAY2BGR)
        showImage(drawRectOnImage(BGRGrayImage))
        return


showImage(grayImage)
cv2.setMouseCallback(mainWindowName, onMouse)

print('[DEBUG](main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

print('[DEBUG](main) Closing all windows.')
cv2.destroyAllWindows()
