"""
Multi-Threaded Video Recorder (& Writer)
"""

import cv2
from threading import Thread, Event, Timer
from os import path as ospath
from utils import putTimestamp, getCurrentISOTime


class RecorderThreader:
    def __init__(self, inputSize, fps=6, recordingLimitSec=10):
        self.stopEvent = Event()
        self.thread = None

        self.timer = None
        self.timerLimit = recordingLimitSec  # seconds

        self.writer = None
        self.filePath = ospath.abspath('./records')
        self.fileNameTemplate = '{0}_recording.mp4'
        self.lastFileName = ''
        self.fps = fps
        self.codec = 'avc1'
        self.fourcc = cv2.VideoWriter_fourcc(*self.codec)
        self.scale = 0.5
        self.size = (int(inputSize[0] * self.scale),
                     int(inputSize[1] * self.scale))
        self.image = None
        self.imageTimestamp = 0
        self.processedImageTimestamp = 0

        print(
            f"(RecorderThreader) Video recording to file initialized:\
                \n                   {self.size[0]}x{self.size[1]} @ {self.fps}fps ({self.codec} codec), saved to '{self.filePath}/{self.fileNameTemplate.format('{DATE}')}'.")

    def start(self):
        print(
            f'(RecorderThreader) Starting video recording for {self.timerLimit} seconds....')

        self.lastFileName = self.fileNameTemplate.format(getCurrentISOTime())
        self.writer = cv2.VideoWriter(
            ospath.join(self.filePath, self.lastFileName),
            self.fourcc,
            self.fps,
            self.size
        )

        if not self.writer.isOpened():
            print('(RecorderThreader) Video writer is not initialized.')
            self.stop(reason='no-video-writer-on-start')

        print(
            f"(RecorderThreader) Used video writer backend API: '{self.writer.getBackendName()}'.")

        self.stopEvent = Event()
        self.thread = Thread(target=self.writeImage, args=())
        self.thread.daemon = True  # keep thread runnning in the background until main app exits
        self.thread.start()

        self.timer = Timer(self.timerLimit, self.stop, kwargs={
                           'reason': f'time-is-up-({self.timerLimit}s)'})
        self.timer.start()

        print('(RecorderThreader) ...video recording started.')
        return self

    def stop(self, reason):
        print(
            f'(RecorderThreader) Stopping video recording...(reason: {reason})')
        self.stopEvent.set()
        if self.writer is not None:
            self.writer.release()
            print(f"(RecorderThreader) Saved video '{self.lastFileName}'")
        if self.timer is not None:
            self.timer.cancel()
        print('(RecorderThreader) ...video recording stopped.')

    def writeImage(self):
        prevLog = ''

        while True:
            if self.stopEvent.is_set():
                log = '(RecorderThreader) -- Stopping video.'
                break

            if not self.writer.isOpened():
                print('(RecorderThreader) Video writer is not initialized.')
                self.stop(reason='no-video-writer-on-write')
                break

            if self.imageTimestamp == self.processedImageTimestamp:
                # To-be-written image did not update. Skipping writing of image to video.
                continue

            log = f'(RecorderThreader) -- Writing video frame (@{self.imageTimestamp}ms)'
            if prevLog != log:
                prevLog = log
                print(log)

            preview = putTimestamp(self.image)
            preview = cv2.resize(preview, None, fx=self.scale,
                                 fy=self.scale, interpolation=cv2.INTER_AREA)

            self.writer.write(preview)
            self.processedImageTimestamp = self.imageTimestamp

    def isRecording(self):
        return self.timer is not None and not self.timer.finished.is_set()

    def updateImage(self, image, timestamp):
        self.imageTimestamp = timestamp
        self.image = image
