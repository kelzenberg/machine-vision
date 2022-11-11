import cv2

"""
Load Image
"""

mainImage = cv2.imread('./Stop.jpg')
print('(main) Image loaded')

"""
Images Store
"""


class Images:
    gray = cv2.cvtColor(mainImage, cv2.COLOR_RGB2GRAY)
    filtered = gray.copy()
    edges = gray.copy()

    @classmethod
    def updateGrayImage(self, image):
        self.gray = image

    @classmethod
    def updateFilteredImage(self, image):
        self.filtered = image

    @classmethod
    def updateEdgesImage(self, image):
        self.edges = image


print(
    f'(Images.init) Gray: {Images.gray.shape}, Filtered: {Images.filtered.shape}, Edges: {Images.edges.shape}')
