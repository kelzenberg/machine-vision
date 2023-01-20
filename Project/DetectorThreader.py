"""
Multi-Threaded Image Detector
"""

import cv2
from typing import Any, Dict
from threading import Thread


class DetectorThreader:
    def __init__(self, classifier: cv2.CascadeClassifier, classifierConfig: Dict[str, Any], image):
        self.classifier = classifier
        self.config = classifierConfig
        self.image = image
        self.preview = None
        self.stopped = False
        print(f'(DetectorThreader) Init Detector.')

    def start(self):
        print('(DetectorThreader) Starting detection.')
        self.thread = Thread(target=self.detectUpperBody, args=())
        self.thread.daemon = True  # keep thread runnning in the background
        self.thread.start()
        return self

    def stop(self):
        print('(DetectorThreader) Stopping detection.')
        self.stopped = True

    def setImage(self, image):
        self.image = image

    def getPreview(self):
        return self.preview

    def detectUpperBody(self):
        while not self.stopped:
            if self.image is None:
                return

            gray = cv2.equalizeHist(cv2.cvtColor(
                self.image, cv2.COLOR_BGR2GRAY))
            preview = cv2.cvtColor(gray.copy(), cv2.COLOR_GRAY2BGR)

            bodies = self.classifier.detectMultiScale(
                gray,
                # scaleFactor: How much the image size is reduced at each image scaling for detection
                scaleFactor=self.config['scaleFactor'],
                # minNeighbors: Affects the quality of the detected objects.
                #   Higher value = fewer detections but with higher quality.
                minNeighbors=self.config['minNeighbors'],
                # minSize: Minimum possible object size. Objects smaller than that are ignored.
                minSize=self.config['minSize']
            )

            for (x, y, w, h) in bodies:
                cv2.rectangle(preview, (x, y), (x + w, y + h),
                              (255, 255, 0), 2, lineType=cv2.LINE_AA)
                cv2.putText(preview, "Upper Body\nDetected", (x + 7, y + 17),
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 0), 2)

            self.preview = preview
