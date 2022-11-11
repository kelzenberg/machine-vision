"""
Trackbar Values
"""


class TrackbarValues:
    filter = 0
    sigma = 0
    kernel = 0

    @classmethod
    def updateFilter(self, value):
        self.filter = value

    @classmethod
    def updateSigma(self, value):
        self.sigma = value
        self.kernel = 1 # needed for sigma

    @classmethod
    def updateKernel(self, value):
        self.kernel = value
        self.sigma = 0 # needed to not overwrite kernel
