"""
Multi-Threaded Video Feed Reader
"""

import cv2
from threading import Thread, Event


class VideoThreader:
    def __init__(self, src=0):
        self.thread = None
        self.stopEvent = None

        self.src = src
        self.feed = cv2.VideoCapture(src)

        if not self.feed.isOpened():
            print("(VideoThreader) Cannot access camera feed.")
            self.stop(reason='no-camera-feed')

        width = int(self.feed.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.feed.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.size = (width, height)

        fps = int(self.feed.get(cv2.CAP_PROP_FPS))
        fourcc = int(self.feed.get(cv2.CAP_PROP_FOURCC))
        codec = bytes([v & 255 for v in (fourcc, fourcc >> 8,
                      fourcc >> 16, fourcc >> 24)]).decode()  # Source: https://stackoverflow.com/a/71838016
        backendAPI = self.feed.getBackendName()
        print(
            f'(VideoThreader) Video Feed initialized: {width}x{height} @ {fps}fps ({codec}) - via {backendAPI}')

    def start(self):
        print('(VideoThreader) Starting video feed...')
        self.stopEvent = Event()
        self.thread = Thread(target=self.readFeed, args=())
        self.thread.daemon = True  # keep thread runnning in the background until main app exits
        self.thread.start()
        print('(VideoThreader) ...video feed started.')
        return self

    def stop(self, reason):
        print(f'(VideoThreader) Stopping video feed...(reason: {reason})')
        if self.stopEvent is not None:
            self.stopEvent.set()
        if self.thread is not None:
            self.thread.join()
        self.feed.release()
        print('(VideoThreader) ...video feed stopped.')

    def readFeed(self):
        while not self.stopEvent.is_set():
            self.retrieved, self.frame = self.feed.read()
            if not self.retrieved:
                print("(VideoThreader) Cannot receive next frame.")
                self.stop(reason='no-next-frame')

    def hasStopped(self):
        stopped = self.stopEvent is not None and self.stopEvent.is_set()
        if stopped:
            print('(VideoThreader) Video feed has stopped.')
        return stopped

    def getLatestFrame(self):
        return self.frame

    def getFrameSize(self):
        return self.size
