import cv2


class Window:
    def __init__(self, name, image, scale=0.2, offset=(0, 0)):
        self.name = name
        self.image = image
        self.scale = scale
        self.offset = offset
        self.generatePreview()

        cv2.namedWindow(name, cv2.WINDOW_KEEPRATIO)
        cv2.moveWindow(name, offset[0], offset[1])
        cv2.setWindowProperty(name, cv2.WND_PROP_TOPMOST, 1)
        print(
            f'(Window.init) Init new Window "{name}": \n    Shape: {image.shape} \n    Preview: {self.preview.shape}, \n    Scale: {scale}, Offset: {offset}')

    def generatePreview(self):
        self.preview = cv2.resize(
            self.image, None, fx=self.scale, fy=self.scale, interpolation=cv2.INTER_AREA)

    def addTrackbar(self, name, min, max, onChange):
        cv2.createTrackbar(name, self.name, min, max, onChange)

    def updateImage(self, image):
        self.image = image
        self.generatePreview()

    def show(self):
        print(f'(Window.show) Show "{self.name}" image')
        cv2.imshow(self.name, self.preview)
