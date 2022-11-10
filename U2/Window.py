import cv2


class Window:
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

    def show(self, name, image):
        # print(f'(Window.show) Show in "{self.name}" window: {name} {image.shape}')
        preview = cv2.resize(image, None, fx=self.scale,
                             fy=self.scale, interpolation=cv2.INTER_AREA)
        cv2.imshow(self.name, preview)
