"""
Multi-Threaded Video Recorder (& Writer)
"""

import cv2
from threading import Thread, Event, Timer
from os import path as ospath


class RecorderThreader:
    def __init__(self, inputSize):
        self.thread = None
        self.stopEvent = Event()
        self.timerLimit = 5  # seconds
        self.timer = Timer(self.timerLimit, self.stop,
                           kwargs={'reason': 'on-timer'})
        self.image = None

        self.filePath = ospath.join(ospath.abspath('./records'), 'output.mp4')
        self.codec = cv2.VideoWriter_fourcc(*'avc1')
        self.fps = 12
        self.scale = 0.5
        self.size = (int(inputSize[0] * self.scale),
                     int(inputSize[1] * self.scale))
        self.writer = cv2.VideoWriter(
            self.filePath, self.codec, self.fps, self.size)

        if not self.writer.isOpened():
            print("(RecorderThreader) Cannot initialize video writer.")
            self.stop(reason='no-video-writer')

        fourcc = bytes([v & 255 for v in (self.codec, self.codec >> 8, self.codec >> 16,
                       self.codec >> 24)]).decode()  # Source: https://stackoverflow.com/a/71838016
        print(
            f"(RecorderThreader) Video recording to file initialized: {self.size[0]}x{self.size[1]} @ {self.fps}fps to '{self.filePath}' ({fourcc})")

    def start(self):
        print('(RecorderThreader) Starting video recording...')
        self.stopEvent = Event()
        self.thread = Thread(target=self.writeImage, args=())
        self.thread.daemon = True  # keep thread runnning in the background until main app exits
        self.thread.start()

        self.writer.open(self.filePath, self.codec, self.fps, self.size)
        if not self.writer.isOpened():
            print("(RecorderThreader) Cannot initialize video writer.")
            self.stop(reason='no-video-writer')

        self.timer.start()
        print(
            f'(RecorderThreader) ...video recording started for {self.timerLimit} seconds.')
        return self

    def stop(self, reason):
        print(
            f'(RecorderThreader) Stopping video recording...(reason: {reason})')
        self.stopEvent.set()
        self.writer.release()
        if self.thread is not None:
            self.thread.join()
        print('(RecorderThreader) ...video recording stopped.')

    def writeImage(self):
        while True:
            if not self.writer.isOpened() \
                    or self.stopEvent.is_set() \
                    or self.image is None:
                break

            print("write")
            preview = cv2.resize(self.image, None, fx=self.scale,
                                 fy=self.scale, interpolation=cv2.INTER_AREA)
            self.writer.write(cv2.cvtColor(preview, cv2.COLOR_BGR2HSV))

    def isNotRunning(self):
        return self.thread is None or self.stopEvent.is_set()

    def updateImage(self, image):
        self.image = image
