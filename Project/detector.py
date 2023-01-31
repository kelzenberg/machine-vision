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
    return cv2.equalizeHist(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))


def drawResults(grayPreview, objects, type: str, color=(255, 255, 0)):
    for idx, (x, y, w, h) in enumerate(objects):
        cv2.rectangle(grayPreview, (x, y), (x + w, y + h),
                      color, 2, lineType=cv2.LINE_AA)
        cv2.putText(grayPreview, f'{type.capitalize()} detected ({idx + 1})',
                    (x + 7, y + 17), cv2.FONT_HERSHEY_COMPLEX, 0.5, color, 2)
    return grayPreview


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
