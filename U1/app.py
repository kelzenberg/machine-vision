"""U1 app"""
import cv2

mainImage = cv2.imread('./Lena.bmp')
grayImage = cv2.cvtColor(cv2.cvtColor(
    mainImage, cv2.COLOR_RGB2GRAY), cv2.COLOR_GRAY2BGR)
print('[DEBUG](main) Image loaded.')

mainWindowName = 'main'
zoomWindowName = 'zoom'
cv2.namedWindow(mainWindowName, cv2.WINDOW_KEEPRATIO)
cv2.moveWindow(mainWindowName, 100, 100)

rectPoints = [None, None]
redColor = (0, 0, 255)  # Red in BGR
zoomValue = 0


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


def validatePoints(points):
    [pointA, pointB] = points
    x1 = pointA[0] if pointA[0] < pointB[0] else pointB[0]
    x2 = pointB[0] if pointB[0] > pointA[0] else pointA[0]
    y1 = pointA[1] if pointA[1] < pointB[1] else pointB[1]
    y2 = pointB[1] if pointB[1] > pointA[1] else pointA[1]
    return [(x1, y1), (x2, y2)]


def createZoomWindow(points):
    [pointA, pointB] = points
    [x1, y1] = pointA
    [x2, y2] = pointB
    croppedImage = mainImage[y1:y2, x1:x2]

    cv2.namedWindow(zoomWindowName, cv2.WINDOW_AUTOSIZE)
    cv2.moveWindow(zoomWindowName, 666, 100)
    cv2.imshow(zoomWindowName, croppedImage)


def onMouse(event: int, x: int, y: int, flags: int, userdata=None):
    if event == 1:  # left-mouse-down
        print('[DEBUG](onMouse) @Left-Click-DOWN:', x, y, flags)
        setRectanglePoints(x, y, slot=0)
        return

    if event == 4:  # left-mouse-up
        print('[DEBUG](onMouse) @Left-Click-UP:', x, y, flags)
        setRectanglePoints(x, y, slot=1)

        if rectPoints[0] != None and rectPoints[1] != None:
            [fromPoint, toPoint] = validatePoints(rectPoints)

            if toPoint[0]-fromPoint[0] > 0 and toPoint[1]-fromPoint[1] > 0:
                showImage(cv2.rectangle(grayImage.copy(),
                                        fromPoint, toPoint, redColor, 2))
                createZoomWindow([fromPoint, toPoint])
        return


def zoomOnChange(value):
    global zoomValue
    if zoomValue != value:
        print(f'[DEBUG](zoomOnChange) Zoom from {zoomValue} to {value}')
        zoomValue = value


cv2.setMouseCallback(mainWindowName, onMouse)
cv2.createTrackbar('Zoom:', mainWindowName, zoomValue, 3, zoomOnChange)
# Trackbar creates errors on CV2 v4.6.x release -> fix is in v5.x, see https://github.com/opencv/opencv/issues/22561#issuecomment-1257164504

showImage(grayImage)

print('[DEBUG](main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

print('[DEBUG](main) Closing all windows.')
cv2.destroyAllWindows()
