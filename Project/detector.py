"""
Body Feature Detector
"""

import cv2
from typing import Dict, Tuple
from glob import glob
from os import path as ospath

classifiers: Dict[str, cv2.CascadeClassifier] = {}
globPath = ospath.join(ospath.abspath('./data'), '*.xml')

for file in sorted(glob(globPath)):
    fileName = file.split('/')[-1].split('.')[0]
    classifiers[fileName] = cv2.CascadeClassifier(file)
    print(f'(detector) Classifier loaded: {fileName}')

upperBodyClassifier = classifiers['haarcascade_upperbody']


def detectUpperBody(image, scaleFactor: float, minNeighbors: int, minSize: Tuple[int, int]):
    gray = cv2.equalizeHist(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
    preview = cv2.cvtColor(gray.copy(), cv2.COLOR_GRAY2BGR)
    bodies = upperBodyClassifier.detectMultiScale(
        gray,
        # scaleFactor: How much the image size is reduced at each image scaling for detection
        scaleFactor=scaleFactor,  # equals 5% resizing per step
        # minNeighbors: Affects the quality of the detected objects.
        #   Higher value = fewer detections but with higher quality.
        minNeighbors=minNeighbors,
        # minSize: Minimum possible object size. Objects smaller than that are ignored.
        minSize=minSize
    )
    for (x, y, w, h) in bodies:
        cv2.rectangle(preview, (x, y), (x + w, y + h),
                      (255, 255, 0), 3, lineType=cv2.LINE_AA)
        cv2.putText(preview, "Upper Body\nDetected", (x + 12, y + 27),
                    cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 0), 2)
    return preview
