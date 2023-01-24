"""
Body Feature Detector
"""

import cv2
from os import path as ospath
from glob import glob
from typing import Dict, Tuple

classifiers: Dict[str, cv2.CascadeClassifier] = {}
globPath = ospath.join(ospath.abspath('./data'), '*.xml')

for file in sorted(glob(globPath)):
    fileName = file.split('/')[-1].split('.')[0]
    classifiers[fileName] = cv2.CascadeClassifier(file)
    print(f'(detector) Classifier loaded: {fileName}')

upperBodyClassifier = classifiers['haarcascade_upperbody']
frontalFaceClassifier = classifiers['haarcascade_frontalface']


def prepareForClassifier(image):
    gray = cv2.equalizeHist(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
    preview = cv2.cvtColor(gray.copy(), cv2.COLOR_GRAY2BGR)
    return gray, preview


def drawResults(image, objects, type: str):
    color = (0, 255, 255) if type == 'face' else (255, 255, 0)

    for (x, y, w, h) in objects:
        cv2.rectangle(image, (x, y), (x + w, y + h),
                      color, 2, lineType=cv2.LINE_AA)
        cv2.putText(image, f'{type.capitalize()} detected',
                    (x + 7, y + 17), cv2.FONT_HERSHEY_COMPLEX, 0.5, color, 2)

    return image


def detectUpperBody(image, scaleFactor: float, minNeighbors: int, minSize: Tuple[int, int]):
    return upperBodyClassifier.detectMultiScale(
        image,
        # scaleFactor: How much the image size is reduced at each image scaling for detection
        scaleFactor=scaleFactor,  # equals 5% resizing per step
        # minNeighbors: Affects the quality of the detected objects.
        #   Higher value = fewer detections but with higher quality.
        minNeighbors=minNeighbors,
        # minSize: Minimum possible object size. Objects smaller than that are ignored.
        minSize=minSize
    )


def detectFace(image, scaleFactor: float, minNeighbors: int, minSize: Tuple[int, int]):
    return frontalFaceClassifier.detectMultiScale(
        image,
        # scaleFactor: How much the image size is reduced at each image scaling for detection
        scaleFactor=scaleFactor,  # equals 5% resizing per step
        # minNeighbors: Affects the quality of the detected objects.
        #   Higher value = fewer detections but with higher quality.
        minNeighbors=minNeighbors,
        # minSize: Minimum possible object size. Objects smaller than that are ignored.
        minSize=minSize
    )
