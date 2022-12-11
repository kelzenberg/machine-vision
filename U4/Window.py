"""
OpenCV Window Helper
"""

import cv2


class Window:
    debugPrint = ''

    def __init__(self, name, scale=1, offset=(0, 0)):
        self.name = name
        self.scale = scale
        self.offset = offset

        cv2.namedWindow(name, cv2.WINDOW_KEEPRATIO)
        cv2.moveWindow(name, offset[0], offset[1])
        cv2.setWindowProperty(name, cv2.WND_PROP_TOPMOST, 1)
        print(
            f'(Window.init) Init new Window "{name}": Scale {scale}, Offset {offset}')

    def addTrackbar(self, name, range, onChange):
        cv2.createTrackbar(name, self.name, range[0], range[1], onChange)

    def setTrackbar(self, name, value):
        cv2.setTrackbarPos(name, self.name, value)

    def destroy(self):
        print(f'(Window.destroy) Destroy "{self.name}" window')
        cv2.destroyWindow(self.name)

    def show(self, imageName, image):
        log = f'(Window.show) Show in "{self.name}" window: {imageName}'
        if log != self.debugPrint:
            self.debugPrint = log
            print(log)

        preview = cv2.resize(image, None, fx=self.scale,
                             fy=self.scale, interpolation=cv2.INTER_AREA)

        if (len(preview.shape) < 3):
            preview = cv2.cvtColor(preview, cv2.COLOR_GRAY2BGR)

        preview = cv2.putText(
            preview, imageName.capitalize(), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
        cv2.imshow(self.name, preview)
