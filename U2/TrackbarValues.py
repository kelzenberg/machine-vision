"""
Trackbar Values Store
"""


class TrackbarValues:
    operator = 0
    filter = 0
    sigma = 0
    kernel = 0
    threshold = 0
    threshold2 = 301
    displayValue = 0

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

    @classmethod
    def updateThreshold(self, value):
        self.threshold = value

    @classmethod
    def updateThreshold2(self, value):
        self.threshold2 = value

    @classmethod
    def updateDisplayValue(self, value):
        self.displayValue = value


print(
    f'(TrackbarValues.init) Operator: {TrackbarValues.operator}, Filter: {TrackbarValues.filter}, Sigma: {TrackbarValues.sigma}, Kernel: {TrackbarValues.kernel}')
