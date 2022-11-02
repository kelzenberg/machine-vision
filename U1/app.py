"""U1 app"""
import cv2

mainImage = cv2.imread('./Lena.bmp')
grayImage = cv2.cvtColor(cv2.cvtColor(
    mainImage, cv2.COLOR_RGB2GRAY), cv2.COLOR_GRAY2BGR)
print('[DEBUG](main) Image loaded.')

mainWindowName = 'Main'
zoomWindowName = 'Zoom & LUT'
cv2.namedWindow(mainWindowName, cv2.WINDOW_KEEPRATIO)
cv2.moveWindow(mainWindowName, 100, 100)
cv2.setWindowProperty(mainWindowName, cv2.WND_PROP_TOPMOST, 1)

rectanglePoints = [None, None]
sortedRectanglePoints = [None, None]
redColor = (0, 0, 255)  # Red in BGR
zoomValue = 0
lutValue = 0

"""
Utility functions
"""


def showImage(windowName, image):
    print('[DEBUG](showImage) Show image in window:', windowName)
    cv2.imshow(windowName, image)


def convertToGrayImage(image):
    return cv2.cvtColor(cv2.cvtColor(image, cv2.COLOR_RGB2GRAY), cv2.COLOR_GRAY2BGR)


def writeText(image, text):
    return cv2.putText(image, text, (10, 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, redColor, 1, cv2.LINE_AA)


def sortTwoPoints(points):
    [pointA, pointB] = points
    x1 = pointA[0] if pointA[0] < pointB[0] else pointB[0]
    x2 = pointB[0] if pointB[0] > pointA[0] else pointA[0]
    y1 = pointA[1] if pointA[1] < pointB[1] else pointB[1]
    y2 = pointB[1] if pointB[1] > pointA[1] else pointA[1]
    return [(x1, y1), (x2, y2)]


def isValidPoints(points):
    if points[0] == None or points[1] == None:
        # At least one Point is missing
        return False
    elif points[1][0]-points[0][0] <= 0 or points[1][1]-points[0][1] <= 0:
        # From- and To-Points are closer than 1 Pixel
        return False
    else:
        # Points are valid
        return True


"""
Rectangle functions
"""


def setRectanglePoints(x: int, y: int, slot: int):
    if slot == 0:
        rectanglePoints[0] = (x, y)
        return
    if slot == 1:
        rectanglePoints[1] = (x, y)
        return


def drawRectangle(points):
    print(f'[DEBUG](drawRectangle) with Points {points}')
    [fromPoint, toPoint] = points
    showImage(mainWindowName, cv2.rectangle(
        grayImage.copy(), fromPoint, toPoint, redColor, 2))


"""
Zoom & LUT functions
"""


def initZoomLUTWindow():
    cv2.destroyWindow(zoomWindowName)
    cv2.namedWindow(zoomWindowName, cv2.WINDOW_AUTOSIZE)
    cv2.moveWindow(zoomWindowName, 666, 100)


def updateZoomLUTWindow(points):
    print(f'[DEBUG](updateZoomWindow) with Points {points}')
    [(x1, y1), (x2, y2)] = points
    croppedImage = mainImage[y1:y2, x1:x2]

    displayedImage = cv2.resize(croppedImage, None, fx=zoomValue + 1,
                                fy=zoomValue + 1, interpolation=cv2.INTER_CUBIC)

    match lutValue:
        case 0:
            pass
        case 13:
            convertedImage = convertToGrayImage(displayedImage)
            displayedImage = writeText(
                convertedImage, f'Zoom: {zoomValue + 1}')
            pass
        case 14:
            invertedImage = cv2.bitwise_not(displayedImage)
            convertedImage = convertToGrayImage(invertedImage)
            displayedImage = writeText(
                convertedImage, f'Zoom: {zoomValue + 1}')
            pass
        case _:
            if 0 <= lutValue - 1 <= 11:
                displayedImage = cv2.applyColorMap(
                    displayedImage, lutValue - 1)
            pass

    showImage(zoomWindowName, displayedImage)


"""
ON-Event Handler
"""


def onMouse(event: int, x: int, y: int, flags: int, userdata=None):
    if event == 1:  # left-mouse-down
        print('[DEBUG](onMouse) @Left-Click-DOWN:', x, y, flags)
        setRectanglePoints(x, y, slot=0)
        initZoomLUTWindow()
        return

    if event == 0 and flags == 1:  # mouse moved & left-mouse down
        print('[DEBUG](onMouse) @Mouse-Moved:', x, y, flags)
        setRectanglePoints(x, y, slot=1)

        global rectanglePoints
        if rectanglePoints[0] == None or rectanglePoints[1] == None:
            return

        global sortedRectanglePoints
        sortedRectanglePoints = sortTwoPoints(rectanglePoints)
        if not isValidPoints(sortedRectanglePoints):
            return

        drawRectangle(sortedRectanglePoints)
        updateZoomLUTWindow(sortedRectanglePoints)
        return


def onChangeZoom(value):
    global zoomValue
    if zoomValue == value:
        return

    print(f'[DEBUG](onChangeZoom) @Zoom-Changed: {zoomValue} to {value}')
    zoomValue = value

    global sortedRectanglePoints
    if not isValidPoints(sortedRectanglePoints):
        return

    updateZoomLUTWindow(sortedRectanglePoints)


def onChangeLUT(value):
    global lutValue
    if lutValue == value:
        return

    print(f'[DEBUG](onChangeLUT) @LUT-Changed: {lutValue} to {value}')
    lutValue = value

    global sortedRectanglePoints
    if not isValidPoints(sortedRectanglePoints):
        return

    updateZoomLUTWindow(sortedRectanglePoints)


"""
Main function
"""

cv2.setMouseCallback(mainWindowName, onMouse)
cv2.createTrackbar('Zoom:', mainWindowName, zoomValue, 3, onChangeZoom)
cv2.createTrackbar('LUT:', mainWindowName, lutValue, 14, onChangeLUT)
# Trackbar creates errors on OpenCV v4.6.x release on MacOS -> fixed in v5.x
# see https://github.com/opencv/opencv/issues/22561#issuecomment-1257164504

showImage(mainWindowName, grayImage)

print('[DEBUG](main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

print('[DEBUG](main) Closing all windows.')
cv2.destroyAllWindows()
