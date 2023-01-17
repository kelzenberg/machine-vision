"""
Body Feature Detector
"""

import cv2
from typing import Dict
from glob import glob
from os import path as ospath

classifiers: Dict[str, cv2.CascadeClassifier] = {}
globPath = ospath.join(ospath.abspath('./data'), '*.xml')

for file in sorted(glob(globPath)):
    fileName = file.split('/')[-1].split('.')[0]
    classifiers[fileName] = cv2.CascadeClassifier(file)
    print(f'(detector) Classifier loaded: {fileName}')

upperBodyClassifier = classifiers['haarcascade_upperbody']


def detectUpperBody(image):
    gray = cv2.equalizeHist(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
    bodies = upperBodyClassifier.detectMultiScale(
        gray
    )
    for (x, y, w, h) in bodies:
        cv2.rectangle(gray, (x, y), (x + w, y + h),
                      (0, 255, 0), 1, lineType=cv2.LINE_AA)
        cv2.putText(gray, "Upper Body Detected", (x + 5, y + 15),
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 2)
    return gray
