"""
Trackbar Values Store
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

    @classmethod
    def updateKernel(self, value):
        self.kernel = value


print(
    f'(TrackbarValues.init) Filter: {TrackbarValues.filter}, Sigma: {TrackbarValues.sigma}, Kernel: {TrackbarValues.kernel}')
