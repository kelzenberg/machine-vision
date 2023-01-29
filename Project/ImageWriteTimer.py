"""
Timer-based image writer
"""

import cv2
from os import path as ospath
from threading import Timer


class ImageWriteTimer:
    def __init__(self, imageName: str, interval=10):
        self.filePath = ospath.abspath('./records')
        self.imageName = imageName
        self.interval = interval  # in seconds
        self.timer = None
        self.isBlocked = False
        self.imageCounter = 0

        print(
            f"(ImageWriteTimer) Timer for image writes initialized: {self.imageName} every {self.interval}s to '{self.filePath}/{self.imageName}_XXX.jpg'")

    def unblock(self):
        print(f'(ImageWriteTimer) ...image writes unblocked again.')
        self.isBlocked = False

    def stop(self, reason):
        if self.timer is not None:
            print(
                f'(VideoThreader) Stopping image writer timer...(reason: {reason})')
            self.timer.cancel()
            self.timer = None

    def write(self, image, objects):
        if self.isBlocked:
            return

        self.writeImage(image, objects)

        self.isBlocked = True
        self.timer = Timer(self.interval, self.unblock)
        self.timer.start()
        print(f'(ImageWriteTimer) Starting new timer to block image writes...')

    def writeImage(self, image, objects):
        for (x, y, w, h) in objects:
            cv2.imwrite(
                ospath.join(self.filePath,
                            f'{self.imageName}_{self.imageCounter}.jpg'),
                image.copy()[y:y+h, x:x+w],
                params=[cv2.IMWRITE_JPEG_QUALITY, 75]
            )
            self.imageCounter += 1
