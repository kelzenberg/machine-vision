"""
Timer-based image writer
"""

import cv2
from os import path as ospath
from threading import Timer
from utils import putTimestamp, getCurrentISOTime


class ImageWriteTimer:
    def __init__(self, type: str, interval=10):
        self.type = type
        self.filePath = ospath.abspath('./records')
        self.fileNameTemplate = '{0}_{1}-{2}.jpg'
        self.interval = interval  # in seconds
        self.timer = None
        self.isBlocked = False

        print(
            f"(ImageWriteTimer) Timer for image writes initialized:\
                \n                  Type '{self.type}' saved every {self.interval}s to '{self.filePath}/{self.fileNameTemplate.format('{DATE}', self.type, '{#}')}'")

    def unblock(self):
        print(f'(ImageWriteTimer) ...image writes are unblocked again.')
        self.isBlocked = False

    def stop(self, reason):
        if self.timer is not None:
            print(
                f'(ImageWriteTimer) Stopping image writer timer...(reason: {reason})')
            self.timer.cancel()
            self.timer = None
            print('(ImageWriteTimer) ...image writer timer stopped.')

    def update(self, image, objects):
        if self.isBlocked:
            return

        self.writeImages(image, objects)

        self.isBlocked = True
        self.timer = Timer(self.interval, self.unblock)
        self.timer.start()
        print(
            f'(ImageWriteTimer) Blocking further image writes for {self.interval} seconds...')

    def writeImages(self, image, objects):
        buffer = 10  # pixel
        for idx, (x, y, w, h) in enumerate(objects):
            preview = image.copy()[y-buffer:y+h+buffer, x-buffer:x+w+buffer]
            preview = putTimestamp(preview)
            fileName = self.fileNameTemplate.format(
                getCurrentISOTime(), self.type, idx
            )

            cv2.imwrite(
                ospath.join(self.filePath, fileName),
                preview,
                params=[cv2.IMWRITE_JPEG_QUALITY, 75]
            )

            print(f"(ImageWriteTimer) Saved image '{fileName}'")
