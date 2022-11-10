import cv2
from utils import convertToGrayBGR

"""
Load Image
"""

mainImage = cv2.imread('./Stop.jpg')
print('(Images) Image loaded.')
grayImage = convertToGrayBGR(mainImage)
filteredImage = grayImage.copy()
edgesImage = filteredImage.copy()
