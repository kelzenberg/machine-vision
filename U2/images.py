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
    gradientX = gray.copy()
    gradientY = gray.copy()
    maxXY = gray.copy()
    sumXY = gray.copy()
    binary = gray.copy()
    canny = gray.copy()

    @classmethod
    def updateGray(self, image):
        self.gray = image

    @classmethod
    def updateFiltered(self, image):
        self.filtered = image

    @classmethod
    def updateGradientX(self, image):
        self.gradientX = image

    @classmethod
    def updateGradientY(self, image):
        self.gradientY = image

    @classmethod
    def updateMaxXY(self, image):
        self.maxXY = image

    @classmethod
    def updateSumXY(self, image):
        self.sumXY = image

    @classmethod
    def updateBinary(self, image):
        self.binary = image

    @classmethod
    def updateCanny(self, image):
        self.canny = image


print(
    f'(Images.init) Gray: {Images.gray.shape}')
