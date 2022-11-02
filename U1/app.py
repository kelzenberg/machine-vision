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
cv2.setWindowProperty(mainWindowName, cv2.WND_PROP_TOPMOST, 1)

rectPoints = [None, None]
sortedRectPoints = [None, None]
redColor = (0, 0, 255)  # Red in BGR
zoomValue = 0
lutValue = 0


def showImage(image, windowName):
    print('[DEBUG](showImage) Show image in window:', windowName)
    cv2.imshow(windowName, image)


def setRectanglePoints(x: int, y: int, slot: int):
    if slot == 0:
        rectPoints[0] = (x, y)
        return
    if slot == 1:
        rectPoints[1] = (x, y)
        return


def sortRectanglePoints(points):
    [pointA, pointB] = points
    x1 = pointA[0] if pointA[0] < pointB[0] else pointB[0]
    x2 = pointB[0] if pointB[0] > pointA[0] else pointA[0]
    y1 = pointA[1] if pointA[1] < pointB[1] else pointB[1]
    y2 = pointB[1] if pointB[1] > pointA[1] else pointA[1]
    return [(x1, y1), (x2, y2)]


def drawRectangle(points):
    print(f'[DEBUG](drawRectangle) with Points {points}')
    [fromPoint, toPoint] = points
    showImage(cv2.rectangle(grayImage.copy(),
                            fromPoint, toPoint, redColor, 2), mainWindowName)


def initZoomWindow():
    cv2.destroyWindow(zoomWindowName)
    cv2.namedWindow(zoomWindowName, cv2.WINDOW_AUTOSIZE)
    cv2.moveWindow(zoomWindowName, 666, 100)


def updateZoomWindow(points):
    print(f'[DEBUG](updateZoomWindow) with Points {points}')
    [(x1, y1), (x2, y2)] = points
    croppedImage = mainImage[y1:y2, x1:x2]
    zoomedImage = cv2.resize(
        croppedImage, None, fx=zoomValue + 1, fy=zoomValue + 1, interpolation=cv2.INTER_CUBIC)
    showImage(zoomedImage, zoomWindowName)


def onMouse(event: int, x: int, y: int, flags: int, userdata=None):
    if event == 1:  # left-mouse-down
        print('[DEBUG](onMouse) @Left-Click-DOWN:', x, y, flags)
        setRectanglePoints(x, y, slot=0)
        initZoomWindow()
        return

    if event == 0 and flags == 1:  # mouse moved & left-mouse down
        print('[DEBUG](onMouse) @Mouse-Moved:', x, y, flags)
        setRectanglePoints(x, y, slot=1)

        if rectPoints[0] == None or rectPoints[1] == None:
            return

        global sortedRectPoints
        sortedRectPoints = sortRectanglePoints(rectPoints)

        if sortedRectPoints[1][0]-sortedRectPoints[0][0] <= 0 or sortedRectPoints[1][1]-sortedRectPoints[0][1] <= 0:
            return

        drawRectangle(sortedRectPoints)
        updateZoomWindow(sortedRectPoints)
        return


def onChangeZoom(value):
    global zoomValue
    if zoomValue != value:
        print(f'[DEBUG](onChangeZoom) @Zoom-Changed: {zoomValue} to {value}')
        zoomValue = value
        updateZoomWindow(sortedRectPoints)

def onChangeLUT(value):
    global lutValue
    if lutValue != value:
        print(f'[DEBUG](onChangeLUT) @LUT-Changed: {lutValue} to {value}')
        lutValue = value


cv2.setMouseCallback(mainWindowName, onMouse)
cv2.createTrackbar('Zoom:', mainWindowName, zoomValue, 3, onChangeZoom)
cv2.createTrackbar('LUT:', mainWindowName, lutValue, 13, onChangeLUT)
# Trackbar creates errors on CV2 v4.6.x release -> fix is in v5.x, see https://github.com/opencv/opencv/issues/22561#issuecomment-1257164504

showImage(grayImage, mainWindowName)

print('[DEBUG](main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

print('[DEBUG](main) Closing all windows.')
cv2.destroyAllWindows()
