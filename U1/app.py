"""U1 app"""
import os
import cv2

print("Path:", os.path.abspath(os.getcwd()))


def loadShowImage():
    img = cv2.imread('./Lena.bmp', cv2.IMREAD_GRAYSCALE)
    print('Image loaded')
    cv2.namedWindow('main')
    cv2.imshow('main', img)
    print('Waiting for user input...')
    cv2.waitKey(0)
    print('Closing all windows')
    cv2.destroyAllWindows()

loadShowImage()
