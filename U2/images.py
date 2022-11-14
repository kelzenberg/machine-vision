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
    gradientX = gray.copy()
    gradientY = gray.copy()
    gradientXY = gray.copy()
    binary = gray.copy()

    @classmethod
    def updateGray(self, image):
        self.gray = image

    @classmethod
    def updateFiltered(self, image):
        self.filtered = image

    @classmethod
    def updateEdges(self, image):
        self.edges = image

    @classmethod
    def updateGradientX(self, image):
        self.gradientX = image

    @classmethod
    def updateGradientY(self, image):
        self.gradientY = image

    @classmethod
    def updateGradientXY(self, image):
        self.gradientXY = image

    @classmethod
    def updateBinary(self, image):
        self.binary = image


print(
    f'(Images.init) Gray: {Images.gray.shape}, Filtered: {Images.filtered.shape}, Edges: {Images.edges.shape}')
