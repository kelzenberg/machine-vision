"""
Multi-Threaded Video Capturing
"""

import cv2
from threading import Thread


class VideoThreader:
    def __init__(self, src=0):
        self.src = src
        self.feed = cv2.VideoCapture(src)
        self.retrieved, self.frame = self.feed.read()
        self.stopped = False

        if not self.feed.isOpened():
            print("(VideoThreader) Cannot access camera feed.")
            self.stop()

        width = int(self.feed.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.feed.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(self.feed.get(cv2.CAP_PROP_FPS))
        fourcc = int(self.feed.get(cv2.CAP_PROP_FOURCC))
        codec = bytes([v & 255 for v in (fourcc, fourcc >> 8,
                      fourcc >> 16, fourcc >> 24)]).decode()  # Source: https://stackoverflow.com/a/71838016
        backendAPI = self.feed.getBackendName()
        print(
            f'(VideoThreader) Video Feed loaded: {width}x{height} @ {fps}fps ({codec}) - via {backendAPI}')

    def start(self):
        self.thread = Thread(target=self.read, args=())
        self.thread.daemon = True  # keep thread runnning in the background
        self.thread.start()
        return self

    def stop(self):
        print('(VideoThreader) Stopping video feed.')
        self.stopped = True
        self.feed.release()

    def read(self):
        while not self.stopped:
            self.retrieved, self.frame = self.feed.read()
            if not self.retrieved:
                print("(VideoThreader) Cannot receive next frame.")
                self.stop()
