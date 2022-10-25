"""U1 app"""
import cv2

imgWindowName = "main"


def showImage(path: str = './Lena.bmp'):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    print('Image loaded.')
    cv2.namedWindow(imgWindowName)
    print('Show image...')
    cv2.imshow(imgWindowName, img)


def onMouse(event: int, x: int, y: int, flags: int, userdata):
    if event == 1:
        print('onMouse @click:', x, y, flags, userdata)
        return


showImage()
cv2.setMouseCallback(imgWindowName, onMouse)

print('Press Q to exit...')
keyCode = cv2.waitKeyEx(0)
print('Closing all windows.', keyCode)
cv2.destroyAllWindows()
