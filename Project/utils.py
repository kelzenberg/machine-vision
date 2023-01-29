"""
OpenCV Utils
"""

import cv2
from datetime import datetime


def putTimestamp(image):
    height = image.shape[0]
    width = image.shape[1]
    image = cv2.rectangle(image, (width-165, height-20), (width, height),
                          (0, 0, 0), -1, lineType=cv2.LINE_AA)
    image = cv2.putText(image, f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}',
                        (width-150, height-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (242, 242, 242), 1, cv2.LINE_AA)
    return image
