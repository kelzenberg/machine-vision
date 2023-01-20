"""
OpenCV Window Helper
"""

import cv2
from threading import Thread


class WindowThreader:
    prevShowLog = ''

    def __init__(self, name, scale=1, offset=(0, 0), image=None):
        # setting up the cv2 window
        self.name = name
        self.scale = scale
        self.offset = offset

        # showing frames
        self.image = image
        self.stopped = False

        cv2.namedWindow(name, cv2.WINDOW_KEEPRATIO)
        cv2.moveWindow(name, offset[0], offset[1])
        cv2.setWindowProperty(name, cv2.WND_PROP_TOPMOST, 1)
        print(
            f'(Window.init) Init new Window "{name}": Scale {scale}, Offset {offset}')

    def addTrackbar(self, name, range, onChange, userData=None):
        if onChange == None:
            # allow no-op trackbars
            def onChange(_):
                pass
        cv2.createTrackbar(
            name, self.name, range[0], range[1], lambda value: onChange(value, userData))

    def setTrackbar(self, name, value):
        print(f'(Window.setTrackbar) Set trackbar "{name}" to {value}')
        cv2.setTrackbarPos(name, self.name, value)

    def destroy(self):
        print(f'(Window.destroy) Destroy "{self.name}" window')
        cv2.destroyWindow(self.name)

    def start(self):
        self.thread = Thread(target=self.show, args=())
        self.thread.daemon = True  # keep thread runnning in the background
        self.thread.start()
        return self

    def stop(self):
        print('(Window.stop) Stopping image showing')
        self.stopped = True

    def setImage(self, image):
        self.image = image

    def show(self):
        if self.image is None:
            return

        while not self.stopped:
            log = f'(Window.show) Show new image in "{self.name}" window'
            if log != self.prevShowLog:
                self.prevShowLog = log
                print(log)

            preview = cv2.resize(
                self.image, None, fx=self.scale, fy=self.scale, interpolation=cv2.INTER_AREA)
            cv2.imshow(self.name, preview)
