"""
OpenCV Utils
"""

import cv2
from datetime import datetime
from typing import Any, Dict, List
from numpy import bitwise_xor


def isEqualImage(image1, image2):
    # source: https://stackoverflow.com/a/23199159
    return image1.shape == image2.shape and not (bitwise_xor(image1, image2).any())


def drawObjectRegions(image, detected: List[Dict[str, Any]]):
    color3C = image.copy()
    gray3C = cv2.cvtColor(
        cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY),
        cv2.COLOR_GRAY2BGR
    )

    for items in detected:
        type = items['type']
        objects = items['objects']
        color = items['color']
        for idx, (x, y, w, h) in enumerate(objects):
            for img in [color3C, gray3C]:
                cv2.rectangle(img, (x, y), (x + w, y + h),
                              color, 2, lineType=cv2.LINE_AA)
                cv2.putText(img, f'{type.capitalize()}\ndetected ({idx + 1})',
                            (x + 7, y + 17), cv2.FONT_HERSHEY_COMPLEX, 0.5, color, 2)

    return color3C, gray3C


def getCurrentISOTime():
    return datetime.now().isoformat(timespec='seconds')


def putTimestamp(image):
    height = image.shape[0]
    width = image.shape[1]
    image = cv2.rectangle(image, (width-165, height-20), (width, height),
                          (0, 0, 0), -1, lineType=cv2.LINE_AA)
    image = cv2.putText(image, f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}',
                        (width-150, height-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (242, 242, 242), 1, cv2.LINE_AA)
    return image
