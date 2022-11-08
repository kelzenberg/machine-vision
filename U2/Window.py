import cv2


class Window:
    def __init__(self, name, image, scale=0.2, offset=(0, 0)):
        self.name = name
        self.image = image
        self.preview = cv2.resize(image, None, fx=scale,
                                  fy=scale, interpolation=cv2.INTER_AREA)
        cv2.namedWindow(name, cv2.WINDOW_KEEPRATIO)
        cv2.moveWindow(name, offset[0], offset[1])
        cv2.setWindowProperty(name, cv2.WND_PROP_TOPMOST, 1)
        print(
            f'(Window.init) Init new Window "{name}": \n    Shape: {image.shape} \n    Preview: {self.preview.shape}, \n    Scale: {scale}, Offset: {offset}')

    def show(self):
        print(f'(Window.show) Show "{self.name}" image')
        cv2.imshow(self.name, self.preview)
