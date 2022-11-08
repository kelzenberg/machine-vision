import cv2


class Window:
    def __init__(self, name, image, scale=0.33, offset=(0, -20)):
        self.name = name
        self.image = cv2.resize(image, None, fx=scale,
                                fy=scale, interpolation=cv2.INTER_AREA)
        cv2.namedWindow(name, cv2.WINDOW_KEEPRATIO)
        cv2.moveWindow(name, offset[0], offset[1])
        cv2.setWindowProperty(name, cv2.WND_PROP_TOPMOST, 1)

    def show(self):
        print('[DEBUG](Window.show) Show image in window:', self.name)
        cv2.imshow(self.name, self.image)
