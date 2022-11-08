import cv2


class Window:
    def __init__(self, name, image, offset=(100, 100)):
        self.name = name
        self.image = image
        cv2.namedWindow(name, cv2.WINDOW_KEEPRATIO)
        cv2.moveWindow(name, offset[0], offset[1])
        cv2.setWindowProperty(name, cv2.WND_PROP_TOPMOST, 1)

    def show(self):
        print('[DEBUG](Window.show) Show image in window:', self.name)
        cv2.imshow(self.name, self.image)
