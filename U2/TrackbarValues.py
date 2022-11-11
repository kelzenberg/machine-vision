"""
Trackbar Values Store
"""


class TrackbarValues:
    operator = 0
    filter = 0
    sigma = 0
    kernel = 0

    @classmethod
    def updateOperator(self, value):
        self.operator = value

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
    f'(TrackbarValues.init) Operator: {TrackbarValues.operator}, Filter: {TrackbarValues.filter}, Sigma: {TrackbarValues.sigma}, Kernel: {TrackbarValues.kernel}')
