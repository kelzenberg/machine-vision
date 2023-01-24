"""
Multi-Threaded Video Recorder (& Writer)
"""

import cv2
from threading import Thread
from os import path as ospath


class RecorderThreader:
    def __init__(self, inputSize):
        self.filePath = ospath.join(ospath.abspath('./records'), 'output.mp4')
        self.codec = cv2.VideoWriter_fourcc(*'mp4v')
        self.fps = 12
        self.scale = 0.5
        self.size = (int(inputSize[0] * self.scale),
                     int(inputSize[1] * self.scale))
        self.writer = cv2.VideoWriter(
            self.filePath, self.codec, self.fps, self.size)
        self.stopped = True

        fourcc = bytes([v & 255 for v in (self.codec, self.codec >> 8, self.codec >> 16,
                       self.codec >> 24)]).decode()  # Source: https://stackoverflow.com/a/71838016
        print(
            f"(RecorderThreader) Video recording to file started: {self.size[0]}x{self.size[1]} @ {self.fps}fps to '{self.filePath}' ({fourcc})")

    def start(self):
        self.thread = Thread(target=self.write, args=())
        self.thread.daemon = True  # keep thread runnning in the background
        self.thread.start()
        self.stopped = False
        print('(RecorderThreader) Starting recording to file.')
        return self

    def stop(self):
        self.stopped = True
        self.writer.release()
        self.writer = None
        print('(RecorderThreader) Stopping recording to file.')

    def write(self):
        while not self.stopped:
            if self.image is not None:
                preview = cv2.resize(self.image, None, fx=self.scale,
                                     fy=self.scale, interpolation=cv2.INTER_AREA)
                self.writer.write(cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV))

    def updateImage(self, image):
        self.image = image

    def isRunning(self):
        return not self.stopped
