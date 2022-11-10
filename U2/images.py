import cv2

"""
Load Image
"""

mainImage = cv2.imread('./Stop.jpg')
print('(Images) Image loaded.')

grayImage = cv2.cvtColor(mainImage, cv2.COLOR_RGB2GRAY)
filteredImage = grayImage.copy()
edgesImage = filteredImage.copy()
